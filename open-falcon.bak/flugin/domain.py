#!/usr/bin/env python
# -*- encoding: utf-8 -*-

""" 1、服务于sre大范围监控颗粒度到域名 """
""" 2、收集：一分钟 域名平均响应时间, 目前按请求数量的大小 """
""" 3、收集：一分钟 域名 2xx 3xx 4xx 5xx 状态码数量百分比，目前按请求数量大小排序"""
""" 4、报警：通过open-falcon制定 """
""" 5、可通过 -n 指定数量采集多少域名 ；-s 加参数 模拟 kibana 指定条件过滤"""


""" 不足一：无法方便的指定输出内容 """
""" 不足二：无法更快捷的添加监控，还需要手动在open-falcon添加 """

import sys
import time
import json
import os
import requests
import argparse
from elasticsearch import Elasticsearch


def size_domain():
    dir_path = "/data/shell_files/domain/"
    files = os.listdir(dir_path)
    size_domain = 0
    for file in files:
        if not os.path.isdir(file):
            num = len(open(dir_path+file).readlines())
            size_domain = num + size_domain
    return size_domain

def should_domain():
    dir_path = "/data/shell_files/domain/"
    files = os.listdir(dir_path)
    should_domain = []
    for file in files:
        if not os.path.isdir(file):
            for line in open(dir_path+file).readlines():
                t1 = {}
                t2 = {}
                t1["domain"] = line.strip()
                t2["match_phrase"] = t1
                should_domain.append(t2)
    return should_domain

def aggs_domain_status(size):
    aggs =  {
        "3": {
            "terms": {
                "field": "domain",
                "size": int(size_domain()),
                "order": {
                    "_count": "desc"
                }
            },
            "aggs": {
                "5": {
                    "terms": {
                        "field": "status",
                        "size": 200,
                        "order": {
                            "_count": "desc"
                        }
                    }
                }
            }
        }
    }

    return aggs

def aggs_domain_time(size):
    aggs = {
        "3": {
            "terms": {
                "field": "domain",
                "size": int(size_domain()),
                "order": {
                    "_count": "desc"
                }
            },
            "aggs": {
                "1": {
                    "avg": {
                        "field": "request_time"
                    }
                }
            }
        }
    }

    return aggs

def Create_json_aggs(start_time, now_time, size, aggs, should_domain):
    """ Replace kibana with simple command lines """
    json = {
        "version": True,
        "size": size,
        "sort": [{
            "@timestamp": {
                "order": "desc",
                "unmapped_type": "boolean"
            }
        }],
        "_source": {
            "excludes": []
        },
        "aggs": aggs ,
        "stored_fields": ["*"],
        "script_fields": {},
        "docvalue_fields": ["@timestamp"],
        "query": {
            "bool": {
                "must": [{
                    "query_string": {
                        "query": args.custom,
                        "analyze_wildcard": True,
                        "default_field": "*"
                    }
                }, {
                    "bool": {
                        "should": should_domain ,
                        "minimum_should_match": 1
                    }
                }, {
                    "range": {
                        "@timestamp": {
                            "gte": start_time,
                            "lte": now_time,
                            "format": "epoch_millis"
                        }
                    }
                }],
                "filter": [],
                "should": [],
                "must_not": [{
                    "bool": {
                        "should": [{
                            "match_phrase": {
                                "uri": "//pigeon-gate-websocket/websocket/connect"
                            }
                        }],
                        "minimum_should_match": 1
                    }
                    }, {
                    "bool": {
                        "should": [{
                            "match_phrase": {
                               "domain": "sta.guazistatic.com"
                            }
                        }],
                        "minimum_should_match": 1
                    }
                }]
            }
        }
    }

    return json


def Connect_es(json):
    es    = Elasticsearch([{"host":"10.16.8.240","port":9200,"timeout":150}])
    res = es.search(
            index=args.index+"-*",
            body=json,
        )

    return res

def Connec_db(db_body):
    index = args.index
    db_name = "".join(index.split('-')[:1])

    #client = InfluxDBClient(args.dbname, 8086, args.dbuser, args.dbpassword, db_name)
    #client.write_points(db_body)
    #print client.query('select * from db_name')


