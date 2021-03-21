#!/bin/python
# -*- encoding: utf-8 -*-
""" The script encapsulates simple kibana query syntax """
""" It supports query、count, status code percentage model and domain name average request time model """

import argparse
from elasticsearch import Elasticsearch
import json
import os
import requests
import sys
import time
#from influxdb import InfluxDBClient


def aggs_per_time(size):
    aggs = {
              "5": {
                    "date_histogram": {
                  "field": "@timestamp",
                  "interval": "30s",
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
                                "size": 5,
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

def aggs_per_status(size):
    aggs = {
        "6": {
            "date_histogram": {
                "field": "@timestamp",
                "interval": "30s",
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
                                "size": 5,
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

def query_host():
    """ Query the nginx log for the specified host """
    query =  {
               "match_phrase": {
                   "beat.hostname": {
                       "query": args.host
                   }
              }
        }
    return query

def query_code():
    """ Query the nginx log that specifies the HTTP code """
    query =  {
               "match_phrase": {
                   "status": {
                       "query": args.code
                   }
              }
        }
    return query

def query_domain():
    """ Query the nginx log for the specified domain name """
    query =  {
               "match_phrase": {
                   "domain": {
                       "query": args.domain
                   }
               }
           }
    return query

def query_default():
    """ Query the nginx log for the specified domain name """
    query =  {
               "match_phrase": {
                   "input_type": {
                       "query": "log"
                   }
               }
           }
    return query

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

def Create_json_query(start_time, now_time, size, query):
    """ A template is provided for the query function above """
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
            "aggs": {
                "2": {
                    "date_histogram": {
                        "field": "@timestamp",
                        "interval": "1m",
                        "time_zone": "Asia/Shanghai",
                        "min_doc_count": 1
                    }
                }
            },
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
                    },  query,  {
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
    bak = {
            "version": True,
            "size": args.number,
            "sort": [{
                "@timestamp": {
                    "order": "desc",
                    "unmapped_type": "boolean"
                }
            }],
            "_source": {
                "excludes": []
            },
            "aggs": {
                "2": {
                    "date_histogram": {
                        "field": "@timestamp",
                        "interval": "1m",
                        "time_zone": "Asia/Shanghai",
                        "min_doc_count": 1
                    }
                }
            },
            "stored_fields": ["*"],
            "script_fields": {},
            "docvalue_fields": ["@timestamp"],
            "query": {
                "bool": {
                    "must": [{
                        "query_string": {
                            "query": args.host,
                            "analyze_wildcard": True,
                            "default_field": "*"
                        }
                    }, {
                        "match_phrase": {
                            "beat.hostname": {
                                "query": args.host
                            }
                        }
                    }, {
                        "bool": {
                            "should": [{
                                "match_phrase": {
                                    "beat.hostname": args.host
                                }
                            }, {
                                "match_phrase": {
                                    "beat.hostname": "g1-c2b-proxy-v02"
                                }
                            }],
                            "minimum_should_match": 1
                        }
                    }, {
                        "match_phrase": {
                            "status": {
                                "query": args.code
                            }
                        }
                    }, {
                        "bool": {
                            "should": [{
                                "match_phrase": {
                                    "status": args.code
                                }
                            }, {
                                "match_phrase": {
                                    "status": "203"
                                }
                            }, {
                                "match_phrase": {
                                    "status": "204"
                                }
                            }],
                            "minimum_should_match": 1
                        }
                    },  {
                        "match_phrase": {
                            "domain": {
                                "query": args.domain
                            }
                        }
                    },  {
                        "bool": {
                            "should": [{
                                "match_phrase": {
                                    "domain": args.domain
                                }
                            }, {
                                "match_phrase": {
                                    "domain": "www.maodu.com"
                                }
                            }],
                            "minimum_should_match": 1
                        }
                    }, {
                        "range": {
                            "@timestamp": {
                                "gte": 1521348378258,
                                "lte": 1521351978258,
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

def Create_json_count(start_time, now_time, query):
    """ A template is provided for the query function above """
    json = {
            "query": {
                "bool": {
                    "must": [{
                        "query_string": {
                            "query": args.custom,
                            "analyze_wildcard": True,
                            "default_field": "*"
                        }
                    },  query, {
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
    if args.model == 'count':
        res = es.count(
                    index=args.index+"-*",
                    body=json,
                )
    else:
        res = es.search(
                    index=args.index+"-*",
                    body=json,
                )

    return res

def Connec_db(db_body):
    index = args.index
    db_name = "".join(index.split('-')[:1])
    print db_name

    #client = InfluxDBClient(args.dbname, 8086, args.dbuser, args.dbpassword, db_name)
    #client.write_points(db_body)
    #print client.query('select * from db_name') 



def query_todb(res):
    db_name = 'nginx'
    measurement = 'nginx-access'
    total = res['hits']['total']
    for hit in res['hits']['hits']:
        url = hit['_source']['uri']
        domain = hit['_source']['domain']
        status = hit['_source']['status']
        request_time = hit['_source']['request_time']
        remote_addr = hit['_source']['remote_addr']
        beat_hostname = hit['_source']['beat']['hostname']
        #upstream_response_time = hit['_source']['upstream_response_time']
        print ("total: {0}  hostname: {1:<15}  remote_addr: {2:<15}  status: {3} ({4:<5})  domain: {5}{6} ".format(total, beat_hostname, remote_addr, status, request_time, domain, url ))

def count_todb(res):
    measurement = 'nginx_count'
    print ('Total: %s' % (res['count']))

def aggs_per_status_todb(res):
    measurement = 'domain_status'
    total = res['hits']['total']
    falcon_output = []
    for hit in res['aggregations']['6']['buckets']:
        print hit['key_as_string']
        for domain in hit['3']['buckets']:
            domain_key = domain['key']
            domain_count = domain['doc_count']
            perdomain_count = float(('%.2f ' % (domain_count * 100 / total)))
            for status in domain['5']['buckets']:
                status_key = status['key']
                status_count = status['doc_count']
                perstatus_count =  float(('%.2f ' % (status_count * 100 / domain_count)))
                print ("total: {0}  domain_count: {1:<7} ({2:>7}%)    status_count: {3:^7} ({4:>7}%)      status: {5:<5} domain: {6} ".format(total, domain_count, perdomain_count, status_count, perstatus_count, status_key, domain_key ))
                if args.todb:
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
                    t['endpoint'] = "domain_status"
                    t['timestamp'] = int(time.time())
                    t['step'] = 60
                    t['counterType'] = 'GAUGE'
                    t['metric'] = 'status=%s' % status_key
                    t['value'] = perstatus_count
                    t['tags'] = 'src=%s' % domain_key
                    falcon_output.append(t)
                    
                    #Connec_db(db_body)
    #r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(falcon_output))
    #print r

def aggs_per_time_todb(res):
    """ Domain name with the highest average response time """
    measurement = 'domain_url_time'
    total = res['hits']['total']
    falcon_output = []
    for hit in res['aggregations']['5']['buckets']:
        print hit['key_as_string']
        for domain in hit['3']['buckets']:
            domain_key = domain['key']
            domain_time = ('%.2f' % (domain['1']['value']))
            domain_count = domain['doc_count']
            perdomain_count = float(('%.2f ' % (domain_count * 100 / total)))
            for url in domain['4']['buckets']:
                url_key = url['key']
                url_time = ('%.2f' % (url['1']['value']))
                url_count = url['doc_count']
                perurl_count =  float(('%.2f ' % (url_count * 100 / domain_count)))
                print ("total:{0}   domain_count: {1:<5}({2:>6}s)    url_count: {3:<5}({4:>6}s)   url: {5}{6} ".format(total, domain_count, domain_time, url_count, url_time, domain_key, url_key ))
                if args.todb:
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
                                "perurl_count": perurl_count,
                                "perdomain_count": perdomain_count
                            }
                        }
                    ] 

                    t = {}
                    t['endpoint'] = "test_log"
                    t['timestamp'] = int(time.time())
                    t['step'] = 60
                    t['counterType'] = 'GAUGE'
                    t['metric'] = 'domain=%s' % domain_key
                    t['value'] = domain_time
                    t['tags'] = 'url=%s' % url_key
                    falcon_output.append(t)
                    #Connec_db(db_body)
                   
    #r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(falcon_output))
    #print r

def Query():
    if args.host is not '*':
        query = query_host()
    elif args.code is not '*':
        query = query_code()
    elif args.domain is not '*':
        query = query_domain()
    else:
        query = query_default()
    
    return query
 

def main():
    now_time = int(time.time() * 1000 )
    start_time = int(time.time() * 1000 - args.time * 60000)

    if args.model == 'domain_status':
        print "This is each domain in total domain AND each status in domain status (per) "
        json = Create_json_aggs(start_time, now_time, 0, aggs_per_status(args.number))
        res = Connect_es(json)
        aggs_per_status_todb(res)
    elif args.model == 'domain_requesttime':
        print "This is each domain AND each url  ava request_time (per) "
        json = Create_json_aggs(start_time, now_time, 0, aggs_per_time(args.number))
        res = Connect_es(json)
        aggs_per_time_todb(res)
    elif args.model == 'count':
        json = Create_json_count(start_time, now_time, Query()) 
        res = Connect_es(json)
        count_todb(res)
    else:
        json =  Create_json_query(start_time, now_time, args.number, Query())
        res = Connect_es(json)
        query_todb(res)
    
        
def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    group = parser.add_mutually_exclusive_group()

    parser.add_argument('-i', '--index', help='Input the index name', default='nginx-access')
    parser.add_argument('-m', '--model', help='Input the model name: count|domain_requesttime|domain_status', default='query')
    parser.add_argument('-s', '--custom', help='Input custom search', default='*')
    parser.add_argument('-n', '--number', type=int, help='Quick extraction of log numbers', default=10)
    parser.add_argument('-t', '--time', type=float, choices=[0.1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], help='Quick selected times /m', default=1)

    group.add_argument('-H', '--host', help='Input the host name', default='*')
    group.add_argument('-c', '--code', help='Input the http code', default='*')
    group.add_argument('-d', '--domain', help='Input the domain name', default='*')

    parser.add_argument('--todb', help='Whether or not to enter the influxdb', action="store_true")
    parser.add_argument('--dbname', help='Input influxdb name', default='127.0.0.1')
    parser.add_argument('-u', '--dbuser', help='Input influxdb databases user', default='admin')
    parser.add_argument('-p', '--dbpassword', help='Input db password', default='admin@password')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args =  parse_args()
    main()
