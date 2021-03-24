#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    domain
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

global alert_msg
global mailto
global alert_value_status
global alert_value_reqstime_avi
global wechat_to_group
global mail_to_group

domain_conut = 500    # 采集最近500个域名
interval_time = 2    # 单位:分钟，表示统计2分钟内的数据
base_pvconut = 50    # 表示计算周期内的数据pv，大于该值会被做计算，小于不做处理
good_resquestime = 2    # 单位：秒，大于该值的返回时间被定义为错误状态
alert_pv_diff_rate=70    # pv掉量超过70%
err_stat = '499,500,502,503,504'    # 错误状态码
alert_msg = []    # 报警信息

contact = 'op1,op1@xxx.com,op2,op2@xxx.com'    # 报警接收人

reload(sys)
sys.setdefaultencoding('utf-8')

json_domain_ava = {
    "size": 0,
    "_source": {
        "excludes": [
        ]
    },
    "aggs": {
        "2": {
            "terms": {
                "field": "domain",
                "size": 500,
                "order": {
                    "_count": "desc"
                }
            },
            "aggs": {
                "3": {
                    "terms": {
                        "field": "status",
                        "size": 20,
                        "order": {
                            "_count": "desc"
                        }
                    }
                }
            }
        }
    },
    "stored_fields": [
        "*"
    ],
    "script_fields": {

    },
    "docvalue_fields": [
        "@timestamp"
    ],
    "query": {
        "bool": {
            "must": [
                {
                    "match_all": {

                    }
                },
                {
                    "range": {
                        "@timestamp": {
                            "gte": 1527336585166,
                            "lte": 1527336705166,
                            "format": "epoch_millis"
                        }
                    }
                }
            ],
            "filter": [

            ],
            "should": [

            ],
            "must_not": [

            ]
        }
    }
}

