#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    getres
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import paramiko
import re

def Connect(hostname,cmd):
    pkey = paramiko.DSSKey.from_private_key_file('/home/vip/.ssh/id_dsa')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=hostname, username='vip', pkey=pkey, timeout=10)
        stdin, stdout, stderr=ssh.exec_command(cmd)
        ret = stdout.readlines()
        ssh.close()
        return ret
    except:
        pass

def GetMem(hostname):
    cmd = 'sudo dmidecode |grep -A16 "Memory Device$"|grep "Size"|grep -v "No"'
    tmp_mem = Connect(hostname,cmd)
    mem_num = len(tmp_mem)
    if mem_num == 0:
        cmd = 'sudo dmesg|grep "Memory"'
        tmp_mem = Connect(hostname,cmd)
        num = len(tmp_mem)
        if num == 0:
            cmd = "cat /proc/meminfo |grep 'MemTotal'|awk '{print $2}'"
            mem = round(int(Connect(hostname,cmd)[0]) / 1024 / 1024)
            final_mem = "{}G*1".format(mem)
            return final_mem
        else:
            mem = round(int(re.split(r'[/k/K]',tmp_mem[0])[2]) / 1024 / 1024)
            final_mem = "{}G*1".format(mem)
            return final_mem
    else:
        size = round(int(re.split(r'[:\s]',tmp_mem[0])[3]) / 1024)
        final_mem = "{}G*{}".format(size,mem_num)
        return final_mem

def GetCpu(hostname):
    cmd = "cat /proc/cpuinfo |grep 'model name'|awk -F ': ' '{print $2}'"
    tmp_cpu = Connect(hostname,cmd)
    cpu_num = len(tmp_cpu)
    cpu = re.split(r'[\s]*',tmp_cpu[0])
    if cpu[4] == "@":
        cpu_model = "{} {} {} {} {} {}".format(cpu[0],cpu[1],cpu[2],cpu[3],cpu[4],cpu[5])
        cpu_ret = "{}*{}".format(cpu_model,cpu_num)
        return cpu_ret
    else:
        cpu_model = "{} {} {} {} {} {} {}".format(cpu[0],cpu[1],cpu[2],cpu[3],cpu[4],cpu[5],cpu[6])
        cpu_ret = "{}*{}".format(cpu_model,cpu_num)
        return cpu_ret

def GetOS(hostname):
    get_kernel_cmd = "uname  -v"
    kernel = Connect(hostname,get_kernel_cmd)[0]
    if "Ubuntu" in kernel:
        cmd = "cat /etc/issue"
        tmp_os = Connect(hostname,cmd)[0]
        os_version = re.split(r'[\s]',tmp_os)
        os = "{} {}".format(os_version[0],os_version[1])
        return os
    else:
        cmd = "cat /etc/redhat-release"
        tmp_os = Connect(hostname,cmd)[0]
        os_version = re.split(r'[\s]',tmp_os)
        if os_version[2] == "release":
            os = "{} {}".format(os_version[0],os_version[3])
        else:
            os = "{} {}".format(os_version[0],os_version[2])
        return os