def aggs_domain_status_filter(res):
    total = res['hits']['total']
    falcon_status = []
    for domain in res['aggregations']['3']['buckets']:
        domain_key = domain['key']
        domain_count = domain['doc_count']
        perdomain_count = ('%.2f ' % (domain_count * 100 / total))
        correct_count, domain_2xx, domain_3xx, domain_4xx, domain_5xx = 0, 0, 0, 0, 0
        if domain_count > 50:
            for status in domain['5']['buckets']:
                status_key = status['key']
                status_count = status['doc_count']
                if status_key < 300:
                    domain_2xx = domain_2xx + status_count
                elif status_key < 400 and status_key > 299:
                    domain_3xx = domain_3xx + status_count
                elif status_key < 500 and status_key > 399:
                    domain_4xx = domain_4xx + status_count
                else:
                    domain_5xx = domain_5xx + status_count

                if status_key < 405 :
                    correct_count = correct_count + status_count

            perdomain_2xx  =  float(('%.2f ' % (domain_2xx * 100 / domain_count)))
            perdomain_3xx  =  float(('%.2f ' % (domain_3xx * 100 / domain_count)))
            perdomain_4xx  =  float(('%.2f ' % (domain_4xx * 100 / domain_count)))
            perdomain_5xx  =  float(('%.2f ' % (domain_5xx * 100 / domain_count)))
            perdomain_ava   =  float(('%.2f ' % (correct_count * 100 / domain_count)))
            #print ("total: {0}  domain_count: {1:<8} ({2:>6}%)  status: ({3:<6}% {4:<4}% {5:<3}% {6}% {7}%) domain: {8} ".format(total, domain_count, perdomain_count, perdomain_2xx, perdomain_3xx, perdomain_4xx, perdomain_5xx, perdomain_ava, domain_key ))
            t = {}
            t['endpoint'] = "sre-job-v01-domain"
            t['timestamp'] = int(time.time())
            t['step'] = 60
            t['counterType'] = 'GAUGE'
            t['metric'] = 'perdomain_ava'
            t['value'] = perdomain_ava
            t['tags'] = 'domain=%s' % domain_key
            falcon_status.append(t)
            t = {}
            t['endpoint'] = "sre-job-v01-domain"
            t['timestamp'] = int(time.time())
            t['step'] = 60
            t['counterType'] = 'GAUGE'
            t['metric'] = 'perdomain_2xx'
            t['value'] = perdomain_2xx
            t['tags'] = 'domain=%s' % domain_key
            falcon_status.append(t)
            t = {}
            t['endpoint'] = "sre-job-v01-domain"
            t['timestamp'] = int(time.time())
            t['step'] = 60
            t['counterType'] = 'GAUGE'
            t['metric'] = 'perdomain_3xx'
            t['value'] = perdomain_3xx
            t['tags'] = 'domain=%s' % domain_key
            falcon_status.append(t)
            t = {}
            t['endpoint'] = "sre-job-v01-domain"
            t['timestamp'] = int(time.time())
            t['step'] = 60
            t['counterType'] = 'GAUGE'
            t['metric'] = 'perdomain_4xx'
            t['value'] = perdomain_4xx
            t['tags'] = 'domain=%s' % domain_key
            falcon_status.append(t)
            t = {}
            t['endpoint'] = "sre-job-v01-domain"
            t['timestamp'] = int(time.time())
            t['step'] = 60
            t['counterType'] = 'GAUGE'
            t['metric'] = 'perdomain_5xx'
            t['value'] = perdomain_5xx
            t['tags'] = 'domain=%s' % domain_key
            falcon_status.append(t)
        else:
           break
    #print json.dumps(falcon_status, indent=3)
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(falcon_status))
    print r.text
    #print falcon_status

def aggs_domain_time_filter(res):
    total = res['hits']['total']
    falcon_time = []
    t = {}
    t['endpoint'] = "sre-job-v01-domain"
    t['timestamp'] = int(time.time())
    t['step'] = 60
    t['counterType'] = 'GAUGE'
    t['metric'] = 'total_count'
    t['value'] = total
    falcon_time.append(t)
    for domain in res['aggregations']['3']['buckets']:
        domain_key = domain['key']
        domain_time = ('%.2f' % (domain['1']['value']))
        domain_count = domain['doc_count']
        t = {}
        t['endpoint'] = "sre-job-v01-domain"
        t['timestamp'] = int(time.time())
        t['step'] = 60
        t['counterType'] = 'GAUGE'
        t['metric'] = 'domain_count'
        t['value'] = domain_count
        t['tags'] = 'domain=%s' % domain_key
        falcon_time.append(t)
        t = {}
        t['endpoint'] = "sre-job-v01-domain"
        t['timestamp'] = int(time.time())
        t['step'] = 60
        t['counterType'] = 'GAUGE'
        t['metric'] = 'domain_time'
        t['value'] = domain_time
        t['tags'] = 'domain=%s' % domain_key
        falcon_time.append(t)
        #print ("total: {0:<5}  domain_count: {1:<8} ({2:>6}%) ({3:>5}s)  domain: {4}".format(total, domain_count, perdomain_count, domain_time, domain_key))
    #print json.dumps(falcon_time, indent=3)
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(falcon_time))
    print r.text
    #print falcon_time

def main():
    now_time = int(time.time() * 1000 )
    start_time = int(time.time() * 1000 - args.time * 60000)


    json = Create_json_aggs(start_time, now_time, 0, aggs_domain_time(args.number), should_domain())
    res = Connect_es(json)
    aggs_domain_time_filter(res)

    json = Create_json_aggs(start_time, now_time, 0, aggs_domain_status(args.number), should_domain())
    res = Connect_es(json)
    aggs_domain_status_filter(res)

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-i', '--index', help='Input the index name', default='nginx-access')
    parser.add_argument('-m', '--model', help='Input the model name', default='query')
    parser.add_argument('-s', '--custom', help='Input custom search', default='*')
    parser.add_argument('-n', '--number', type=int, help='Quick extraction of log numbers', default=10)
    parser.add_argument('-t', '--time', type=float, choices=[0.1,0,1,2,3,4,5,6,7,8,9], help='Quick selected times /m', default=1)

    parser.add_argument('--todb', help='Whether or not to enter the influxdb', action="store_true")
    parser.add_argument('--dbname', help='Input influxdb name', default='127.0.0.1')
    parser.add_argument('-u', '--dbuser', help='Input influxdb databases user', default='nginx')
    parser.add_argument('-p', '--dbpassword', help='Input db password', default='nginx@password')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args =  parse_args()
    main()
