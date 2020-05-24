#!/usr/bin/env python
#-*- coding:utf-8 -*-
""" Digital collection of graphics : 0=FATAL 2=STOPPED 3=RESTART 5=RUNNING 6=undefined"""

import sys
import socket
import time
import json
import subprocess


def not_empty(self):
    """ for filter del null"""
    return self and self.strip()

def execute_system_commands(cmd):
    """ system command """
    cmd_obj = subprocess.Popen(
        cmd,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    result_tuple = cmd_obj.communicate()
    if result_tuple[1]:
        print result_tuple[1]
        exit()
    return filter(not_empty, result_tuple[0].split('\n'))

def get_value(self):
    """ Digitization """
    fcmd = "supervisorctl  status %s |awk '{print $2}'" % self
    status = 6

    if  "STOPPED" in execute_system_commands(fcmd):
        status = 2
    elif "FATAL" in  execute_system_commands(fcmd):
        status = 0
    else:
        rcmd = "supervisorctl status  %s |grep RUNNING |awk -F'uptime' '{print $2}'|awk -F'[ :]' '{print $2$(NF-2)$(NF-1)$(NF)}'" % self
        run_time = ''.join(execute_system_commands(rcmd))
        if int(run_time) > 500:
            status = 5
        else:
            status = 3
    return status

def main():
    """ main function """

    output = []
    cmd = "/bin/supervisorctl status|awk '{print $1}'"
    for program in  execute_system_commands(cmd):
        t = {}
        t['endpoint'] = socket.gethostname()
        t['timestamp'] = int(time.time())
        t['step'] = 60
        t['counterType'] = "GAUGE"
        t['metric'] = 'supervisor'
        t['value'] = get_value(program)
        t['tags'] = 'program=%s' % program
        output.append(t)
    return output

if __name__ == "__main__":
    if  main():
        print json.dumps(main(), indent=3)
    sys.stdout.flush()

