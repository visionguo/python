#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    get_domain
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
from datetime import datetime
from datetime import date
import datetime
import time
import logging
import ConfigParser
import datetime
import sys
import yaml
import os
from mysql import *
import redis

reload(sys)
sys.setdefaultencoding('utf-8')

"""
获取sre pv现状
"""
get_sre_pv_precent_json={
    "size":0,
    "_source":{
        "excludes":[
        ]
    },
    "aggs":{
        "2":{
            "terms":{
                "field":"@timestamp",
                "size":50000,
                "order":{
                    "1":"desc"
                }
            },
            "aggs":{
                "1":{
                    "avg":{
                        "field":"pv"
                    }
                },
                "3":{
                    "avg":{
                        "field":"Reliability"
                    }
                }
            }
        }
    },
    "stored_fields":[
        "*"
    ],
    "script_fields":{

    },
    "docvalue_fields":[
        "@timestamp"
    ],
    "query":{
        "bool":{
            "must":[
                {
                    "query_string":{
                        "query":"\"api-bi.xxx.com\"",
                        "analyze_wildcard":True,
                        "default_field":"*"
                    }
                },
                {
                    "range":{
                        "@timestamp":{
                            "gte":1541237646756,
                            "lte":1541238546756,
                            "format":"epoch_millis"
                        }
                    }
                }
            ],
            "filter":[

            ],
            "should":[

            ],
            "must_not":[

            ]
        }
    }
}

"""
pre域名
"""
get_domain_pre_json={
    "size":0,
    "_source":{
        "excludes":[
            "xinche_order.xxx.com"
        ]
    },
    "aggs":{
        "2":{
            "terms":{
                "field":"domain",
                "size":500,
                "order":{
                    "_count":"desc"
                }
            }
        }
    },
    "stored_fields":[
        "*"
    ],
    "script_fields":{

    },
    "docvalue_fields":[
        "@timestamp"
    ],
    "query":{
        "bool":{
            "must":[
                {
                    "query_string":{
                        "query":"/g1-sp-proxy-.*/",
                        "analyze_wildcard":True,
                        "default_field":"*"
                    }
                },
                {
                    "range":{
                        "@timestamp":{
                            "gte":1538398426243,
                            "lte":1539003226243,
                            "format":"epoch_millis"
                        }
                    }
                }
            ],
            "filter":[

            ],
            "should":[

            ],
            "must_not":[

            ]
        }
    }
}

"""
计算可用性均值
"""
get_avg_reliability_json={
    "size":0,
    "_source":{
        "excludes":[

        ]
    },
    "aggs":{
        "1":{
            "avg":{
                "field":"Reliability"
            }
        }
    },
    "stored_fields":[
        "*"
    ],
    "script_fields":{

    },
    "docvalue_fields":[
        "@timestamp"
    ],
    "query":{
        "bool":{
            "must":[
                {
                    "query_string":{
                        "query":"\"ws-org.xxx-int.com\"",
                        "analyze_wildcard":True,
                        "default_field":"*"
                    }
                },
                {
                    "range":{
                        "@timestamp":{
                            "gte":1539002256219,
                            "lte":1539007046829,
                            "format":"epoch_millis"
                        }
                    }
                }
            ],
            "filter":[

            ],
            "should":[

            ],
            "must_not":[

            ]
        }
    }
}

def set_redis(k,v):
    """
    建立redis连接
    """
    r = redis.Redis(host='127.0.0.1', port=6379, password='qwer#123$a', decode_responses=True)  # host是redis主机，需要redis服务端和客户端都启动
    r.set(k,v)    # key是"k"，value是"v"，将键值对存入redis缓存
    r.expire(k, 70000)    # 设置k的过期时间，单位为秒

def get_redis(k):
    """
    获取key
    """
    r = redis.Redis(host='127.0.0.1', port=6379,password='qwer#123$a', decode_responses=True)
    return  r.get(k)

def get_blacklist_conflist():
    """
    获取黑名单列表数据
    """
    base_dir = os.path.split(os.path.realpath(__file__))[0]
    global domain_conflist
    global cf2
    cf2 = ConfigParser.ConfigParser()
    cf2.read(base_dir + "/blacklist.ini")

def get_domain_info(domain):
    """
    获取域名信息
    """
    re={}
    for i in domain.split(","):
        sql='select `use_for` from domain where name="'+i+'"'
        r=query_db(sql)
        if r :
            re[i]=r[0][0]
    return json.dumps(re,ensure_ascii=False)

