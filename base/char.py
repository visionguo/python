#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# -*- coding: <encoding name> -*-

import os
import sys

#运行第一个python程序
print("today is sunny")
def a (b):
    b = "Hello python world!";
    return

print a

#变量
message="today id monday"
print(message)

info="kobe"
print(info)
info="James"
print(info)

def a (message):
    message="Hello world!";
    return 0
def b (message):
    message="Hello";
    return 0

print a
print b

#字符串
#大小写#
name ="hello world!"
print(name.title()) #title是将单词首字母大写。.是让python对变量name执行title()执行对操作。括号是因为方法通常需要额外对信息来完成其工作，这种信息是在括号内提供的，此处函数title（）不需要额外的信息，因此括号后面是空的。
print(name.upper()) #将字符串全部大写
print(name.lower()) #将字符串全部小写

#拼接#
first_name = "拼"
last_name = "接"
full_name = first_name + " " + last_name
print full_name

first_name = "hello"
last_name = "world"
full_name = first_name + " " + last_name

print( "Hi, " + full_name.title() + "!")
message = "Hi, " + full_name.title() + "!" #将消息存储在变量中
print (message)

#空白#
#空白：制表符，换行符，空格，目的是使用空白来组织输出，达成可读性指标
print("python")
print("\tpython") #制表符
print("Languages:\npython\ngo\ndjango") #换行符
print("Languages:\n\tpython\n\tgo\n\tdjango") #先换行再加制表符
print("Languages:\t\npython\n\tgo\n\tdjango")

#删除空白
favorite_language ='python '
favorite_language
print(favorite_language)
favorite_language.rstrip() #删除右端空白
print(favorite_language.rstrip())
favorite_language.lstrip() #删除左端空白
favorite_language.strip()  #删除两端空白

#函数str
age = 25
message = "Happy " + str(age) + "rd Birthday!" #函数str，将非字符串值表示为字符串
print(message)