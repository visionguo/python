#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2021/03/22
# Brief:
#    gen_case_id
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from mysql import query_db, modify_db
import datetime

def gen_case_id():
    today = datetime.date.today()
    str_today = str(today).replace('-','')
    qsql = "select count(1) from noc where serial_number like %s" % ("'%" + str_today + "%'",)
    case_num = query_db(qsql)
    next_case_num = int(case_num[0][0]) + 1
    case_id = str_today + '_' + str(next_case_num)
    msql = "insert into noc (serial_number) values (%s) " % ("'" + case_id + "'")
    return case_id

