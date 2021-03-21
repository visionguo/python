#!/bin/env python
# -*- coding:utf-8 -*-
########################################################################
##  Loaded=类加载数量  Bytes=所占空间大小   Time=所用时间
##  E=年轻代伊甸园内存占比  O=old代内存占比  M=元数据区内存占用比
##  YGC=年轻代gc次数   YGCT=年轻代gc所用时间  FG=老年代gc次数  FGCT=老年代gc所用时间  GCT=垃圾回收消耗的总时间
########################################################################

import json
import socket
import subprocess
import sys
import time


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
        exit()
    return filter(not_empty, result_tuple[0].split('\n'))


def get_project_name(pid):
    """ get project_name """
    try:
        opt = open('/proc/' + pid +'/cmdline').readline()
    except IOError:
        print "Error: 没有找到PID文件"
        project_name = None
    else:
        opt_list = opt.split('-')
        for i in range(len(opt_list)):
            if opt_list[i].startswith('DprojectName'):
                project_name = opt_list[i].split('=')[1].strip('\x00')
    return project_name

def get_gcstat(pid):
    """ get jstat gc """
    fcmd = "/bin/jstat -gcutil %s" % pid
    gcstat = execute_system_commands(fcmd)
    ## str convert float/int
    gcstat_name = gcstat[0].split()[2:11]
    gcstat_value = map(float, gcstat[1].split())[2:11]
    ## two list convert dicts
    dicts = dict(zip(gcstat_name, gcstat_value))
    return dicts

def get_class(pid):
    fcmd = "/bin/jstat -class %s" % pid
    classstat = execute_system_commands(fcmd)
    classstat_name  = classstat[0].split()
    classstat_value = map(float, classstat[1].split())
    del classstat_name[3]
    del classstat_value[3]
    dicts = dict(zip(classstat_name, classstat_value))
    return dicts

def get_pid():
    """ get pid """
    cmd = "pgrep -f DprojectName"
    pids = execute_system_commands(cmd)
    return pids

def main():
    output = []
    for pid in get_pid():
        project_name = get_project_name(pid)
        if not project_name:
            continue

        dicts = dict(get_class(pid).items() + get_gcstat(pid).items())
        for key in dicts.keys():
            t = {}
            t['endpoint'] = socket.gethostname()
            t['timestamp'] = int(time.time())
            t['step'] = 60
            t['counterType'] = 'GAUGE'
            t['metric'] = 'jvm.%s' % key.lower()
            t['value']= dicts[key]
            t['tags'] = 'project_name=%s,src=java' % project_name
            output.append(t)

    if output:
        print json.dumps(output)

if __name__ == "__main__":
    main()
    sys.stdout.flush()
