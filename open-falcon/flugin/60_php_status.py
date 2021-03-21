#!/usr/bin/env python
#-*- coding:utf-8 -*-
""" monitor php status 60_php.py """

import re
import sys
import socket
import time
import json
from urlparse import urlparse as parse_url
from FastCGIClient import *

URL = "http://127.0.0.1:9001/php-status"

def get_status():
    """ get php_status """
    parseResult = parse_url(URL)
    host = parseResult.hostname
    port = parseResult.port
    uri = parseResult.path
    query = parseResult.query
    client = FastCGIClient(host, port, 3000, 0)
    params = {'GATEWAY_INTERFACE': 'FastCGI/1.0',
              'REQUEST_METHOD': 'POST',
              'SCRIPT_FILENAME': uri,
              'SCRIPT_NAME': uri,
              'QUERY_STRING': query,
              'REQUEST_URI': uri,
              'SERVER_SOFTWARE': 'php/fcgiclient',
              'REMOTE_ADDR': '127.0.0.1',
              'REMOTE_PORT': '9985',
              'SERVER_ADDR': '127.0.0.1',
              'SERVER_PORT': '80',
              'SERVER_NAME': "localhost",
              'SERVER_PROTOCOL': 'HTTP/1.1',
              'CONTENT_TYPE': 'application/x-www-form-urlencoded',
             }
    return client.request(params)

def status_key():
    """ get php_status key """

    content = get_status()
    accepted_conn = re.compile(r"(accepted conn:\s+)(\d+)", re.M|re.I).search(content).group(2)
    max_children = re.compile(r"(max children reached:\s+)(\d+)", re.M|re.I).search(content).group(2)
    slow_request = re.compile(r"(slow requests:\s+)(\d+)", re.M|re.I).search(content).group(2)
    restart_time = re.compile(r"(start since:\s+)(\d+)", re.M|re.I).search(content).group(2)
    listen_queue = re.compile(r"(listen queue:\s+)(\d+)", re.M|re.I).search(content).group(2)
    listen_queue_max = re.compile(r"(max listen queue:\s+)(\d+)", re.M|re.I).search(content).group(2)
    process_idle = re.compile(r"(idle processes:\s+)(\d+)", re.M|re.I).search(content).group(2)
    process_active = re.compile(r"(active processes:\s+)(\d+)", re.M|re.I).search(content).group(2)
    process_active_max = re.compile(r"(max active processes:\s+)(\d+)", re.M|re.I).search(content).group(2)

    all_status = {
        'accepted_conn':    [accepted_conn, 'GAUGE'],
        'slow_request':     [slow_request, 'GAUGE'],
        'restart_time':     [restart_time, 'GAUGE'],
        'listen_queue':     [listen_queue, 'GAUGE'],
        'listen_queue_max': [listen_queue_max, 'GAUGE'],
        'process_idle':     [process_idle, 'GAUGE'],
        'process_active':   [process_active, 'GAUGE'],
        'process_active_max': [process_active_max, 'GAUGE'],
        'max_children_reached': [max_children, 'GAUGE'],
    }

    output = []
    for key in all_status:
        t = {}
        t['endpoint'] = socket.gethostname()
        t['timestamp'] = int(time.time())
        t['step'] = 60
        t['counterType'] = all_status[key][1]
        t['metric'] = 'php.%s' % key
        t['value'] = all_status[key][0]
        t['tags'] = 'src=php'
        output.append(t)
    return output


if __name__ == '__main__':
    if status_key():
        print json.dumps(status_key(), indent=3)
    sys.stdout.flush()

```
"""
参数详解
"""

# 参数
# curl http://www.ttlsa.com/status
pool:                 www
process manager:      dynamic
start time:           14/May/2014:22:40:15 +0800
start since:          58508
accepted conn:        33
listen queue:         0
max listen queue:     8
listen queue len:     0
idle processes:       2
active processes:     1
total processes:      3
max active processes: 5
max children reached: 0
slow requests:        2091

# 解释
pool – fpm池子名称，大多数为www
process manager – 进程管理方式,值：static, dynamic or ondemand. dynamic
start time – 启动日期,如果reload了php-fpm，时间会更新
start since – 运行时长
accepted conn – 当前池子接受的请求数
listen queue – 请求等待队列，如果这个值不为0，那么要增加FPM的进程数量
max listen queue – 请求等待队列最高的数量
listen queue len – socket等待队列长度
idle processes – 空闲进程数量
active processes – 活跃进程数量
total processes – 总进程数量
max active processes – 最大的活跃进程数量（FPM启动开始算）
max children reached - 大道进程最大数量限制的次数，如果这个数量不为0，那说明你的最大进程数量太小了，请改大一点。
slow requests – 启用了php-fpm slow-log，缓慢请求的数量
```