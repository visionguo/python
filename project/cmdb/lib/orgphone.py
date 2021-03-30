#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    orgphone
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import requests
import time
import base64
import hashlib
import hmac
import uuid
from urllib.parse import urlencode, quote_plus

URL = "http://ws-org.xxx-corp.com/staff/getUserInfoByCondition"

ORG_APP_KEY = ""
ORG_APP_SECRET = ''

def signature(payload):
    """
    签名
    """
    sort_tuple = [(k, payload[k]) for k in sorted(payload)]
    urlencoded = urlencode(sort_tuple, quote_via=quote_plus)
    m = hmac.new(ORG_APP_SECRET, urlencoded.encode('utf-8'), hashlib.sha256)
    m = base64.b64encode(m.digest())
    m = hashlib.md5(m).hexdigest()
    return m[5:15]

def getphone(username):
    """
    获取手机号
    """
    payload = {
        'appkey': ORG_APP_KEY,
        'expires': int(time.time()) + 200,
        'nonce': str(uuid.uuid4()),
        'type': 1,
        'condition': username
    }
    sig = signature(payload)
    payload['signature'] = sig

    r = requests.get(URL, params=payload)
    if len(r.json()['data']) != 0:
        phone = r.json()['data'][0]['mobilePhone']
        return phone
    else:
        return 1