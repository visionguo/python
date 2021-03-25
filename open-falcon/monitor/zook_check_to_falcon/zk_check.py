#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/14
# Brief:
#    zk_check
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import re
import time
import logging
import json
import requests
import ConfigParser
import commands
import datetime
import sys
import os
import kazoo
from kazoo.exceptions import ConnectionLossException
from kazoo.exceptions import *
from kazoo.retry import KazooRetry
from kazoo.client import KazooClient
from elasticsearch import Elasticsearch
import etcd3
import etcd3.members
import dns.resolver

"""
open-falcon 结构体
"""
falcon_json={
    "endpoint":"g1-c2b-pre-v03",
    "timestamp":1528944550,
    "metric":"load.cpu",
    "value":0.01,
    "counterType":"GAUGE",
    "step":60,
}

def check_dns():
    """
    check dns
    """
    new_dict = {}    # 定义一个新字典
    with open('dns.ini', 'r') as f:    # 打开dns.ini文件
        lines = f.readline()    # 读取第一行
        print lines
        try:
            a = dns.resolver.query(lines,'A')    # dns解析
            print a
            for i in dict:
                print i
                new_dict["domain"] = "dns"
                new_dict["Reliability"] = dict[i]
                new_dict["@timestamp"] = datetime.datetime.utcnow()
                new_dict["type"] = "sre_Reliability"
                new_dict["pv"] = 1
                insert_es("doc", "sre-" + datetime.datetime.now().strftime("%Y-%m"), new_dict)
        except Exception, e:
            print "dns resolver error:" + str(e)
            pass

def get_domain_conflist():
    """
    获取冲突域名cf
    """
    base_dir = os.path.split(os.path.realpath(__file__))[0]
    global domain_conflist
    global cf
    cf = ConfigParser.ConfigParser()    # 使配置文件生效
    cf.read(base_dir + "/zk-conf.ini")

def put_command(cmd):
    """
    put command
    """
    a, b = commands.getstatusoutput(cmd)  # print b
    return a, b

def format_result(rlist, split):
    """
    格式化输出
    """
    new_dict = {}
    while '' in rlist:    # 去除list的空值
        rlist.remove('')
    for i in rlist:    # list转换为字典
        l = i.split(split)
        new_dict[l[0]] = l[1].strip()    # strip：去除首尾空格
    return new_dict

def put_falcon(re):
    """
    输出到falcon接口
    """
    print re
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(re))    # json结构体push到falcon接口，即可使该metric策略生效
    print r

def conn_zk_create(zklist,k,v):
    """"
    create a client and start it
    """
    try:
        zk = KazooClient(hosts=zklist, timeout=0.5)    # create a client
        zk.start()    # 启动客户端
        if not zk.exists(k):
            zk.create(k,v)
    except Exception as e:
        pass

def conn_zk_get(zklist,k):
    """
    连接zk并获取数据
    """
    try:
        zk = KazooClient(hosts=zklist, timeout=0.5)
        zk.start()
        data, stat = zk.get(k)
        return data,stat
    except Exception:
        pass
        return None,None

def ckeck_zkcluster_stat():
    """
    监控zk集群运行状态
    """
    dict = {}
    for i in cf.sections():   # 分集群检查
        avi=0
        zk_list = cf.get(i, "zklist").split(",")
        print zk_list
    # 检查zk状态
        conn_zk_create(zk_list,"/check_zk", "ok")
        if conn_zk_get(zk_list,"/check_zk")[0] is not None:
            avi=100
        else:
            avi=0
        print avi
        dict[i]=avi
    print dict
    return dict

def put_sre_zk_avi(dict):
    """
    写入es
    """
    new_dict={}
    for i in dict:
        print i
        new_dict["domain"]=i
        new_dict["Reliability"] = dict[i]
        new_dict["@timestamp"] = datetime.datetime.utcnow()
        new_dict["type"] = "sre_Reliability"
        new_dict["pv"] = 1
        insert_es("doc", "sre-" + datetime.datetime.now().strftime("%Y-%m"), new_dict)

def insert_es(doc_type, index, json):
    """
    插入es数据
    """
    es = Elasticsearch([{"host": "es_ip", "port": 9200, "timeout": 150}])
    res = es.index(
        doc_type=doc_type,
        index=index,
        body=json,
    )
    return res

# check_dns()time.sleep(20)
get_domain_conflist()
zk_env = cf.sections()

# print zk_env
for i in cf.sections():
  result = {}
  zk_list = cf.get(i, "zklist").split(",")
  for zk_node in zk_list:
    """
    ruok
    """
    result_ruok = {}
    try:
        cmd_ruok = 'echo ruok | nc -w 2 ' + zk_node.split(":")[0] + ' 2181'
        if put_command(cmd_ruok)[1] == "imok":
            result_ruok["zk_status"] = 1
        else:
            result_ruok["zk_status"] = 0
    except:
        print    "ruok  error!"

    """
    srvr
    """
    result_srvr = {}
    try:
        cmd_srvr = 'echo srvr | nc -w 2 ' + zk_node.split(":")[0] + ' 2181'    # 通过nc探测连通性
        result_list_srvr = put_command(cmd_srvr)[1].split('\n')
        result_srvr = format_result(result_list_srvr, ':')
        del result_srvr["Zookeeper version"], result_srvr["Latency min/avg/max"], result_srvr["Zxid"]
    except:
        print "srvr error!"

    """
    wchs
    """
    result_wchs = {}
    try:
        cmd_wchs = 'echo wchs | nc -w 2 ' + zk_node.split(":")[0] + ' 2181'
        result_list_wchs = put_command(cmd_wchs)[1].split('\n')
        result_wchs = format_result(result_list_wchs[1:], ':')
    except:
        print "wchs error!"

    """
    mntr
    """
    result_mntr = {}
    try:
        cmd_mntr = 'echo mntr | nc -w 2 ' + zk_node.split(":")[0] + ' 2181'
        result_list_mntr = put_command(cmd_mntr)[1].split('\n')
        result_mntr = format_result(result_list_mntr, '\t')
        del result_mntr["zk_version"], result_mntr["zk_max_file_descriptor_count"]
    except:
        print "mntr error!"

    # 合并结果
    result.update(result_srvr)
    result.update(result_wchs)
    result.update(result_ruok)
    result.update(result_mntr)
    ts = int(time.time())
    for p in result:
        falcon_json["endpoint"]=zk_node
        falcon_json["metric"]=p
        falcon_json["value"] = result[p]
        falcon_json["timestamp"] = ts
        l=[]
        l.append(falcon_json)
        put_falcon(l)

put_sre_zk_avi(ckeck_zkcluster_stat())