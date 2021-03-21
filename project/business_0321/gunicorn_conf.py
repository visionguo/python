# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    gunicorn_conf
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

bind = '0.0.0.0:5000'
backlog = 20

workers = 3
worker_class = 'sync'
worker_connections = 1000
timeout = 300000
keepalive = 2

spew = False
pidfile = 'logs/gunicorn.pid'
accesslog = '-'
errorlog = '-'
loglevel = 'info'
access_log_format = '%(h)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s %(L)ss'

proc_name = 'cmdb'
