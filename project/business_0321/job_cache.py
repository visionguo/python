# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    job_cache
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from flask import Response, request
from config import config
from sqlalchemy import create_engine
import os
import sys
import requests

FLASK_CONFIG = sys.argv[1]
config_name = config[FLASK_CONFIG]
print(FLASK_CONFIG)

def connect_db(sql):
    """
    connect db
    """
    engine = create_engine(config_name.CMDB_DATABASE_URI)
    connection = engine.connect()
    result = connection.execute(sql)
    
    data = result.fetchall()    # list格式输出所有RowProxy对象
    connection.close()
    return data

for day in '1d', '3d', '7d':
    url = "%ssla?query_time=%s" % (config_name.CACHE_DOMAIN, day)
    print(url)
    res = requests.get(url) 
    print(res.elapsed.total_seconds())
    print(res.status_code)

for day in '1d', '3d', '7d', '1m':
    url2 = "%srelease?query_time=%s" % (config_name.CACHE_DOMAIN, day)
    print(url2)
    res2 = requests.get(url2) 
    print(res2.elapsed.total_seconds())
    print(res2.status_code)

print("job Ok")
