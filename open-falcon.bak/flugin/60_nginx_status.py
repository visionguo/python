#!/usr/bin/env python
#-*- coding:utf-8 -*-
""" monitor nginx status 60_nginx.py """

import re
import sys
import socket
import time
import traceback
import urllib
import json

NG_STATUS_URI = 'http://127.0.0.1/web-status'

def main():
    """ main function """
    try:
        content1 = urllib.urlopen(NG_STATUS_URI).read()
    except Exception:
        traceback.print_exc()

    get_nginx_connect = re.compile(r"(active connections: )(\d+)", re.I).search(content1).group(2)
    get_nginx_read = re.compile(r"(Reading: )(\d+)", re.M|re.I).search(content1).group(2)
    get_nginx_write = re.compile(r"(Writing: )(\d+)", re.M|re.I).search(content1).group(2)
    get_nginx_wait = re.compile(r"(Waiting: )(\d+)", re.M|re.I).search(content1).group(2)
    get_nginx_accept = re.compile(r"^ (\d+)(.)(\d+)(.)(\d+)", re.M|re.I).search(content1).group(1)
    get_nginx_handle = re.compile(r"^ (\d+)(.)(\d+)(.)(\d+)", re.M|re.I).search(content1).group(3)
    get_nginx_request1 = re.compile(r"^ (\d+)(.)(\d+)(.)(\d+)", re.M|re.I).search(content1).group(5)
    get_nginx_fail = int(get_nginx_accept) - int(get_nginx_handle)

    all_status = {
        'activeing': [get_nginx_connect, 'GAUGE'],
        'reading': [get_nginx_read, 'GAUGE'],
        'writing': [get_nginx_write, 'GAUGE'],
        'waiting': [get_nginx_wait, 'GAUGE'],
        'all_accepts': [get_nginx_accept, 'GAUGE'],
        'all_request': [get_nginx_request1, 'GAUGE'],
        'fail_accepts': [get_nginx_fail, 'GAUGE'],
        'qps': [get_nginx_request1, 'COUNTER'],
    }

    output = []
    for key in all_status:
        t = {}
        t['endpoint'] = socket.gethostname()
        t['timestamp'] = int(time.time())
        t['step'] = 60
        t['counterType'] = all_status[key][1]
        t['metric'] = 'nginx.%s' % key
        t['value'] = all_status[key][0]
        t['tags'] = 'src=nginx'
        output.append(t)
    return output

if __name__ == "__main__":
    if main():
        print json.dumps(main(), indent=3)
    sys.stdout.flush()

