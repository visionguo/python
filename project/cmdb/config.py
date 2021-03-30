#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    lockdown
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

"""
lockdown config file
"""

import multiprocessing
import socket

class Config:
    # Django security setting, if your disable debug model, you should setting that
    ALLOWED_HOSTS = ['*']

    # Development env open this, when error occur display the full process track, Production disable it
    DEBUG = False

    # Database settings
    DB_ENGINE = ''
    DB_NAME = ''
    DB_HOST = ''
    DB_PORT = ''
    DB_USER = ''
    DB_PASSWORD = ''

    # LDAP settings
    LDAP_SERVER = ''
    LDAP_BIND_DN = ''
    LDAP_BIND_PASSWORD = ''
    LDAP_SEARCH_OU = ''
    LDAP_SEARCH_FILTER = ''
    LDAP_GROUP_SEARCH_FILTER = ''

    IS_ACTIVE_OU = ''
    IS_STAFF_OU = ''
    IS_SUPERUSER_OU = ''

    # gunicorn setting
    HTTP_BIND_HOST = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    HTTP_LISTEN_PORT = '8080'
    LOG_LEVEL = 'info'
    WORKERS = multiprocessing.cpu_count() * 2 + 1
    DAEMON = True
    LOG_FORMAT = '%(h)s %(l)s %(u)s %(t)s %(m)s  %(U)s %(q)s %(H)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(T)s'
    LOG_PATH = '/data/service_logs/gunicorn'
    ACCESS_LOG_FILE = 'gunicorn_access.log'
    ERROR_LOG_FILE = 'gunicorn_error.log'

    # Fort api
    FortBASE_URL = "http://fort_api_url/fort/api"
    FortDepartQuery = "/sysDepart/query"
    FortDepartAdd = "/sysDepart/add"
    FortAssetQuery = "/sysEquipment/query"
    FortAssetAdd = "/sysEquipment/add"

    fort_data = {
        "appkey": "",
    }