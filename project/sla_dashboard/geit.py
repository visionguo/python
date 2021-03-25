#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    geit
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import requests
import json
from elasticsearch import Elasticsearch
from urllib import urlencode
from urllib import quote
import re
import shutil
import time
import logging
import ConfigParser
import datetime
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

def get_subbusiness_mem_all(business):
    """
    获取子产品线所有内存
    """
    result=[]
    api="http://p8s.xxx-int.com/api/v1/query?query="    # 从p8s源获取监控数据
    query="sum by (business,subbusiness) (node_memory_MemTotal_bytes  {business=~\""+str(business)+"\"})"    # 内存求和
    respose = requests.get(api+query)
    return respose.json()

def get_subbusiness_mem_maxuse(business,subbusiness):
    """
    获取子产品线内存最大值
    """
    result=[]
    print subbusiness
    api="http://p8s.xxx-intp.com/api/v1/query?query="    # 从p8s源获取监控数据
    query="sum by (business,subbusiness) (node_memory_MemTotal_bytes  {business=~\""+str(business)+"\",subbusiness=~\""+subbusiness+"\"}) - sum by (business,subbusiness) (min_over_time(node_memory_MemAvailable_bytes {business=~\""+str(business)+"\",subbusiness=~\""+subbusiness+"\"} [30d]) )"    # 使用promsql获取最大值
    respose = requests.get(api+query)
    return respose.json()

def get_subbusiness_mem_prentuse(business):
    """
    获取子产品线内存使用率现状
    """
    result=[]
    api="http://p8s.xxx-int.com/api/v1/query?query="
    query="(sum by (business,subbusiness) (node_memory_MemTotal_bytes  {business=~\""+str(business)+"\"}) - sum by (business,subbusiness) (min_over_time(node_memory_MemAvailable_bytes {business=~\""+str(business)+"\"} [30d]) )) *100 / sum by (business,subbusiness) (node_memory_MemTotal_bytes  {business=~\""+str(business)+"\"})"
    respose = requests.get(api+query)
    return respose.json()

def get_subbusiness_cpu_max_prentuse(business):
    """
    获取cpu当前最大值
    """
    result=[]
    api="http://p8s.xxx-int.com/api/v1/query_range?query="
    query="avg by (business,subbusiness)( irate  (node_cpu_seconds_total {business=~\""+str(business)+"\",mode=\"idle\"}[30m] )  )"
    timerange="&start=2018-10-02T20:10:30.781Z&end=2018-10-09T20:11:00.781Z&step=30m"
    respose = requests.get(api+query+timerange)
    for r in respose.json()["data"]["result"]:
        print r["metric"]["subbusiness"],float(min(r["values"], key=lambda a: a[1])[1])*100
    return respose.json()

print "prent_use-----"
a=get_subbusiness_cpu_max_prentuse(str(b))