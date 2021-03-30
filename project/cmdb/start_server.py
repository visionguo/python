#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    start_server
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import os
import argparse
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(BASE_DIR)

try:
    from config import Config as CONFIG
except ImportError:
    print("Can't find the config file")
    exit(1)

ACCESS_LOG = "{}/{}".format(CONFIG.LOG_PATH,CONFIG.ACCESS_LOG_FILE)
ERROR_LOG = "{}/{}".format(CONFIG.LOG_PATH,CONFIG.ERROR_LOG_FILE)
HTTP_HOST = CONFIG.HTTP_BIND_HOST or '127.0.0.1'
HTTP_PORT = CONFIG.HTTP_LISTEN_PORT or '8080'
LOG_FORMAT = CONFIG.LOG_FORMAT
LOG_LEVEL = CONFIG.LOG_LEVEL
WORKERS = CONFIG.WORKERS
DAEMON = CONFIG.DAEMON or True
RUN_DIR = os.path.join(BASE_DIR,'run')

try:
    os.makedirs(CONFIG.LOG_PATH)
    os.makedirs(RUN_DIR)
except:
    pass

def make_migrations():
    print("Check database structure change")
    os.chdir(BASE_DIR)
    subprocess.call('python3 manage.py makemigrations', shell=True)

def make_migrate():
    print("init database")
    os.chdir(BASE_DIR)
    subprocess.call('python3 manage.py migrate', shell=True)

def collect_static():
    print("Collect static files")
    os.chdir(BASE_DIR)
    subprocess.call('python3 manage.py collectstatic --no-input', shell=True)

def prepare():
    make_migrations()
    make_migrate()
    collect_static()

def get_pid_file_path(service):
    return os.path.join(RUN_DIR, '{}.pid'.format(service))

def get_pid(service):
    pid_file = get_pid_file_path(service)
    if os.path.isfile(pid_file):
        with open(pid_file) as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0

def Start():
    print("\n Start CMDB Server")
    prepare()
    service = 'gunicorn'
    bind = '{}:{}'.format(HTTP_HOST,HTTP_PORT)
    pid_file = '{}/{}.pid'.format(RUN_DIR,service)
    start_cmd = "{} lockdown.wsgi:application -b {} -D -p {} --access-logformat '{}' --log-level {}" \
                " --access-logfile {} --error-logfile {} --workers {}".format(service, bind,pid_file,LOG_FORMAT,LOG_LEVEL,ACCESS_LOG,
                                                                 ERROR_LOG, WORKERS)
    os.chdir(BASE_DIR)
    subprocess.call(start_cmd,shell=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""
            Start CMDB service control
            Example: \r\n
            %(prog)s start
        """
    )

    parser.add_argument(
        'action', type=str,
        choices =("start"),
        help = "Start service"
    )

    args = parser.parse_args()
    action =args.action

    if action == "start":
        Start()