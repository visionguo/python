#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2021/04/06
# Brief:
#    volume_sold_percent_gt_80
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

with open('/Users/guoshaogang/Documents/github_0321/practice_0322/volume_sold_percent_gt_80.txt', 'r') as f:    # 打开文件
    data = f.readlines()    # 读取所有行数
    for i in data:    # 遍历所有行数，每次只取一行
        x = i.split()    # 以空格为分隔符对数据进行切分
        sub_num = float(x[3]) - float(x[4])    # 数值相减，float方法将str转换为浮点型
        if sub_num < 100:    # 当剩余量小于100时
            print(x[1], x[2], round(sub_num, 2))    # 打印

"""
从数据库获取数据
"""
# mysql -h10.21.104.247 -P3306 -uiaas_op_storage -pBaidu123#@! -Ne "use iaas_op_cds;select * from cds_cluster_capacity where volume_sold_percent > 80;" > volume_sold_percent_gt_80.txt


import MySQLdb

"""
定义连接数据库函数
"""
def mysql_connect():
    try:
            db = MySQLdb.connect(host="10.21.104.247", user="iaas_op_storage", passwd="Baidu123#@!", db="iaas_op_cds", \
                                         connect_timeout=10, charset='utf8')    # 打开数据库连接
            cursor = db.cursor()    # 使用cursor（）方法获取操作游标
            sql = "select * from cds_cluster_capacity where volume_sold_percent > 80;"    # SQL查询语句
            try:
                cursor.execute(sql)    # 执行SQL语句
                data_all = cursor.fetchall()    # 获取所有记录列表
#                print(data_all)
                for row in data_all:
                    id = row[0]
                    cluster_name = row[1]
                    capacity_type = row[2]
                    volume_total_capacity = row[3]
                    volume_sold_capacity = row[4]
                    volume_sold_percent = row[5]
                    node_nums = row[6]
                    update_time = row[7]
#                    print("cluster_name=%s, capacity_type=%s, volume_total_capacity=%s, volume_sold_capacity=%s" % (cluster_name, capacity_type, volume_total_capacity, volume_sold_capacity))
                    div_num = (volume_sold_capacity / volume_total_capacity) * 100
                    sub_num = volume_total_capacity - volume_sold_capacity
                    if sub_num < 100:
                        print("cluster_name=%s, capacity_type=%s, volume_can_sold_capacity: %dT, volume_sold_percent: %d" % (cluster_name, capacity_type, sub_num, div_num))
            except Exception:
                print("Error: unable to fecth data")
            cursor.close()
            db.close()
    except Exception:
            print("Error: Can not Connect to mysql server")

if __name__ == '__main__':
    mysql_connect()