def Connect_es(index,json):
    """
    连接es
    """
    es = Elasticsearch([{"host":"ip","port":9200,"timeout":150}])
    res = es.search(
                index=index,
                body=json,
            )
    return res

def get_blacklist():
    """
    获取黑名单
    """
    base_dir = os.path.split(os.path.realpath(__file__))[0]
    f = open(base_dir + "/blacklistw.yml")
    return yaml.load(f)

def getre(query,proxy_cluster):
    """
    获取
    """
    re1 = query
    re2 = "domain:/.*(domain1.com|domain2|domain3|domain4-int.com).*/"
    if proxy_cluster in get_blacklist():
        re3 = "NOT domain:" + str(get_blacklist()[proxy_cluster]).replace(', ', '|').replace("\'", "\"").replace("[", "/(").replace("]", ")/")
        print re1 + " AND " + re2 + " AND " + re3
        return re1 + " AND " + re2 + " AND " + re3
    else:
        print re1 + " AND " + re2
        return re1 + " AND " + re2

"""
获取pv当前值
"""
def get_sre_pv_precent(index,domain,start,end):
    get_sre_pv_precent_json["query"]["bool"]["must"][1]["range"]["@timestamp"]["gte"] = start
    get_sre_pv_precent_json["query"]["bool"]["must"][1]["range"]["@timestamp"]["lte"] = end
    get_sre_pv_precent_json["query"]["bool"]["must"][0]["query_string"]["query"] = domain
    pvsum = 0
    avi_sum = 0
    avi_detail = []
    try:
        jdata = Connect_es(index,get_sre_pv_precent_json)
        msg_count = jdata["hits"]["total"]
    except Exception as e:
        logging.error(e)

    for i in jdata["aggregations"]["2"]["buckets"]:
        if i["1"]["value"] is None:
            i["1"]["value"] = 0
        pvsum+=i["1"]["value"]

        if i["3"]["value"] is None:
            i["3"]["value"] = 0
        avi_detail.append(i["3"]["value"] )
    for i in jdata["aggregations"]["2"]["buckets"]:
        avi_sum+=i["3"]["value"]*(i["1"]["value"]/(pvsum+0.00000001))
    return avi_sum,pvsum,avi_detail

def get_domain_precent_new(index,query,start,end,timerate,proxy_name):
    """
    获取域名当前百分比
    """
    avi=0
    strings = ['domain', 'reliability', 'rate', 'count', 'allcount','fact']
    info=[]
    proxy_pv_sum=0
    proxy_avi_sum=0
    this_start = long(time.time() * 1000 - 60*72*60*1000)
    this_end = long(time.time() * 1000)
    proxy_raw_info={}
    domain_raw_info = []
    get_domain_pre_json["query"]["bool"]["must"][1]["range"]["@timestamp"]["gte"] = this_start
    get_domain_pre_json["query"]["bool"]["must"][1]["range"]["@timestamp"]["lte"] = this_end
    get_domain_pre_json["query"]["bool"]["must"][0]["query_string"]["query"] = getre(query,proxy_name)
    try:
        jdata = Connect_es(index,get_domain_pre_json)
        msg_count = jdata["hits"]["total"]
    except Exception as e:
        logging.error(e)

    for i in jdata["aggregations"]["2"]["buckets"]:
        if re.search(r"domain1|domain2|domain3", i["key"]) and i["doc_count"]>200 :
            domain_avg_reliability=get_sre_pv_precent("sre*", str(i["key"]), start, end)    # 按pv计算单个域名可用性
        else:
            domain_avg_reliability = get_sre_pv_precent("sre*", str(i["key"]), start, end)
        proxy_raw_info[i["key"]] = domain_avg_reliability
    for i in proxy_raw_info:
        proxy_pv_sum += proxy_raw_info[i][1]
    for i in proxy_raw_info:
        proxy_avi_sum += proxy_raw_info[i][0] * (proxy_raw_info[i][1] /(proxy_pv_sum+0.0000001))
        v = [i, round(proxy_raw_info[i][0], 3), str(round((proxy_raw_info[i][1] / (proxy_pv_sum+0.0000001)) * 100, 2)),str(proxy_raw_info[i][1]), str(proxy_pv_sum),str(round(proxy_raw_info[i][0] * (proxy_raw_info[i][1] / (proxy_pv_sum+0.0000001)  ), 3))]
        d = dict(zip(strings, v))
        info.append(d)
    allinfo=info,round(proxy_avi_sum, 3),query,time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(start/1000)),time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(end/1000))
    print json.dumps(allinfo)
    set_redis("avi_"+proxy_name+"_"+timerate,allinfo)
    return info,round(proxy_avi_sum, 3),query,time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(start/1000)),time.strftime("%/%m/%d %H:%M:%S",time.localtime(end/1000))

