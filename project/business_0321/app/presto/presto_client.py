#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    presto_client
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

"""
DB-API implementation backed by Presto
"""

from __future__ import absolute_import
from __future__ import unicode_literals

try:    #Python2.7
    from urllib import urlencode as urlencode
    from urllib import urlopen as urlopen
    from urllib2 import Request as request
except:    #Python3.6
    from urllib.parse import urlencode as urlencode
    from urllib.request import urlopen as urlopen
    from urllib.request import Request as request

from builtins import object
import json
from pyhive import common
from pyhive.common import DBAPITypeObject

"""
Make all exceptions visible in this module per DB-API
"""
from pyhive.exc import *    #noqa
import base64
import getpass
import logging
import requests
from requests.auth import HTTPBasicAuth
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

try:    #Python 3.6
    import urllib.parse as urlparse
except ImportError:    #Python 2.7
    import urlparse

"""
PEP 249 module globals
"""
apilevel = '2.0'
threadsafety = 2    #Threads may share the module and connections.
paramstyle = 'pyformat'    #Python extended format codes

_logger = logging.getLogger(__name__)
_escaper = common.ParamEscaper()

def connect(*args, **kwargs):
    """
    Constructor for creating a connection to the database.
    :returns: a :py:class:`Connection` object.
    """
    return Connection(*args, **kwargs)

class Connection(object):
    """
    Presto does not have a notion of a persistent connection.
    Thus, these objects are small stateless factories for cursors, which do all the real work.
    """
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def close(self):
        """
        Presto does not have anything to close
        """
        pass

    def commit(self):
        """
        Presto does not support transactions
        """
        pass

    def cursor(self):
        """
        Return a new :py:class:`Cursor` object using the connection.
        """
        return Cursor(*self._args, **self._kwargs)

    def rollback(self):
        raise NotSupportedError("Presto does not have transactions")    #pragma: no cover


