#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    cron
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from lib.getres import GetCpu,GetMem
from .models import Asset

def UpdateRes:
    """
    更新结果
    """
    hosts = Asset.objects.exclude(platform='Windows')
    for host in hosts:
        hostname = host.hostname
        mem = GetMem(hostname)
        cpu = GetCpu(hostname)
        update_host = Asset.objects.get(hostname=hostname)
        update_host.update(mem=mem,cpu=cpu)