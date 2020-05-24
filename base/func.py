#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import os
import string

#函数是带名字带代码块，用于完成具体的工作
#定义函数
def greet():        #def作为关键字，告诉python你要定义一个函数
    print("Hello!") #文档字符串
greet()             #函数调用

#向函数传递信息
def greet(username):    #username是形参
    print("Hello, " +username.title() + "!")
greet('visionguo')      #visionguo是实参，实参是调用函数时传递给函数的信息

#传递实参
#位置实参
def pets_describe(animel_type,pet_name):
    print("\nI have a " + animel_type)
    print("my pet_name's " + pet_name + " animel_type's is a " + animel_type)
pets_describe('husky','ErHa')
pets_describe('dog','lele')

#关键字实参，是传递给函数的名称一值对
def pets_describe(animel_type,pet_name):
    print("\nI have a " + animel_type)
    print("my pet_name's " + pet_name + " animel_type's is a " + animel_type)
pets_describe(pet_name = 'Mimi',animel_type='cat')
pets_describe(animel_type='cat',pet_name = 'Mimi')    #位置调换也无妨

#默认值
#可给每个形参指定默认值
def pets_describe(pet_name,animel_type='dog'):      #先列出没有默认值的形参，再列出有默认值的实参，让python依能够正确地解读位置实参
   print("\nI have a " + animel_type)
   print("my pet_name's " + pet_name + " animel_type's is a " + animel_type)
pets_describe(pet_name = 'haha')
pets_describe('haha')

#等效的函数调用
# 一条名为Willie的小狗
#describe_pet('willie')
#describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
#describe_pet('harry', 'hamster')
#describe_pet(pet_name='harry', animal_type='hamster')
#describe_pet(animal_type='hamster', pet_name='harry')

#返回值
#使用return语句将值返回到调用函数的代码行
def name(xing,ming):
    print('\nname is ' + xing + ming)
name('vision','guo')

#让实参变成可选的
def name(xing,ming,hao=''):     #给实参hao指定一个默认值——空字符串
    name = xing +" " + ming +" "+ hao
    return name.title()

name1=name("vision",'guo')
print(name1)
name2=name("su","xing",'AllenSu')
print(name2)

def name(xing,ming,hao=''):     #给实参hao指定一个默认值——空字符串
    #if hao != '':
    if hao:
        name = xing +" " + ming +" "+ hao
    else:
        name = xing + " " + ming
    return name.title()

name1=name("yi",'er')
print(name1)
name2=name("san","si",'wu')
print(name2)

#返回字典
#函数可返回任何类型的值
def build_person(xing,ming):
    person={'xing':'xing','ming':'ming'}
    return person
person=build_person('vision','guo')
print(person)

def build_person(xing,ming,age=''):         #新增形参age，默认值设置为空字符串
    person={'xing':'xing','ming':'ming'}
    if age:                     #如果函数调用中包含这个形参的值，这个值将存储到字典中
        person['age']=age
    return person
person=build_person('vision','guo',age='25')
print(person)

#结合使用函数和while循环
def name(xing,ming):
    full_name= xing + ' ' + ming
    full_name.title()
    return full_name

full_name=name('allen','su')
print(full_name)

#加if判断
# def name(xing,ming):
#     full_name= xing + ' ' + ming
#     return full_name.title()
#
# while True:
#     f_name = input("f_name:")
#     if f_name == 'q':
#         break
#     l_name = input("l_name:")
#     if l_name == 'q':
#         break
#     full_name=name('f_name','l_name')
# print(full_name)

#传递列表
def greet(names):
    for name in names:
        print("Hello, " + name +"!")
name_list=['tom','tom1','tom2']
greet(name_list)

#在函数中修改列表
uneaten_fruit = ['apple','banana','orange']
eaten_fruit=[]

while uneaten_fruit:
    current_fruit=uneaten_fruit.pop()
    print("uneaten_fruit: " + current_fruit)
    eaten_fruit.append(current_fruit)
for eat_fruit in eaten_fruit:
    print("eat_fruit: "+ eat_fruit)

#传递任意数量的实参
#预先不知道函数需要接受多少个实参，python允许函数从调用语句中收集任意数量的实参

def make_pizza(*toppings):          #形参*toppings中的星号让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
    print("\n make pizza toppings")
    for topping in toppings:
        print("-" + topping)
make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")

#结合使用位置实参和任意数量实参
#如果让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中
def make_pizza(size,*toppings):
    print("\nmaking a " +str(size) +"-inch pizza with the following toppings")
    for topping in toppings:
        print("-" + topping)
make_pizza("12","pepperoni")
make_pizza("16","mushrooms","green peppers","extra cheese")

#使用任意数量的关键字实参
def build_profile(first,last,**user_info):      #创建一个字典，包含用户的一切信息
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('allen','su',
                            location='beijing',
                            field='music',
                            good_friend='bird')
print(user_profile)

#将函数存储在模块中
def make_pizza(size,*toppings):
    print("\nmaking a " +str(size) +"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

#导入特定的函数
from module_name import function_name       #导入模块中的特定函数
from module_name import function_0,function_1   #通过用逗号分隔函数名，导入任意数量的函数

#使用as给函数指定别名
from pizza import make_pizza as mp      #给函数make_pizza()指定了别名mp()

#给模块指定别名
import pizza as p

