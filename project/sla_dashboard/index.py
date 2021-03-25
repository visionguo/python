#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    index
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from flask import Flask
from flask import Flask, app, request, render_template, redirect, url_for, session, abort, jsonify, make_response, send_from_directory, make_response, jsonify, Response
from mysql import *
from get_domain import *
import sys
from flask import Flask, app, request, render_template, redirect, url_for, session, abort, jsonify, make_response, send_from_directory, make_response, jsonify, Response
from mysql import *
import requests, json, urllib, urllib2, thread, threading
app = Flask(__name__)
reload(sys)
sys.setdefaultencoding('utf-8')

"""
产品线sla页面
"""
@app.route('/serviceline_sla.html')
def  index():
    proxydict=json.loads('{"xx集群":["sys-proxy","pub-proxy"],"yy集群":["sale-web"]}')
    proxy_name=request.args.get('proxy')
    timerate=request.args.get('timerate')
    if (timerate is not None and proxy_name is not None ):
        a=get_domain_all_reliability(proxy_name,timerate,proxydict)
    return render_template('serviceline_sla.html',**locals())

@app.route('/')
@app.route('/overall_sla.html')
def pages():
    proxydict=json.loads('{"xx集群":["sys-proxy","pub-proxy"]}')
    timerate = request.args.get('timerate')
    proxycluster_avi={}
    if (timerate is None):
        timerate="n7"
    for i in proxydict:
            a = get_domain_all_reliability(i, timerate, proxydict)
            print a
            proxycluster_avi[i]=a[0][1],a[1][1]
            print a

    print proxycluster_avi
    return render_template('overall_sla.html', **locals())

"""
push cache数据
"""
@app.route('/pushcache')
def pushcache():
    proxydict=json.loads('{"xx集群":["sys-proxy","pub-proxy"]}')
    timerate = request.args.get('timerate')
    proxycluster_avi={}
    if (timerate is  None):
        timerate="n7"
    for i in proxydict:
            a = get_domain_all_reliability_2(i, timerate, proxydict)
            proxycluster_avi[i]=a[0][1],a[1][1]

"""
绘图页面
"""
@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html', **locals())

"""
基础sla
"""
@app.route('/base_sla.html')
def cards():
    timerate = request.args.get('timerate')
    if (timerate is None):
        timerate = "n7"
    start = get_timerate(timerate)[0]
    end = get_timerate(timerate)[1]
    base_zk_online_info=get_sre_pv_precent("sre*", "online_dubbo_zook", start, end)
    base_zk_pre_info = get_sre_pv_precent("sre*", "pre_dubbo_zook", start, end)
    base_zk_test_info = get_sre_pv_precent("sre*", "test_dubbo_zook", start, end)
    base_etcd_online_info = get_sre_pv_precent("sre*", "online_etcd", start, end)
    base_etcd_pre_info = get_sre_pv_precent("sre*", "pre_etcd", start, end)
    base_etcd_test_info = get_sre_pv_precent("sre*", "test_etcd", start, end)
    start=time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(start / 1000))
    end=time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(end / 1000))
    return render_template('base_sla.html', **locals())

"""
a.html
"""
@app.route('/a.html')
def blacklist():
    a= get_blacklist()
    print a
    return render_template('a.html', **locals())

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run()
