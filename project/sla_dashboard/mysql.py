#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    mysql
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import MySQLdb
import time, datetime
from datetime import datetime
from datetime import timedelta
import re
import sys
import json

gap = 3
reload(sys)
sys.setdefaultencoding('utf-8')

def query_db(sql):
    try:
        conn=MySQLdb.connect(host="ip",port=3999,user="user_w",passwd="passwd",db="cmdb",charset="utf8")
        cursor = conn.cursor()
        cursor.execute(sql)
        alldata = cursor.fetchall()
        cursor.close()
        conn.close()
        return alldata
    except Exception, e:
        print e
