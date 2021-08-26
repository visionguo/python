#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2021/04/06
# Brief:
#    cds_essd_20210407
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

# from decimal import Decimal    # 处理decimal数据

"""
浮点型数据相加
"""
# a = 0.1
# b = 0.2
# print(type(a))
# print type(b)
# c = Decimal(str(a)) + Decimal(str(b))
# print c

"""
处理手动导出的mysql数据
"""
# def foo():
#     with open("/Users/guoshaogang/Documents/github_0321/practice_0322/cds_essd_20210407.txt", 'r') as f:
#         my_list = []  # 定义一个空列表
#         for row in f:
#             remove_blank = row.split()    # 去除字符串两端的空白
#             disk_total = remove_blank[0]  # 获取disK_total值
#             disk_used = remove_blank[1]  # 获取disk_used值
#             div_sum = float(disk_used) / float(disk_total)  # 计算出使用率
#             div_num_to_str = str(div_sum)  # 把浮点型数据转换为字符串数据
#             my_list.append(div_num_to_str)  # 把for循环得到的字符串添加进一个列表中
#         return my_list
#
# if __name__ == '__main__':
#     func_to_Variable = foo()  # 将函数赋值给变量
#     total = 0
#     row_num = len(func_to_Variable)
#     for num in range(0, row_num):
#         total = total + float(func_to_Variable[num])
#     print round(total / row_num, 3) * 100  # 浮点型取小数点后三位

import MySQLdb

def foo():
    try:
        db = MySQLdb.connect(host="10.21.104.247", user="iaas_op_storage", passwd="Baidu123#@!", db="iaas_op_cds", \
                                     connect_timeout=10, charset='utf8')    # 打开数据库连接
        cursor = db.cursor()    # 使用cursor（）方法获取操作游标
        sql = "select  disk_total,disk_used from cds_blockserver where disk_type='unknown' and region_name='bjdd_rdma_r1';"    # SQL查询语句
        try:
            cursor.execute(sql)    # 执行SQL语句
            data_all = cursor.fetchall()    # 获取所有记录列表
            my_list = []    # 定义一个空列表
            for row in data_all:
                disk_total = row[0]    # 获取disK_total值
                disk_used = row[1]    # 获取disk_used值
                div_sum = float(disk_used) / float(disk_total)    # 计算出使用率
                div_num_to_str = str(div_sum)    # 把浮点型数据转换为字符串数据
                my_list.append(div_num_to_str)    # 把for循环得到的字符串添加进一个列表中
            return my_list
        except Exception:
            print("Error: unable to fecth data")
        cursor.close()
        db.close()
    except Exception:
            print("Error: Can not Connect to mysql server")

if __name__ == '__main__':
    func_to_Variable = foo()    # 将函数赋值给变量
    total = 0
    row_num = len(func_to_Variable)
    for num in range(0, row_num):
        total = total + float(func_to_Variable[num])
    print round(total/row_num, 3)*100    # 浮点型取小数点后三位