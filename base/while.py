#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import sys
import os
import string

#函数input()
#name = input("please enter your name:")
#print(name)

#int()来获取数值输入
#age = input("\nHow old are you? ")
#age = int(age)
#print(age >= 18)

#height = input("How tall are you? ")
#height=int(height)

#if (height > 175):
#    print("\nyou are tall enough to visionguo!")
#else:
#    print("you are too lower!")

#求模运算符
print(5%3)

# number = raw_input("Enter a number,and I will tell you if it's even or odd: ")
# number=int(number)
#
# if number % 2 == 0:
#     print("\nThe number " + str(number) + " ,is even!")
# else:
#     print("\nThe number " + str(number) + " ,is odd!")

#while
#for循环 用于针对集合中的每个元素都有一个代码块#
#while循环 不断地运行，直到指定的条件不满足为止#

number = 1
while number <=5:
    print(number)
    number += 1

#让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

#使用标志
#用于判断整个程序是否处于活动状态，这个变量被称为标志
prompt = "\n Tell me something,and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program. "

active = True
#while active:
    # message = input(prompt)
    # if message == 'quit':
    #     active = False
    # else:
    #     print(message)

#使用break退出循环
    # prompt = "\n Enter the city you want to go:"
    # prompt += "\n Enter 'quit' to end the program. "
    #
    # while True:
    #     city = input(prompt)
    #     if city == 'quit':
    #         break
    #     else:
    #         print("I would like to go to " + city())

#在循环中使用continue

current_number=0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 1:
        continue
    print(current_number)

#避免无限循环
x = 1
while x <= 5:
    print(x)
    x += 1

#在列表之间移动元素
unconfirmed_users = ['tom','tom1','tom2']  #未验证的用户列表
confirmed_users = []                       #已验证的用户列表
while unconfirmed_users:
    current_number = unconfirmed_users.pop()
    confirmed_users.append(current_number)

print(confirmed_users)

#删除包含特定值的所有列表元素
pets = ['cat','dag','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#使用用户输入来填充字典
responses = {}           #定义一个空字典
polling_active = True    #设置一个标志，指出调查是否继续

while polling_active:
#     name = input('\n Please input your name:')
#     response = input('\n what color do you like?')

    responses[name] = response    #将答卷存储在字典中

#    repeat = input('\n Is there anyone else to participate in?(yes/no)')    #是否还有人要参与
    if repeat == 'no':
        polling_active = False

print("\n --- poll results ---")
for name,response in responses.items():
    print(name + "would like " + response)
