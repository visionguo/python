# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    query_time
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import datetime
from flask import request

def get_days(start_time, n):
    """
    Get days
    """
    end_time = (start_time - datetime.timedelta(days=n)).strftime('%Y-%m-%d')
    old_time = (start_time - datetime.timedelta(days=n + n)).strftime('%Y-%m-%d')
    return end_time, old_time
    
def get_time():
    """
    Get time
    """
    query_time = request.args.get("query_time", "")

    if query_time:
        if query_time == '3d':
            n = 3
            start_time = (datetime.datetime.now() - datetime.timedelta(days=1))
        elif query_time == '7d':
            n = 7
            weekday = int(datetime.datetime.now().strftime('%w'))
            start_time = (datetime.datetime.now() - datetime.timedelta(days=weekday))
        elif query_time == '30d':
            n = 1
            monthday = int(datetime.datetime.now().strftime('%d'))
            start_time = (datetime.datetime.now() - datetime.timedelta(days=monthday))
        else:
            n = 7
            start_time = (datetime.datetime.now() - datetime.timedelta(days=1))    #从昨天开始算
            query_time='7d'
        
    else:    
       n = 7
       start_time = (datetime.datetime.now() - datetime.timedelta(days = 1))    #从昨天开始算
       query_time = "7d"
        
    end_time, old_time = get_days(start_time, n)
    start_time = start_time.strftime('%Y-%m-%d')

    return start_time, end_time, old_time, query_time
 





