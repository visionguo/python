#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#if判断
cars = ['bmw','audi','byd','toyata']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#条件测试
#字符串比较#
car = 'audi'    #赋值
car == 'audi'   #比较

#数字比较#
age = 18    #赋值
age == 18   #比较

#and
age = 18
name = 'vision'
if age == 18 and name == 'vision':
    print(age)
else:
    print(name)

#or
age = 25
name = 'guo'
if age > 25 or name == 'guo':
    print(age)
else:
    print(name)

#in
color = ['red','green','yellow','blue','black','white','orange']
if 'red' in color:
    print('red')
else:
    print('none')

#not in
color = ['red','green','yellow','blue','black','white','orange']
if 'gray' not in color:
    print('gray')
else:
    print('none')

#if-elif-else
age = 18
if age <10:
    print('10')
elif age < 25:
    print('25')
else:
    print(age)

#多个elif#
age = 30
if age <10:
    age=10
elif age < 40:
    age =40
elif age < 50:
    age=50
else:
    print(age)
print ("your age is: " + str(age) + '.')

#多个if,运行多个代码块
football_team = ['GoalKeeper','SideBack','MiddleField','WingForward']
if 'GoalKeeper' in football_team:
    print('GoalKeeper')
if 'WingForward' in football_team:
    print('WingForward')

#确认列表不为空
football_teams = []

if football_teams:
    for football_team in football_teams:
        print("football_team")
else:
    print("none")

colors=['red','green','blue']
lists=['clothes','paper','ball','red']

for color in colors:
    if color in lists:
        print(color + " in lists")
    else:
        print(color + " is not in lists")

