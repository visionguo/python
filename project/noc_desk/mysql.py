#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2021/03/22
# Brief:
#    mysql
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import pymysql

def query_db(sql):
    db = pymysql.connect(host="ip",    # your host, usually localhost
                         user="noc",    # your username
                         passwd="nocpasswd",    # your password
                         db="noc")    # name of the data base
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(e)
    db.close()

def modify_db(sql):
    """
    更改mysql
    """
    db = pymysql.connect(host="10.16.208.178",    # your host, usually localhost
                         user="noc",         # your username
                         passwd="nocpasswd",  # your password
                         db="noc")        # name of the data base

    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        d = {'res': 'success'}
        print(d)
        return (d)
    except:
        db.rollback()
        d = {'res': 'fail'}
        return (d)
    db.close()