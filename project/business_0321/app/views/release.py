# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    release
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from flask import  render_template, Response, request
from app.db import MySQL_query, Cache_query
from .query_time import get_time
from .mythread import MyThread
import datetime
import requests
import os
import threading

from config import config

config_name = config[os.getenv('FLASK_CONFIG') or 'default']

def get_business_gitpid(business_name):
    """
    获取该业务线下的所有主机
    """
    cmdb_domain = config_name.CMDB_DOMAIN
    host_url = cmdb_domain + "/api/v1/asset/business/" + business_name
    req = requests.get(host_url)
    hosts = req.json()

    result_str = ''
    
    mysql_object = MySQL_query()
    print("根据主机信息间接获取特定项目属于特定业务线, 直接读库")
    for i in range(len(hosts)):
            result_str = result_str +  hosts[i]['hostname'] + "%%' or onlinehost like '%%"
    fuck = "onlinehost like '%%" + result_str + "fuckfuck%%'"  
    # cmdb的gitlab_pid 叫 git_group
    gitlab_sql = "select git_group from projects where %s" % fuck
    gitlab_pids = mysql_object.mysql_RowProxy_to_str(gitlab_sql, 'cmdb')

    print(gitlab_pids)
    return gitlab_pids

def earthworm_release(business_name, start_time, end_time, old_time, query_time):
    """
    CI/CD 平台信息
    """
    mysql_object = MySQL_query()
    cache_object = Cache_query()

    """
    判断是否有缓存，再加一级缓存
    """
    cache_key = "008_" + query_time + "_" + start_time + "__earthworm__" +  business_name
    cache = cache_object.get_redis(cache_key)
    result = []
    if cache:
        print("OK")
        result = eval(cache)
    else:
        gitlab_pids = get_business_gitpid(business_name)
        """
        输出查询的是项目名gitgroup/gitname + 发布id + 发布人 + 发布包名 + 发布时间
        """
        if gitlab_pids:
            print("进入earthworm")
            earthworm_release_sql = "select project_gitlab.gitlab_pid as name, release_apply.id as release_id, release_apply.apply_user_id as user, \
                release_apply.package_name as package , release_apply.create_time  as create_time from project_gitlab  \
                left join release_apply on project_gitlab.project_id=release_apply.project_id  where \
                (release_apply.online_task_id is not null or release_apply.online_gray_task_id is not null ) and  \
                project_gitlab.gitlab_pid in (%s) and  \
                (release_apply.create_time>'%s 24:00' and release_apply.create_time<='%s 24:00') " % (gitlab_pids, end_time, start_time)
            print(earthworm_release_sql)
            fields = ['name', 'release_id', 'user', 'package', 'create_time']
            result = mysql_object.mysql_RowProxy_to_list(earthworm_release_sql, fields, 'earthworm')
        
            result.sort(key=lambda  x:(x['name'],x['release_id']), reverse=False)
            print("No")
            cache_object.set_redis(cache_key, result)
    return result

def medusa_release(business_name, start_time, end_time, old_time, query_time):
    """
    Docker环境上线平台信息
    """
    mysql_object = MySQL_query()
    cache_object = Cache_query()
    
    """
    判断是否有缓存，再加一级缓存
    """
    cache_key = "008_" + query_time + "_" + start_time + "__medusa__" +  business_name
    cache = cache_object.get_redis(cache_key)
    result = []
    if cache:
        print("OK")
        result = eval(cache)
    else:
        gitlab_pids = get_business_gitpid(business_name)
        if gitlab_pids:
            #输出查询的是项目名gitgroup/gitname + 发布id + 发布人 + 发布包名 + 发布时间
            print("进入medusa")
            medusa_release_sql = "select app.gitlab_pid as name, app_deploy_history.id as release_id, app_deploy_history.operator as user, app_deploy_history.deploy_name as package, app_deploy_history.created_at as create_time from app \
                left join app_deploy_history on app.id=app_deploy_history.app_id  \
                where app_deploy_history.deploy_status = 'success' and   \
                app_deploy_history.cluster = 'online' and  \
                app.gitlab_pid in (%s)  and   \
                (app_deploy_history.created_at>'%s 24:00' and app_deploy_history.created_at<='%s 24:00') " % (gitlab_pids, end_time, start_time)
            print(medusa_release_sql)
            fields = ['name', 'release_id', 'user', 'package', 'create_time']
            result = mysql_object.mysql_RowProxy_to_list(medusa_release_sql, fields, 'medusa')
            
            result.sort(key=lambda  x:(x['name'],x['release_id']), reverse=False)
            cache_object.set_redis(cache_key, result)
    return result

