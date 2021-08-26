#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2021/03/22
# Brief:
#    test_0322
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

# from functools import reduce
# def list_dict_duplicate_removal():
#     data_list = [{"a": "123", "b": "321"}, {"a": "123", "b": "321"}, {"b": "321", "a": "123"}, {"d": "12", "sdf": "2312"}]
#     run_function = lambda x, y: x if y in x else x + [y]
#     return reduce(run_function, [[], ] + data_list)
#
# if __name__ == '__main__':
#     print (list_dict_duplicate_removal())

# import MySQLdb
#
# def mysql_connect():
#     try:
#         db = MySQLdb.connect(host="10.21.104.247", user="iaas_op_storage", passwd="Baidu123#@!", db="iaas_op_cds", connect_timeout=10, charset='utf8')    # 打开数据库连接
#         cursor = db.cursor()    # 使用cursor()方法获取操作游标
#         sql = "select * from cds_cluster_region_capacity where region_name like '%sparse' limit 50;"    # SQL查询语句
#         cursor.execute(sql)    # 使用execute方法执行SQL语句
#         data_all = cursor.fetchall()    # 使用fetchall()方法获取一条数据
#         count = data_all[0]
#         cursor.close()
#         db.close()    # 关闭数据库连接
#         print(count)
#     except Exception:
#         print("Can not Connect to mysql server")

# domain = open('domain.txt','rw')
# print "文件名为:" , domain.name    # 读取文件名
#
# line1 = domain.readline()    # 读取第一行
# print line1
#
# line2 = domain.readline(10)    # 读取前10个字节
# print(line2)

# """
# 2021-04-17
# python wsgi
# """
#
# from wsgiref.simple_server import make_server
#
# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Vision Guo!</h1>']
#
# httpd = make_server('', 8080, application)
#
# print("Serving HTTP on port 8080......")
# httpd.serve_forever()    # 开始监听HTTP请求

# def twonums(nums, target):
#     lens = len(nums)
#     j = -1
#     for i in range(lens):
#         if (target-nums[i]) in nums:
#             if (nums.count(target-nums[i] == 1)) & (target - nums[i] == nums[i]):
#                 continue
#             else:
#                 j = nums.index(target-nums[i], i+1)
#                 break
#     if j > 0:
#         return [i, j]
#     else:
#         []
#
# if __name__  == '__main__':
#     nums = [2, 7, 11]
#     target = 9
#     a = twonums(nums, target)
#     print a

# #duck typing
# class duck1():
#     def test(self):
#         print("guagua")
#
# class person1():
#     def test(self):
#         print("I am a personal, I can guagua")
#
# def in_forst(duck):
#     duck.test()
#
# def game():
#     a = duck1()
#     b = person1()
#     in_forst(a)
#     in_forst(b)
#     print(type(in_forst(a)))
#     print(type(in_forst(b)))
#     print(type(a))
#     print(type(b))
#     print(isinstance(a, duck1))
#     print(isinstance(b, person1))
#
#     # isinstance(in_forst(b))
#
# game()

# #monkey patch
# import socket
# import time
#
# print(socket.socket)
#
# print("After monkey patch")
# from gevent import monkey
# monkey.patch_socket()
# print(socket.socket)
#
# import select
# print(select.select)
# monkey.patch_select()
# print("After monkey patch")
# print(select.select)
#
# import time
#
# print(time.time())
#
# def _time():
#     return 1234
#
# time.time = _time
#
# print(time.time())

# ll = [1,2,3]
# d =dict(a=1)
#
# print(type(ll))
# print(type(d))
#
# print(isinstance(ll, list))
# print(isinstance(d, dict))
#
# def add(a, b):
#     if isinstance(a, int):
#         return a+b
#     elif isinstance(a, str):
#         return a.upper() + b
#
# print(add(1, 2))
# print(add('head', 'tail'))
#
# print(id(ll))
# print(id(d))
#
# print(ll is d)
# print(ll is ll)

# 列表和字典推导

# a = ['a', 'b', 'c']
# b = [1, 2, 3]
# #d = ['a':1, 'b':2, 'c':3]
#
# d = {}
# for i in range(len(a)):
#     # a[]= b[i]
#     d[a[i]] = b[i]
#     # print(a[i])
#     # print(b[i])
# print(d)
#
# d = {k:v for k,v in zip(a, b)}
# print(d)
#
# l = [i for i in range(10)]
# print(l)
# l = (i for i in range(10))
# print(l)
# print(type(l))
# # c = for i in l:print(i)
# # print(c)

# def add(a, b, *, c):
#    return a+b+c
#
# ret = add(1, 2, c=3)
# print(ret)

# def flist(l):
#     l.append(0)
#     print(id(l))
#     print(l)
#
# ll = []
# print(id(ll))
# flist(ll)
# flist(ll)
#
# def fstr(s):
#     s += 'a'
#     print(s)
#
# ss = 'hehe'
# fstr(ss)
# fstr(ss)

#
# def clear(l):
#     l = []
#
# ll = [1,2,3]
# clear(ll)
# print(ll)

# def flist(l=[1]):
#     l.append(1)
#     print(l)
#
# flist()
# flist()

# def print_multi_index(*args):
#     print(type(args), args)
#     for a,b in enumerate(args):
#         print(a, b)
#
# print_multi_index('a', 'b')

# def print_multi_index(**kwargs):
#     print(type(kwargs), kwargs)
#     for a, b in kwargs.items():
#         print('{}: {}'.format(a, b))
#
# print_multi_index(a=1, b=2)

# def print_arg_kwarg(a, *args, **kwargs):
#     print(a)
#
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
#
# print_arg_kwarg('a', 'b', sport='basketball')

# class Solution:
#     def a(self, x):
#         if x < 0:
#             return False
#         if x >=0:
#             s = str(x)
#             beg, end = 0, len(s)-1
#             while beg == end:
#                 beg += 1
#                 end -= 1
#                 return True
#         return True

# class Solution:
#     def a(self, x):
#         if x < 0:
#             return False
#         if x >=0:
#             s = str(x)
#             beg, end = 0, len(s)-1
#             while beg < end:
#                 if s[beg] == s[end]:
#                     beg += 1
#                     end -= 1
#                 else:
#                     return True
#         return True
#
# def test():
#     b = Solution()
#     assert b.a(121) is True
#
# test()

# class Person:
#     Country = 'china'  # class var
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def print_country(cls):
#         print(cls.Country)
#
#     @staticmethod
#     def join_name(first_name, last_name):
#         return last_name + first_name

# class Person:
#     Country = 'china'  # 类变量
#
#     def __int__(self, name):  # 实例变量(实例属性)
#         self.name = name
#
#     def print_name(self):
#         print(self.name)
#
# laowang = Person('laowang')
# laoguo = Person('laoguo')
# laowang.print_name()
# laoguo.print_name()
# # print(laowang.Country)
# # print(laoguo.Country)

import time

def log_time(func):
    def _log(*args, **kwargs):
        beg = time.time()
        res = func(*args, **kwargs)
        print("use time:{}".format(time.time()-beg))
        return res
    return _log

@log_time
def mysleep():
    time.sleep(1)

mysleep()



#!/usr/bin/python

def pailie(s,i):
    if i == len(s):
        print(s)
    else:
        for j in range(i, len(s)):
            s[j], s[i] = s[i], s[j]
            pailie(s, i+1)
            s[j], s[i] = s[i], s[j]

test = 'abc'
s = list(test)
pailie(s, 0)