class Cursor(common.DBAPICursor):
    """
    These objects represent a database cursor, which is used to manage the context of a fetch operation.
    """

    def __init__(self, host, port='8080', username=None, catalog='hive', group='adhoc',
                 schema='default', poll_interval=1, source='pyhive', session_props=None,
                 protocol='https', password=None, requests_session=None, requests_kwargs={'verify': False}):
        """
        :param host: hostname to connect
        :param port: int
        :param username: string
        :param catalog: string
        :param schema: string
        :param poll_interval: int
        :param source: string
        :param protocol: string
        :param password: string
            Using BasicAuth, requires ``https``.
        :param requests_session: a ``requests.Session`` object for advanced usage.
            Caller is responsible for closing session.
        :param requests_kwargs: Additional ``**kwargs`` to pass to requests
        """

        super(Cursor, self).__init__(poll_interval)
        """
        Config
        """
        self._host = host
        self._port = port
        self._username = username or getpass.getuser()
        self._catalog = catalog
        self._schema = schema
        self._arraysize = 1
        self._poll_interval = poll_interval
        self._source = source
        self._session_props = session_props if session_props is not None else {}
        self._token = None
        self._group = group
        self._password = password

        if protocol not in ('http', 'https'):
            raise ValueError("Protocol must be http/https, is {!r}".format(protocol))
        self._protocol = protocol
        self._requests_session = requests_session or requests

        requests_kwargs = dict(requests_kwargs) if requests_kwargs is not None else {}
        if password is not None and 'auth' in requests_kwargs:
            raise ValueError("Cannot use both password and requests_kwargs authentication")
        for k in ('method', 'url', 'data', 'headers'):
            if k in requests_kwargs:
                raise ValueError("Cannot override requests argument {}".format(k))
        if password is not None:
            requests_kwargs['auth'] = HTTPBasicAuth(username, password)
            if protocol != 'https':
                raise ValueError("Protocol must be https when passing a password")
        self._requests_kwargs = requests_kwargs
        self._reset_state()

    def _reset_state(self):
        """
        Reset state about the previous query in preparation for running another query
        """
        super(Cursor, self)._reset_state()
        self._nextUri = None
        self._columns = None

    @property
    def description(self):
        """
        This read-only attribute is a sequence of 7-item sequences.
        Each of these sequences contains information describing one result column:

        - name
        - type_code
        - display_size (None in current implementation)
        - internal_size (None in current implementation)
        - precision (None in current implementation)
        - scale (None in current implementation)
        - null_ok (always True in current implementation)

        The ``type_code`` can be interpreted by comparing it to the Type Objects specified in the section below.
        """

        """
        Sleep until we're done or we got the columns
        """
        self._fetch_while(
            lambda: self._columns is None and
                    self._state not in (self._STATE_NONE, self._STATE_FINISHED)
        )
        if self._columns is None:
            return None
        return [
            (col['name'], col['type'], None, None, None, None, True)
            for col in self._columns
        ]

    def execute(self, operation, parameters=None):
        """
        Prepare and execute a database operation (query or command).
        Return values are not defined.
        """
        if self._protocol == 'https':
            if 'adhoc' == self._group:
                self._token = self._get_token(self._username, self._password)
            else:
                self._token = self._password

        headers = {
            'X-Presto-Catalog': self._catalog,
            'X-Presto-Schema': self._schema,
            'X-Presto-Source': self._source,
            'X-Presto-User': self._username,
            "token": self._token,
            "group": self._group
        }
        if self._session_props:
            headers['X-Presto-Session'] = ','.join(
                '{}={}'.format(propname, propval)
                for propname, propval in self._session_props.items()
            )

        """
        Prepare statement
        """
        if parameters is None:
            sql = operation
        else:
            sql = operation % _escaper.escape_args(parameters)

        self._reset_state()
        self._state = self._STATE_RUNNING
        url = urlparse.urlunparse((
            self._protocol,
            '{}:{}'.format(self._host, self._port), '/v1/statement', None, None, None))
        _logger.info('%s', sql)
        _logger.debug("Headers: %s", headers)
        response = self._requests_session.post(
            url, data=sql.encode('utf-8'), headers=headers, **self._requests_kwargs)
        self._process_response(response)

    def cancel(self):
        """
        Cancel the request
        """
        if self._state == self._STATE_NONE:
            raise ProgrammingError("No query yet")
        if self._nextUri is None:
            assert self._state == self._STATE_FINISHED, "Should be finished if nextUri is None"
            return

        response = self._requests_session.delete(self._nextUri, **self._requests_kwargs)
        if response.status_code != requests.codes.no_content:
            fmt = "Unexpected status code after cancel {}\n{}"
            raise OperationalError(fmt.format(response.status_code, response.content))

        self._state = self._STATE_FINISHED
        self._nextUri = None

    def poll(self):
        """
        Poll for and return the raw status data provided by the Presto REST API.
        :returns: dict -- JSON status information or ``None`` if the query is done
        :raises: ``ProgrammingError`` when no query has been started
        :note: This is not a part of DB-API.
        """
        if self._state == self._STATE_NONE:
            raise ProgrammingError("No query yet")
        if self._nextUri is None:
            assert self._state == self._STATE_FINISHED, "Should be finished if nextUri is None"
            return None
        response = self._requests_session.get(self._nextUri, **self._requests_kwargs)
        self._process_response(response)
        return response.json()

    def _fetch_more(self):
        """
        Fetch the next URI and update state
        """
        self._process_response(self._requests_session.get(self._nextUri, **self._requests_kwargs))

    def _decode_binary(self, rows):
        """
        As of Presto 0.69, binary data is returned as the varbinary type in base64 format
        This function decodes base64 data in place
        """
        for i, col in enumerate(self.description):
            if col[1] == 'varbinary':
                for row in rows:
                    if row[i] is not None:
                        row[i] = base64.b64decode(row[i])

    def _process_response(self, response):
        """
        Given the JSON response from Presto's REST API, update the internal state with the next URI and any data from the response
        """
        #TODO handle HTTP 503
        if response.status_code != requests.codes.ok:
            fmt = "Unexpected status code {}\n{}"
            raise OperationalError(fmt.format(response.status_code, response.content))

        response_json = response.json()
        _logger.debug("Got response %s", response_json)
        assert self._state == self._STATE_RUNNING, "Should be running if processing response"
        self._nextUri = response_json.get('nextUri')
        self._columns = response_json.get('columns')
        if 'X-Presto-Clear-Session' in response.headers:
            propname = response.headers['X-Presto-Clear-Session']
            self._session_props.pop(propname, None)
        if 'X-Presto-Set-Session' in response.headers:
            propname, propval = response.headers['X-Presto-Set-Session'].split('=', 1)
            self._session_props[propname] = propval
        if 'data' in response_json:
            assert self._columns
            new_data = response_json['data']
            self._decode_binary(new_data)
            self._data += map(tuple, new_data)
        if 'nextUri' not in response_json:
            self._state = self._STATE_FINISHED
        if 'error' in response_json:
            raise DatabaseError(response_json['error'])

    def _get_token(self, user, password):
        """
        Get the token
        """
        varify_result = self._verify_token(token=self._token)
        if (json.loads(varify_result)['status']):
            return self._token
        login_result = self._login(user, password)
        json_result = json.loads(login_result)
        if (json_result['status']):
            self._token = json_result['token']
        else:
            print("user password err")
        return self._token

    def _verify_token(self, token):
        """
        Verify token via sso
        """
        url = 'http://sso.xxx.com/account/identity'
        values = {'token': token}
        data = urlencode(values).encode('utf-8')
        result = urlopen(url, data)
        code = result.getcode()
        if code != 200:
            fmt = "Unexpected status code after sso login {}\n{}"
            raise OperationalError(fmt.format(result.status_code, result.content))
        return result.read()

    def _login(self, user, password):
        """
        Login via sso
        """
        url = 'http://sso.xxx.com/account/log_in_api'
        params = {}
        params['username'] = user
        params['password'] = password
        params = urlencode(params).encode('utf-8')
        result = urlopen(url, params)
        code = result.getcode()
        if code != 200:
            fmt = "Unexpected status code after sso login {}\n{}"
            raise OperationalError(fmt.format(result.status_code, result.content))
        return result.read()

"""
See types in presto-main/src/main/java/com/facebook/presto/tuple/TupleInfo.java
"""
FIXED_INT_64 = DBAPITypeObject(['bigint'])
VARIABLE_BINARY = DBAPITypeObject(['varchar'])
DOUBLE = DBAPITypeObject(['double'])
BOOLEAN = DBAPITypeObject(['boolean'])
