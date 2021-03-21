#!/bin/python
# -*- encoding: utf-8 -*-
""" 取1分钟 N 个域名平均响应时间内排名前N 的域名(扩展：取每个域名的url)"""


import sys
import time
import json
import os
import requests
import argparse
from elasticsearch import Elasticsearch
#from influxdb import InfluxDBClient


def aggs_perurl_time(size):
    aggs = {
        "5": {
            "date_histogram": {
                "field": "@timestamp",
                "interval": "60s",
                "time_zone": "Asia/Shanghai",
                "min_doc_count": 1
            },
            "aggs": {
                "3": {
                    "terms": {
                        "field": "domain",
                        "size": size,
                        "order": {
                            "1": "desc"
                        }
                    },
                    "aggs": {
                        "1": {
                            "avg": {
                                "field": "request_time"
                            }
                        },
                        "4": {
                            "terms": {
                                "field": "uri",
                                "size": 4,
                                "order": {
                                    "1": "desc"
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
                }
            }
        }
    }

    return aggs

def Create_json_aggs(start_time, now_time, size, aggs):
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


def aggs_perurl_time_todb(res):
    """ Domain name with the highest average response time """
    measurement = 'domain_requesttime'
    total = res['hits']['total']
    falcon_domain_time = []
    for hit in res['aggregations']['5']['buckets']:
        #print hit['key_as_string']
        for domain in hit['3']['buckets']:
            domain_key = domain['key']
            domain_time = ('%.2f' % (domain['1']['value']))
            domain_count = domain['doc_count']
            perdomain_count = float(('%.2f ' % (domain_count * 100 / total)))
            t = {}
            t['endpoint'] = "nginx_domain_requesttime"
            t['timestamp'] = int(time.time())
            t['step'] = 60
            t['counterType'] = 'GAUGE'
            t['metric'] = 'request_time'
            t['value'] = domain_time
            t['tags'] = 'domain=%s' % domain_key
            falcon_domain_time.append(t)
            for url in domain['4']['buckets']:
                url_key = url['key']
                url_time = ('%.2f' % (url['1']['value']))
                url_count = url['doc_count']
                perurl_count =  ('%.2f ' % (url_count * 100 / domain_count))
                print ("total:{0}   domain_count: {1:<5}({2:>6}s)    url_count: {3:<5}({4:>6}s)   url: {5}{6} ".format(total, domain_count, domain_time, url_count, url_time, domain_key, url_key ))
                db_body = [
                    {
                        "measurement": measurement,
                        "tags": {
                            "domain": domain_key,
                            "urltime": url_time,
                            "url": url_key
                        },
                        "time": hit['key_as_string'],
                        "fields": {
                            "url_time": url_time,
                            "domain_time": domain_time,
                            "perdomain_count": perdomain_count
                        }
                    }
                ]

                #Connec_db(db_body)
    #print falcon_domain_time
    #print json.dumps(falcon_domain_time, indent=3)
    #r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(falcon_domain_time))
    #print r.text


def main():
    now_time = int(time.time() * 1000 )
    start_time = int(time.time() * 1000 - args.time * 60000)

    print "This is each domain AND each url  ava request_time (per) "
    json = Create_json_aggs(start_time, now_time, 0, aggs_perurl_time(args.number))
    res = Connect_es(json)
    aggs_perurl_time_todb(res)

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