json_reqstime_avi = {
    "size": 0,
    "_source": {
        "excludes": [

        ]
    },
    "aggs": {
        "2": {
            "terms": {
                "field": "domain",
                "size": 50,
                "order": {
                    "_count": "desc"
                }
            },
            "aggs": {
                "3": {
                    "filters": {
                        "filters": {
                            "bad_request_time": {
                                "query_string": {
                                    "query": "request_time :>1.5",
                                    "analyze_wildcard": True,
                                    "default_field": "*"
                                }
                            },
                            "good_request_time": {
                                "query_string": {
                                    "query": "request_time :<=1.5",
                                    "analyze_wildcard": True,
                                    "default_field": "*"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "stored_fields": [
        "*"
    ],
    "script_fields": {

    },
    "docvalue_fields": [
        "@timestamp"
    ],
    "query": {
        "bool": {
            "must": [
                {
                    "match_all": {

                    }
                },
                {
                    "range": {
                        "@timestamp": {
                            "gte": 1527474117582,
                            "lte": 1527475017582,
                            "format": "epoch_millis"
                        }
                    }
                }
            ],
            "filter": [

            ],
            "should": [

            ],
            "must_not": [

            ]
        }
    }
}

keyword_count = {"size": 0, "_source": {"excludes": []},
                 "aggs": {"2": {"date_range": {"field": "@timestamp", "ranges": [{"from": "now-2m", "to": "now"}]}}},
                 "stored_fields": ["*"], "script_fields": {}, "docvalue_fields": ["@timestamp"], "query": {"bool": {
        "must": [{"query_string": {"query": "\"Resolving timed out\"", "analyze_wildcard": True, "default_field": "*"}},
                 {"range": {"@timestamp": {"gte": 1536729216060, "lte": 1536732816060, "format": "epoch_millis"}}}],
        "filter": [], "should": [], "must_not": []}}}


get_domain_proxy_json={
    "size":0,
    "_source":{
        "excludes":[
            "xinche_order.xxx.com"
        ]
    },
    "aggs":{
        "2":{
            "terms":{
                "field":"beat.hostname",
                "size":1,
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
                        "query":"\"ws-org.xxx-int.com\"",
                        "analyze_wildcard":True,
                        "default_field":"*"
                    }
                },
                {
                    "range":{
                        "@timestamp":{
                            "gte":1539174071038,
                            "lte":1539174971039,
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
get_499less500ms_count_json={
    "size":0,
    "_source":{
        "excludes":[
            "xinche_order.xxx.com"
        ]
    },
    "aggs":{
        "2":{
            "filters":{
                "filters":{
                    "request_time:<0.4":{
                        "query_string":{
                            "query":"request_time:<0.4",
                            "analyze_wildcard":True,
                            "default_field":"*"
                        }
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
                        "query":"\"wx-apm.xxx.com\"",
                        "analyze_wildcard":True,
                        "default_field":"*"
                    }
                },
                {
                    "match_phrase":{
                        "status":{
                            "query":499
                        }
                    }
                },
                {
                    "range":{
                        "@timestamp":{
                            "gte":1539782612138,
                            "lte":1539783512138,
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
pv_diff_json={
    "size":0,
    "_source":{
        "excludes":[
            "xinche_order.xxx.com"
        ]
    },
    "aggs":{
        "2":{
            "date_histogram":{
                "field":"@timestamp",
                "interval":"1m",
                "time_zone":"Asia/Shanghai",
                "min_doc_count":0
            },
            "aggs":{
                "3":{
                    "serial_diff":{
                        "buckets_path":"_count"
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
                        "query":"\"mcrypt.dns.xxx.com\"",
                        "analyze_wildcard":True,
                        "default_field":"*"
                    }
                },
                {
                    "range":{
                        "@timestamp":{
                            "gte":1541335800000,
                            "lte":1541339999999,
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
get_domain_list_json={
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
                "size":5000,
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
                    "match_all":{

                    }
                },
                {
                    "range":{
                        "@timestamp":{
                            "gte":1541428376909,
                            "lte":1541429276911,
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

def Connect_es(index, json):
    """
    连接es数据库
    """
    es = Elasticsearch([{"host": "ip1", "port": 9200, "timeout": 150}])
    res = es.search(
        index=index,
        body=json,
    )
    return res

def insert_es(doc_type, index, json):
    """
    插入es数据
    """
    es = Elasticsearch([{"host": "ip2", "port": 9200, "timeout": 150}])
    res = es.index(
        doc_type=doc_type,
        index=index,
        body=json,
    )
    return res

def get_domain_conflist():
    """
    读取域名列表
    """
    base_dir = os.path.split(os.path.realpath(__file__))[0]
    global domain_conflist
    global cf
    cf = ConfigParser.ConfigParser()
    cf.read(base_dir + "/conf.ini")

def night_threshold_value(value):
    """
    夜间报警阈值
    """
    if datetime.datetime.now().hour > 23  or  datetime.datetime.now().hour <7 :
        night_threshold_value  = float(value) * 0.6
    else:
        night_threshold_value=value
    return night_threshold_value

def get_domain_list():
    """
    获取域名list
    """
    start = long(time.time() - interval_time * 60) * 1000
    end = long(time.time() * 1000)
    get_domain_list_json["query"]["bool"]["must"][1]["range"]["@timestamp"]["gte"] = start
    get_domain_list_json["query"]["bool"]["must"][1]["range"]["@timestamp"]["lte"] = end
    try:
        jdata = Connect_es(index, get_domain_list_json)
        msg_count = jdata["hits"]["total"]
    except Exception as e:
        logging.error(e)
    return jdata["aggregations"]["2"]["buckets"]

def pv_diff(index):
    """
    统计域名pv
    """
    for i in get_domain_list():    # 调用接口获取域名列表,挨个检测
        pv_diff_rate=0
        domain=i["key"]
        domain_pv=i["doc_count"]
        start = long(time.time() - 5 * 60 ) * 1000    # 计算5分钟内值
        end = long(time.time() ) * 1000    # 60*60000-1
        pv_diff_json["query"]["bool"]["must"][1]["range"]["@timestamp"]["gte"] = start
        pv_diff_json["query"]["bool"]["must"][1]["range"]["@timestamp"]["lte"] = end
        pv_diff_json["query"]["bool"]["must"][0]["query_string"]["query"] = "\""+domain+"\""
        if domain_pv > 10000:    # 如果域名pv大于500才计算
            try:
                jdata = Connect_es(index,pv_diff_json)    # 获取5分钟内pv变化数
                msg_count = jdata["hits"]["total"]
            except Exception as e:
                logging.error(e)
        """
        如果pv大于500,且都能获取到变化量则统计计算
        """
            # pv巨增模型
            if jdata["aggregations"]["2"]["buckets"][-5]["doc_count"] > 3000 and (jdata["aggregations"]["2"]["buckets"][-5]["doc_count"] - jdata["aggregations"]["2"]["buckets"][-2]["doc_count"] ) <0 :
                pv_diff_rate= (jdata["aggregations"]["2"]["buckets"][-2]["doc_count"] - jdata["aggregations"]["2"]["buckets"][-5]["doc_count"] ) / float(jdata["aggregations"]["2"]["buckets"][-2]["doc_count"] )*100
                print pv_diff_rate
            # pv巨减模型
            if jdata["aggregations"]["2"]["buckets"][-5]["doc_count"] > 2000 and (jdata["aggregations"]["2"]["buckets"][-5]["doc_count"] - jdata["aggregations"]["2"]["buckets"][-2]["doc_count"]) > 0:
                pv_diff_rate = (jdata["aggregations"]["2"]["buckets"][-5]["doc_count"] - jdata["aggregations"]["2"]["buckets"][-2]["doc_count"]) / float(jdata["aggregations"]["2"]["buckets"][-5]["doc_count"]) * 100
                print pv_diff_rate
            if domain in cf.sections():
            """
            以上计算中间3分钟的变化率
            """
                if float(pv_diff_rate) > int(cf.get(domain, "alert_pv_diff_rate")):
                    proxy_name = get_domain_proxy(domain)
                    msg = "[P]域名PV剧变:%s (来源:%s)\n    变化率:%s(阈值:%s) \n    详情:[由 %s To %s]" % (domain, proxy_name, str(pv_diff_rate)[:5], int(cf.get(domain, "alert_pv_diff_rate")),jdata["aggregations"]["2"]["buckets"][-5]["doc_count"],jdata["aggregations"]["2"]["buckets"][-2]["doc_count"])
                    write_tmp(domain, msg)
                    printmsg
            else:
                 if float(pv_diff_rate) > float(alert_pv_diff_rate):
                    proxy_name = get_domain_proxy(domain)
                    msg = "[P]域名PV剧变:%s (来源:%s)\n    变化率:%s(阈值:%s) \n    详情:[由 %s To %s]" % (domain, proxy_name, str(pv_diff_rate)[:5], alert_pv_diff_rate,jdata["aggregations"]["2"]["buckets"][-5]["doc_count"], jdata["aggregations"]["2"]["buckets"][-2]["doc_count"])
                    write_tmp(domain, msg)
                    print msg

def get_499less500ms_count(domain,start,end):
    """
    获取状态码为499且耗时小于500ms的域名
    """
    # print start,end
    get_499less500ms_count_json["query"]["bool"]["must"][2]["range"]["@timestamp"]["gte"] = start
    get_499less500ms_count_json["query"]["bool"]["must"][2]["range"]["@timestamp"]["lte"] = end
    get_499less500ms_count_json["query"]["bool"]["must"][0]["query_string"]["query"] =  "\""+domain+"\""
    try:
        jdata = Connect_es(index,  get_499less500ms_count_json)
        msg_count = jdata["hits"]["total"]
    except Exception as e:
        logging.error(e)
    return jdata["aggregations"]["2"]["buckets"]["request_time:<0.4"]["doc_count"]

def get_domain_proxy(domain):
    """
    获取域名代理
    """
    index="nginx-access-*"
    start =long(time.time() - interval_time * 60) * 1000
    end = long(time.time() * 1000)
    get_domain_proxy_json["query"]["bool"]["must"][1]["range"]["@timestamp"]["gte"] = start
    get_domain_proxy_json["query"]["bool"]["must"][1]["range"]["@timestamp"]["lte"] = end
    get_domain_proxy_json["query"]["bool"]["must"][0]["query_string"]["query"] = "\""+domain+"\""
    try:
        jdata = Connect_es(index, get_domain_proxy_json)
        res = jdata["aggregations"]["2"]["buckets"][0]["key"]
    except Exception as e:
        logging.error(e)
    return res

def tongji_reqstime_avi(index):
    """
    统计request的平均耗时
    """
    start =long(time.time() - interval_time * 60) * 1000
    end = long(time.time() * 1000)
    json_reqstime_avi["aggs"]["2"]["terms"]["size"] = domain_conut
    json_reqstime_avi["query"]["bool"]["must"][1]["range"]["@timestamp"]["gte"] = start
    json_reqstime_avi["query"]["bool"]["must"][1]["range"]["@timestamp"]["lte"] = end
    json_reqstime_avi["aggs"]["2"]["aggs"]["3"]["filters"]["filters"]["bad_request_time"]["query_string"][
        "query"] = "request_time :>" + str(good_resquestime)
    json_reqstime_avi["aggs"]["2"]["aggs"]["3"]["filters"]["filters"]["good_request_time"]["query_string"][
        "query"] = "request_time :<=" + str(good_resquestime)
    msg_count = 0
    try:
        jdata = Connect_es(index, json_reqstime_avi)
        msg_count = jdata["hits"]["total"]
    except Exception as e:
        logging.error(e)
    if msg_count > 0:
        for i in jdata["aggregations"]["2"]["buckets"]:
            domain = i["key"]
            allcount = i["doc_count"]
            rightcount = i["3"]["buckets"]["good_request_time"]["doc_count"]
            reqstime_avi = 100
            if re.search(r"xxx|yyy|zzz", domain):
                if allcount > base_pvconut:
                    if rightcount > 0:
                        reqstime_avi = float(rightcount) / allcount * 100
                    else:
                        reqstime_avi = 0
            if domain in cf.sections():
                if reqstime_avi < night_threshold_value(int(cf.get(domain, "reqtime_avi_alert"))):
                    proxy_name=get_domain_proxy(domain)
                    msg = "[T]响应超长告警: %s (来源:%s)\n    可用性:%s(阈值:%s) \n    [总请求:%s,大于%ss请求:%s]" % (
                    domain,proxy_name, str(reqstime_avi)[:5], str(night_threshold_value(int(cf.get(domain, "reqtime_avi_alert")))), allcount, good_resquestime,
                    allcount - rightcount)
                    write_tmp(domain, msg)
            else:
                if reqstime_avi < alert_value_reqstime_avi:
                    proxy_name = get_domain_proxy(domain)
                    msg = "[T]响应超长告警:%s (来源:%s)\n    可用性:%s(阈值:%s) \n    [总请求:%s,大于%ss请求:%s]" % (
                    domain,proxy_name, str(reqstime_avi)[:5], alert_value_reqstime_avi, allcount, good_resquestime,
                    allcount - rightcount)
                    write_tmp(domain, msg)

def tongji_status_avi(index):
    """
    统计状态码平均值
    """
    start = long(time.time() - interval_time * 60 - 10) * 1000
    end = long(time.time() -10) * 1000    # //60*60000-1
    json_reqstime_avi["aggs"]["2"]["terms"]["size"] = domain_conut
    json_domain_ava["query"]["bool"]["must"][1]["range"]["@timestamp"]["gte"] = start
    json_domain_ava["query"]["bool"]["must"][1]["range"]["@timestamp"]["lte"] = end
    msg_count = 0
    try:
        jdata = Connect_es(index, json_domain_ava)
        msg_count = jdata["hits"]["total"]
    except Exception as e:
        logging.error(e)
    if msg_count > 0:
        for i in jdata["aggregations"]["2"]["buckets"]:
            domain = i["key"]
            allcount = i["doc_count"]
            rightcount = 0
            domainavi = 100
            m = []
            new_dict = {}
            if re.search(r"xxx|yyy|zzz", domain):
                for p in i["3"]["buckets"]:
                    m.append(p.values())
                    if domain in cf.sections():
                        if str(p.values()[0]) not in (cf.get(domain, "err_stat")).split(','):
                            rightcount += p.values()[1]
			if (str(p.values()[0]) == "499" ) and (str(p.values()[0])  in (cf.get(domain, "err_stat")).split(',')):
                            rightcount += int(get_499less500ms_count(domain,start,end))
                    else:
                        if str(p.values()[0]) not in err_stat.split(','):
                            rightcount += p.values()[1]
                        if (str(p.values()[0]) == "499") and (str(p.values()[0]) in err_stat.split(',')):
                            rightcount += int(get_499less500ms_count(domain, start, end))
                    if rightcount > 0:
                        domainavi = float(rightcount) / allcount * 100
                    else:
                        domainavi = 0
            for i in m:
                new_dict[i[0]] = i[1]
            new_dict["domain"] = domain
            new_dict["Reliability"] = domainavi
            new_dict["@timestamp"] = datetime.datetime.utcnow()
            new_dict["type"] = "sre_Reliability"
            new_dict["pv"] = allcount
            new_dict["err_stat"] = err_stat
            insert_es("doc", "sre-" + datetime.datetime.now().strftime("%Y-%m"), new_dict)
            # print domain,domainavi
            if allcount > base_pvconut:
                if domain in cf.sections():
                    if domainavi <  night_threshold_value(int(cf.get(domain, "status_avi_alert"))):
                        proxy_name = get_domain_proxy(domain)
                        msg = "[S]状态异常告警:%s (来源:%s)\n    可用性:%s(阈值%s)\n    详情[%s]" % (
                        domain,proxy_name, str(domainavi)[:5], str(night_threshold_value(int(cf.get(domain, "status_avi_alert")))), str(m))
                        #print msg
                        write_tmp(domain, msg)
                else:
                    if domainavi < alert_value_status:
                        proxy_name = get_domain_proxy(domain)
                        msg = "[S]状态异常告警:%s (来源:%s)\n    可用性:%s(阈值%s)\n    详情[%s]" % (
                        domain,proxy_name, str(domainavi)[:5], alert_value_status, str(m))
                        #print msg
                        write_tmp(domain, msg)

def tongji_keyword_count(index, keyword):
    """
    统计关键字次数
    """
    max_count = 250
    start = long(time.time() - interval_time * 60) * 1000
    end = long(time.time()) * 1000    # //60*60000-1
    keyword_count["query"]["bool"]["must"][1]["range"]["@timestamp"]["gte"] = start
    keyword_count["query"]["bool"]["must"][1]["range"]["@timestamp"]["lte"] = end
    keyword_count["query"]["bool"]["must"][0]["query_string"]["query"] = keyword
    try:
        jdata = Connect_es(index, keyword_count)
        msg_count = jdata["aggregations"]["2"]["buckets"][0]["doc_count"]
    except Exception as e:
        logging.error(e)
    if msg_count >= max_count:
        msg="[K] Keyword [" + str(keyword) + "] > " + str(max_count) + "个[2 min] [当前"+ str(msg_count) + "个]"
        write_tmp("key_word",msg)

def send_im(alert_user, msg):
    """
    通过内部im发送报警
    """
    os.popen(
        "curl notbot.xxx-int.com/api/sendmsg.peter -d to='" + alert_user + "' -d content='" + msg + "' -d subject=域名报警 ")

def write_tmp(domain, msg):
    """
    发送邮件报警
    """
    if domain in cf.sections():
        if cf.get(domain, "contact"):
            for i in cf.get(domain, "contact").split(','):
                f = open('/tmp/mailuser/' + str(i), 'a')
                f.write(msg + '\n')
                f.close()
    else:
        for i in contact.split(','):
            f = open('/tmp/mailuser/' + str(i), 'a')
            f.write(msg + '\n')
            f.close()

get_domain_conflist()    # 主函数
index = "nginx-access-*"
if not os.path.exists('/tmp/mailuser/'):
    os.makedirs('/tmp/mailuser/')

"""
初始化阈值，默认90, 夜间打折
"""
alert_value_status = int(night_threshold_value(95))
alert_value_reqstime_avi = int(night_threshold_value(90))

tongji_status_avi(index)
tongji_reqstime_avi(index)
pv_diff(index)

index_php_server = "php-service-*"
tongji_keyword_count(index_php_server,"\"Resolving timed out\"")

if os.listdir('/tmp/mailuser/') != []:
    for root, dirs, files in os.walk("/tmp/mailuser/"):
        for i in files:
            f = open('/tmp/mailuser/' + i, 'r')
            alert_msg = f.read()
            send_guagua(i, str(alert_msg))
            os.remove("/tmp/mailuser/" + i)

