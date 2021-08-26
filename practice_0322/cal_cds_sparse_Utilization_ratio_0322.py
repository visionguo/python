#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2021/03/22
# Brief:
#    cal_cds_sparse_Utilization_ratio
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import os
import sys
import time
import re
import MySQLdb

"""
region_name列表
"""
region_name_list = ['r0_sparse', 'r1_sparse', 'r2_sparse', 'r3_sparse', 'r4_sparse', 'r5_sparse', 'r6_sparse',
                    'r7_sparse', 'r8_sparse', 'r9_sparse']

def cal_cds_sparse_ratio():
    """
    定义连接数据库函数
    """
    try:
        db = MySQLdb.connect(host="10.21.104.247", user="iaas_op_storage", passwd="Baidu123#@!", db="iaas_op_cds", \
                                     connect_timeout=10, charset='utf8')    # 打开数据库连接
        cursor = db.cursor()    # 使用cursor（）方法获取操作游标
        sql = "select *  from cds_cluster_region_capacity where region_name like '%sparse%';"    # SQL查询语句
        try:
            cursor.execute(sql)    # 执行SQL语句
            data_all = cursor.fetchall()    # 获取所有记录列表
            for row in data_all:
                cluster_name = row[1]
                region_name = row[2]
                capacity_type = row[3]
                disk_total_capacity = row[4]
                disk_used_capacity = row[5]

                """
                要对输出的数据进行的操作
                """
                for sparse_num in range(10):
                    if (region_name == region_name_list[sparse_num]):
                        if (capacity_type == 'ssd'):
                            ssd_total = disk_total_capacity
                            ssd_used = disk_used_capacity
                            float_ssd_total = round(float(ssd_total))
                            float_ssd_used = round(float(ssd_used))
                        elif (capacity_type == 'sata'):
                            sata_total = disk_total_capacity
                            sata_used = disk_used_capacity
                            float_sata_total = round(float(sata_total))
                            float_sata_used = round(float(sata_used))
                            ratio_total = "%.2f" % (float_sata_total / float_ssd_total)
                            ratio_used = "%.2f" % (float_sata_used / float_ssd_used)
                            if (ratio_total >= "3"):
                                print(cluster_name, region_name, ratio_total)
                time.sleep(0.1)  # 进程挂起的时间
        except Exception:
            print("Error: unable to fecth data")
        cursor.close()
        db.close()
    except Exception:
        print("Error: Can not Connect to mysql server")

if __name__ == '__main__':
    cal_cds_sparse_ratio()