"""
时间速率timerate
"""
def get_timerate(timerate):
    if timerate == "n7":
        start = long(time.time() * 1000 - 60 * 24 * 60 * 1000 * 7)
        end = long(time.time() * 1000)
    if timerate == "n14":
        start = long(time.time() * 1000 - 60 * 24 * 60 * 1000 * 14)
        end = long(time.time() * 1000 - 60 * 24 * 60 * 1000 * 7)
    if timerate == "n30":
        start = long(time.mktime(datetime(datetime.today().year,datetime.today().month,1,0,0,0).timetuple()))*1000
        end = long(time.time() * 1000)
    if timerate == "lm":
        print "time"
        print datetime(datetime.today().year,1,1,1,1,1)
        date1 = datetime.now()
        y = date1.year
        m = date1.month
        print y,m
        month_start_dt = date(y, m, 1)
        if m == 1:  # 如果是1月
            start_date = date(y - 1, 12, 1)
        else:
            start_date = date(y, m - 1, 1)
        start =long(time.mktime(start_date.timetuple()))*1000
        end_date = date(y, m, 1) - timedelta(days=1)
        end = long(time.mktime(end_date.timetuple()))*1000
    return start,end

"""
计算环比数据
"""
def get_huanbi(index, query, timerate ,proxy_name):
    if timerate == "n7":
        timerate = "n14"
        time = get_timerate(timerate)
        if get_redis("avi_" + proxy_name + "_" + timerate) is not None:
            return tuple(eval(get_redis("avi_" + proxy_name + "_" + timerate)))
        else:
            return get_domain_precent_new(index, query,  time[0], time[1], timerate, proxy_name)
    if timerate == "n30":
        timerate = "lm"
        time = get_timerate(timerate)
        if get_redis("avi_" + proxy_name + "_" + timerate) is not None:
            return tuple(eval(get_redis("avi_" + proxy_name + "_" + timerate)))
        else:
            return get_domain_precent_new(index, query, time[0], time[1], timerate, proxy_name)

"""
计算环比数据2
"""
def get_huanbi2(index, query, timerate ,proxy_name):
    if timerate == "n7":
        timerate = "n14"
        time = get_timerate(timerate)
        return get_domain_precent_new(index, query,  time[0], time[1], timerate,proxy_name)
    if timerate == "n30":
        timerate = "lm"
        time = get_timerate(timerate)
        return get_domain_precent_new(index, query, time[0], time[1], timerate,proxy_name)

"""
计算所有的域名可用性
"""
def  get_domain_all_reliability(proxy_name,timerate,proxydict):
        time=get_timerate(timerate)
        print time
        index = "nginx-access-*"
        proxy_cluster=proxydict[proxy_name]
        if type(proxy_cluster) is list:
            jionstr=".*/ OR /g1-"
            query=re.sub(r'$', '.*/)', re.sub(r'^', '(/g1-', jionstr.join(proxy_cluster)))
        else:
            query = re.sub(r'$', '.*/)', re.sub(r'^', '(/g1-',proxy_cluster))
        print query
        if get_redis("avi_"+proxy_name+"_"+timerate) is  not None:
            huanbi= get_huanbi(index, query, timerate,proxy_name)
            return tuple(eval(get_redis("avi_"+proxy_name+"_"+timerate))),huanbi
        else:
            huanbi = get_huanbi(index, query,  timerate,proxy_name)
            return get_domain_precent_new(index, query, time[0], time[1], timerate,proxy_name),huanbi

"""
计算所有的域名可用性2
"""
def get_domain_all_reliability_2(proxy_name,timerate,proxydict):
        time=get_timerate(timerate)
        index = "nginx-access-*"
        proxy_cluster=proxydict[proxy_name]
        if type(proxy_cluster) is list:
            jionstr=".*/ OR /g1-"
            query=re.sub(r'$', '.*/)', re.sub(r'^', '(/g1-', jionstr.join(proxy_cluster)))
        else:
            query = re.sub(r'$', '.*/)', re.sub(r'^', '(/g1-',proxy_cluster))
        print query
        huanbi = get_huanbi2(index, query,  timerate,proxy_name)
        return get_domain_precent_new(index, query, time[0], time[1], timerate,proxy_name),huanbi