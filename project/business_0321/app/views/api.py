#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    app
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import json
from flask import Response, request
from app.db import MySQL_query, Presto_query

def cmdb_business():
    """
    Get business via cmdb
    """
    sql = "select * from business"
    fields = ['id', 'name', 'name_english', 'person_duty', 'org_id']
    object = MySQL_query()
    result = object.mysql_RowProxy_to_list(sql, fields)
    print(result)
    return Response(json.dumps(result, indent=3, ensure_ascii=False), mimetype='application/json')

def cmdb_business_orm():
    """
    Get business_orm via cmdb
    """
    object_mymysql_RowProxy_to_list = MySQL_query()
    result = object_mymysql_RowProxy_to_list.orm_query()
    print(result)

def cmdb_subbusiness():
    """
    Get subbusiness via cmdb
    """
    sql = "select * from subbusiness"
    fields = ['id', 'name', 'name_english', 'person', 'business_id']
    object = MySQL_query()
    result = object.mysql_RowProxy_to_list(sql, fields)
    return Response(json.dumps(result, indent=3, ensure_ascii=False), mimetype='application/json')

def cmdb_domain():
    """
    Get domain via cmdb
    """
    domain_arg = request.args.get("domain", "")
    domain =  domain_arg.replace(',', '|')
    sql = "select * from domain where name regexp " + "'"+domain+"'"
    fields = ['id', 'name', 'ip', 'use_for', 'person_duty', 'project_id', 'subbusiness_id']
    object = MySQL_query()
    result = object.mysql_RowProxy_to_list(sql, fields)
    return Response(json.dumps(result, indent=3, ensure_ascii=False), mimetype='application/json')

def presto_domain():
    """
    Get presto_domain
    """
    domain_arg = request.args.get("domain", "")
    domain =  domain_arg.replace(",", "' or domain='")
    sql = "select dt,dh,domain,count(domain) as total_count from sre.nginx_access where (domain='"+domain+"') \
          and dt='2018-10-19' and dh>'20' and status=200 group by dt,dh,domain order by dt desc,dh desc"
    fields = ['dt', 'dh', 'domain', 'total_count']
    object = Presto_query()
    result = object.presto_Tuple_to_list(sql, fields)
    return Response(json.dumps(result, indent=3, ensure_ascii=False), mimetype='application/json')
