#!/bin/python
# -*- encoding: utf-8 -*-
""" 取一分钟的请求较多的 N 个域名的五个状态码，每个状态码占域名百分比 """


import sys
import time
import json
import os
import requests
import argparse
from elasticsearch import Elasticsearch
from influxdb import InfluxDBClient




def aggs_per_status(size):
    aggs = {
        "6": {
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
                            "_count": "desc"
                        }
                    },
                    "aggs": {
                        "5": {
                            "terms": {
                                "field": "status",
                                "size": 3,
                                "order": {
                                    "_count": "desc"
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
                "must_not": []
            }
        }
    }

    return json



def Connect_es(json):
    #url = "http://10.16.8.240:9200/nginx-acces-2018-03-18/_search"
    #r = requests.post(url, data=json, headers=headers)
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



def aggs_per_status_todb(res):
    measurement = 'domain_status'
    total = res['hits']['total']
    falcon_domain_status = []
    for hit in res['aggregations']['6']['buckets']:
        print hit['key_as_string']
        for domain in hit['3']['buckets']:
            domain_key = domain['key']
            domain_count = domain['doc_count']
            perdomain_count = ('%.2f ' % (domain_count * 100 / total))
            for status in domain['5']['buckets']:
                status_key = status['key']
                status_count = status['doc_count']
                perstatus_count =  float(('%.2f ' % (status_count * 100 / domain_count)))
                print ("total: {0}  domain_count: {1:<7} ({2:>7}%)    status_count: {3:^7} ({4:>7}%)      status: {5:<5} domain: {6} ".format(total, domain_count, perdomain_count, status_count, perstatus_count, status_key, domain_key ))
                db_body = [
                    {
                        "measurement": measurement,
                        "tags": {
                            "domain": domain_key,
                            "status": status_key
                        },
                        "time": hit['key_as_string'],
                        "fields": {
                            "perstatus": perstatus_count,
                            "perdomain": perdomain_count
                        }
                    }
                ]

                t = {}
                t['endpoint'] = "domain_status_test"
                t['timestamp'] = int(time.time())
                t['step'] = 60
                t['counterType'] = 'GAUGE'
                t['metric'] = 'status.%s' % status_key
                t['value'] = perstatus_count
                t['tags'] = 'domain=%s' % domain_key
                falcon_domain_status.append(t)

                Connec_db(db_body)
    print json.dumps(falcon_domain_status, indent=3)
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(falcon_domain_status))
    print r.text


def main():
    now_time = int(time.time() * 1000 )
    start_time = int(time.time() * 1000 - args.time * 60000)

    
    json = Create_json_aggs(start_time, now_time, 0, aggs_per_status(args.number))
    res = Connect_es(json)
    aggs_per_status_todb(res)
   

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