def release():
    """
    release
    """
    start_time, end_time, old_time, query_time = get_time() 
    url = request.url   
    url = url.split('?')[0] 
    
    cache_object = Cache_query()

    """
    判断是否有缓存，再加一级缓存
    """
    cache_key = "008_" + query_time + "_" + start_time + "__release"
    cache = cache_object.get_redis(cache_key)
    if cache:
        print("OK")
        result = eval(cache)
    else:
        """
        获取所有业务线
        """
        business_url = config_name.CMDB_DOMAIN + "/api/v1/business/"
        req = requests.get(business_url)
        business = req.json()

        result = []
        for i in range(len(business)):
            result_json = {}
            business_name = business[i]['name']
            business_person = business[i]['person_duty']
            business_name_english = business[i]['name_english']   
            print(business_name)         

            release_earthworm = earthworm_release(business_name, start_time, end_time, old_time, query_time)
            release_medusa  = medusa_release(business_name, start_time, end_time, old_time, query_time)
            
            earthworm_release_count = len(release_earthworm)
            medusa_release_count = len(release_medusa)

            result_json['earthworm_release_count'] = earthworm_release_count 
            result_json['medusa_release_count'] = medusa_release_count
            result_json['business_name'] = business_name
            result_json['business_person'] = business_person
            result_json['business_name_english'] = business_name_english
            result.append(result_json)

        result.sort(key=lambda  x:(x['earthworm_release_count'],x['medusa_release_count']), reverse=False)
        print("No")
        cache_object.set_redis(cache_key, result)
    """
    获取release的总数
    """
    earthworm_release_all = 0
    medusa_release_all = 0
    for i in range(len(result)):
        earthworm_release_all = earthworm_release_all + result[i]['earthworm_release_count']
        medusa_release_all = medusa_release_all + result[i]['medusa_release_count']
    return  render_template('release.html', re=result, url=url, query_time=query_time, earthworm_release_all=earthworm_release_all, medusa_release_all=medusa_release_all)
    
def earthworm_release_business(business_name):
    """
    CI/CD上线平台维护的业务线信息
    """
    url = request.url   
    url = url.split('?')[0] 
    start_time, end_time, old_time, query_time = get_time() 

    result = earthworm_release(business_name, start_time, end_time, old_time, query_time)

    if result:
        return  render_template('release_detail.html', re=result, url=url, query_time=query_time)
    else:
        return Response("业务线线下没有主机，主机用来获取项目名", mimetype='application/json')

def medusa_release_business(business_name):
    """
    Docker上线平台维护的业务线信息
    """
    url = request.url   
    url = url.split('?')[0] 
    start_time, end_time, old_time, query_time = get_time()

    result = medusa_release(business_name, start_time, end_time, old_time, query_time)
    if result:
        return  render_template('release_detail.html', re=result, url=url, query_time=query_time)
    else:
        return Response("业务线线下没有主机，主机用来获取项目名", mimetype='application/json')

def release_bak():
    """
    维护release信息
    """
    start_time, end_time, old_time, query_time = get_time() 
    url = request.url   
    url = url.split('?')[0] 
    
    mysql_object = MySQL_query()
    cache_object = Cache_query()

    """
    判断是否有缓存，再加一级缓存
    """
    cache_key = "008_" + query_time + "_" + start_time + "__release_bak"
    cache = cache_object.get_redis(cache_key)
    cache = ""
    if cache:
        print("ok")
        result = eval(cache)
    else:
        """
        获取所有业务线
        """
        business_url = config_name.CMDB_DOMAIN + "/api/v1/business/"
        req = requests.get(business_url)
        business = req.json()

        result = []
        for i in range(len(business)):
            result_json = {}
            business_name = business[i]['name']
            business_person = business[i]['person_duty']
            business_name_english = business[i]['name_english']   
            print(business_name)         
            gitlab_pids = get_business_gitpid(business_name)
            if gitlab_pids:
                earthworm_release_sql = "select count(*) as earthworm_release_count from project_gitlab left join release_apply on project_gitlab.project_id=release_apply.project_id  \
                where \
                (release_apply.online_task_id is not null or release_apply.online_gray_task_id is not null ) and  \
                project_gitlab.gitlab_pid in (%s) and  \
                (release_apply.create_time>'%s 24:00' and release_apply.create_time<='%s 24:00') " % (gitlab_pids, end_time, start_time)

                earthworm_release = mysql_object.sql_query(earthworm_release_sql, 'earthworm')
                earthworm_release_count = earthworm_release[0][0]
    
                print("进入medusa")
                medusa_release_sql = "select count(*) as medusa_release_count from app left join app_deploy_history on app.id=app_deploy_history.app_id  \
                    where app_deploy_history.deploy_status = 'success' and   \
                    app_deploy_history.cluster = 'online' and  \
                    app.gitlab_pid in (%s)  and   \
                    (app_deploy_history.created_at>'%s 24:00' and app_deploy_history.created_at<='%s 24:00') " % (gitlab_pids, end_time, start_time)
                print(medusa_release_sql)
                medusa_release = mysql_object.sql_query(medusa_release_sql, 'medusa')
                medusa_release_count = medusa_release[0][0]

                result_json['earthworm_release_count'] = earthworm_release_count 
                result_json['medusa_release_count'] = medusa_release_count
                result_json['business_name'] = business_name
                result_json['business_person'] = business_person
                result_json['business_name_english'] = business_name_english
                result.append(result_json)

        result.sort(key=lambda  x:(x['earthworm_release_count'],x['medusa_release_count']), reverse=False)
        print("No")
        cache_object.set_redis(cache_key, result)

    """
    获取release的总数
    """
    earthworm_release_all = 0
    medusa_release_all = 0
    for i in range(len(result)):
        earthworm_release_all = earthworm_release_all + result[i]['earthworm_release_count']
        medusa_release_all = medusa_release_all + result[i]['medusa_release_count']
    return  render_template('release.html', re=result, url=url, query_time=query_time, earthworm_release_all=earthworm_release_all, medusa_release_all=medusa_release_all)
