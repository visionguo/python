#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# -*- coding: <encoding name> -*-

"""
Test_code
"""

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# def get_formatted_name(first,final):
#     full_name = first +' ' +final
#     return full_name.title()

# print("Enter 'q' to quit.")
# while True:
#     first = raw_input("\nEnter the first_name:")
#     if first == 'q':
#         break
#     final = raw_input("\nEnter the final_name:")
#     if final == 'q':
#         break
#     formatted_name = get_formatted_name(first,final)
#     print("\tNeatly formatted name: " +formatted_name + '!')

#单元测试和测试用例
#单元测试用于核实函数的某个方面没有问题
#测试用例是一组单元测试

#可通过的测试
# import unittest     #导入模块unittest
# #from name_function import get_formatted_name   #导入测试的函数get_formatted_name
#
# class NamesTestCase(unittest.TestCase):     #创建NamesTestCase的类，包含一系列针对get_formatted_name()的单元测试
#     def test_first_final_name(self):
#         formatted_name = get_formatted_name('vision','guo')     #调用函数并将值存储
#         self.assertEqual(formatted_name,'Vision Guo')           #断言方法用来核实得到的结果是否与期望的结果一致
#
# unittest.main()

# .                     #有一个测试通过了
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s  #指出python运行了一个测试，和消耗时间
#
# OK                    #该测试用例中的所有单元测试都通过了

#不能通过的测试
# def get_formatted_name(first,middle,final):
#     full_name = first +' ' +middle +' ' +final
#     return full_name.title()
#
# import unittest
#
# class NamesTestCase(unittest.TestCase):
#     def test_first_final_name(self):
#         formatted_name = get_formatted_name('vision','guo')
#         self.assertEqual(formatted_name,'Vision Guo')
#
# unittest.main()

#测试未通过时怎么办
# def get_formatted_name(first,final,middle=''):
#     if middle:
#         full_name = first + ' ' + midlle + ' ' + final
#     else:
#         full_name = first + ' ' + final
#     return full_name.title()
#
# import unittest
#
# class NamesTestCase(unittest.TestCase):
#     def test_first_final_name(self):
#         formatted_name = get_formatted_name('vision','guo')
#         self.assertEqual(formatted_name,'Vision Guo')
#
# unittest.main()

#添加新测试
# def get_formatted_name(first,final,middle=''):
#     if middle:
#         full_name = first + ' ' + middle + ' ' + final
#     else:
#         full_name = first + ' ' + final
#     return full_name.title()
# import unittest
# #from name_function import get_formatted_name
#
# class NameTestCase(unittest.TestCase):
#     def test_first_final_name(self):
#         formatted_name = get_formatted_name('allen','su')
#         self.assertEqual(formatted_name,'Allen Su')
#     def test_first_middle_final_name(self):
#         formatted_name =get_formatted_name('lin','jun','jie')
#         self.assertEqual(formatted_name,'Lin Jie Jun')
# unittest.main()

#测试类
# class AnonymousSurvey():            #收集匿名调查问卷的答案
#     def __init__(self,question):    #存储一个问题，并为存储答案做准备
#         self.question = question
#         self.responses = []         #空列表，用于存储答案
#     def show_question(self):        #显示调查问卷
#         print(question)
#
#     def store_response(self,new_response):  #存储单份调查答卷
#         self.responses.append(new_response)
#
#     def show_results(self):         #显示收集到的所有答卷
#         print("Survey results:")
#         for response in responses:
#             print('-' + response)
#
# from survey import AnonymousSurvey
# responses = []
# question = "what language did you first learn to spark?"    #定义一个问题，并创建一个表示调查的AnonymousSurvey对象
# my_survey = AnonymousSurvey(question)
#
# my_survey.show_question()
# print("Enter 'q' to quit")
# while True:
#     response =raw_input("Language:")
#     if response == 'q':
#         break
#     my_survey.store_response(response)
#
# print("\nThank you to everyone who participated in this survey!")
# my_survey.show_results()

#测试AnonymousSurvey类
# import unittest                         #导入unittest模块
# #from survey import AnonymousSurvey     #导入要测试的类AnonymousSurvey
# class AnonymousSurvey():            #收集匿名调查问卷的答案
#     def __init__(self,question):    #存储一个问题，并为存储答案做准备
#         self.question = question
#         self.responses = []         #空列表，用于存储答案
#     def show_question(self):        #显示调查问卷
#         print(question)
#
#     def store_response(self,new_response):  #存储单份调查答卷
#         self.responses.append(new_response)
#
#     def show_results(self):         #显示收集到的所有答卷
#         print("Survey results:")
#         for response in responses:
#             print('-' + response)
#
# class TestAnonmyousSurvey(unittest.TestCase):   #将要测试用例命名为TestAnonmyousSurvey，也继承了unittest.TestCase
#     """针对AnonmyousSurvey类的测试"""
#     def test_store_single_response(self):
#         """测试单个答案会被妥善地存储"""
#         question ="What language did you first learn to speak?"
#         my_survey=AnonymousSurvey(question)
#         my_survey.store_response('chinese')     #创建实例my_survey使用方法store_response()存储单个答案chinese
#         self.assertIn('chinese',my_survey.responses)
#     def test_store_three_responses(self):
#         """测试三个答案会被妥善地存储"""
#         question="What language do you like?"
#         my_survey =AnonymousSurvey(question)
#         responses=['python','go','shell']
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response,my_survey.responses)
#
# unittest.main()

#方法setUp()
import unittest                         #导入unittest模块
#from survey import AnonymousSurvey     #导入要测试的类AnonymousSurvey
class AnonymousSurvey():            #收集匿名调查问卷的答案
    def __init__(self,question):    #存储一个问题，并为存储答案做准备
        self.question = question
        self.responses = []         #空列表，用于存储答案
    def show_question(self):        #显示调查问卷
        print(question)

    def store_response(self,new_response):  #存储单份调查答卷
        self.responses.append(new_response)

    def show_results(self):         #显示收集到的所有答卷
        print("Survey results:")
        for response in responses:
            print('-' + response)

responses = []
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question ="What language do you like?"
        self.my_survey=AnonymousSurvey(question)            #创建一个调查对象
        self.responses= ['English','Spanish','Mandarin']    #创建一个答案列表
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):       #测试三个答案会被妥善地存储
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()
#运行测试用例时，每完成一个单元测试，Python都打印一个字符:测试通过时打印一个句点;测试引发错误时打印一个E ;测试导致断言失败时打印一个F 。

"""
char
"""

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

"""
class
"""

import sys
import os
import string

#根据类来创建对象被成为实例化
#创建和使用类
class Dog():        #一次模拟小狗的简单尝试，首字母大写的名称指的是类
    def __init__(self,name,age):        #初始化属性name和age，类中的函数称为方法。__init__ 每当你根据Dog类创建新实例时，python会自动运行它
        self.name = name                #self这个形参放在其它形参的前面
        self.age  = age                 #以self为前缀的变量都可供类中的所有方法使用，还可通过类的任何实例来访问这些变量
        #可通过实例访问的变量称为属性
    def sit(self):                      #每个与类相关联的方法调用都自动传递实参self,它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
                                        #创建Dog实例时，python将调用Dog类的方法__init__().将通过实参向Dog()传递名字和年龄；self会自动传递，无需传递它
                                        #根据Dog类创建实例时，只需给最后两个形参提供值
        print(self.name.title() +" is now sitting.")    #模拟小狗被命令坐下
    def roll_over(self):
        print(self.name.title() + " rolled over.")      #模拟小狗在打滚

#在python2.7中创建类
#class ClassName(object):
#    --snip--

#根据类创建实例,类是如何创建实例的说明
my_dog = Dog('lele',6)  #调用__init__(),将创建一个表示特定小狗的实例，使用lele和6来设置属性name和age
print("My Dog's name is " + my_dog.name.title() + ".")
print("My dog is " +str(my_dog.age) + " year old.")
print(my_dog.name)  #句点表示法，访问my_dog的属性name的值

#调用方法
my_dog = Dog('haha',8)
my_dog.sit()
my_dog.roll_over()

#创建多个实例
my_dog=Dog('beibei','3')
your_dog=Dog('huanhuan','5')

print("\nMy Dog's name is " + my_dog.name.title() + ".")
print("My dog is " +str(my_dog.age) + " year old.")
my_dog.sit()

print("\nMy Dog's name is " + your_dog.name.title() + ".")
print("My dog is " +str(your_dog.age) + " year old.")
your_dog.sit()

#使用类和实例
#car类
class Car():
    def __init__(self,make,model,year):     #初始化描述汽车的属性
        self.make=make      #获取存储在形参make中的值，并将其存储到变量make中
        self.model=model
        self.year=year
    def get_descriptive_name(self):     #返回整洁的描述性信息
        long_name = str(self.year) +" " + self.make + " " +self.model
        return long_name.title()
my_car =Car('2018','audi','a4l')
print(my_car.get_descriptive_name())

#给属性指定默认值
class Car():
    def __init__(self,make,year,model):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading='0'
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    def read_odometer(self):
        print("\nThis car has " + str(self.odometer_reading) +" miles on it")
my_new_car=Car('audi','2018','audi')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#修改属性的值
#直接修改属性的值
class Car():
    def __init__(self,make,year,model):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading='0'
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    def read_odometer(self):
        print("\nThis car has " + str(self.odometer_reading) +" miles on it")
my_new_car=Car('audi','2018','audi')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#通过方法修改属性的值
class Car():
    def __init__(self,make,year,model):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading='0'

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("\nThis car has " + str(self.odometer_reading) + " miles on it")

    my_new_car = Car('audi', '2018', 'audi')
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
my_new_car=Car('audi','2018','audi')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(30)
my_new_car.read_odometer()

#通过方法对属性的值进行递增
class Car():
    def __init__(self,make,year,model):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading='0'

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("\nThis car has " + str(self.odometer_reading) + " miles on it")

    my_new_car = Car('audi', '2018', 'audi')
    def update_odometer(self,mileage):
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_used_car=Car("bmx",'2018','x5')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(20000)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#继承
#子类的方法 __init__()
class Basketball_teams(object):     #或者 class Group(Basketball_teams,object):
    def __init__(self,name,city,player_number):
        self.name=name
        self.city=city
        self.player_number=player_number
        self.champion=0
    def get_descriptive_name(self):
        basketball_team=self.city +" " + self.name +" "+"hava " +str(self.player_number) +" player"
        return basketball_team.title()
    def won_champion(self):
        print("They have won " +str(champion) +" champions!")

    def update_champion(self,time):
        if time >=self.champion:
            self.champion=time
        else:
            print("you can not")
    def increment_champion(self,time):
        self.champion += time

#class Group(Basketball_teams):     #出错语句，这是2.7写法
class Group(Basketball_teams):      #定义子类，父类必须包含在当前文件中
    def __init__(self,name,city,player_number):
        #super().__init__(name, city, player_number)    #出错语句，这是2.7写法
        super(Group,self).__init__(name,city,player_number)       #初始化父类的属性，super将父类和子类关联起来
        self.team_color = 'golden'      ##给子类定义属性和方法
    def describe_team_color(self):
        print("This backetball team color is " + self.team_color)
my_love = Group('leaker','san Francisco',13)
print(my_love.get_descriptive_name())
my_love.describe_team_color()

#将实例用作属性
class Basketball_teams(object):
    def __init__(self,name,city,player_number):
        self.name=name
        self.city=city
        self.player_number=player_number
        self.champion=0
    def get_descriptive_name(self):
        basketball_team=self.city +" " + self.name +" "+"hava " +str(self.player_number) +" player"
        return basketball_team.title()
    def won_champion(self):
        print("They have won " +str(champion) +" champions!")

    def update_champion(self,time):
        if time >=self.champion:
            self.champion=time
        else:
            print("you can not")
    def increment_champion(self,time):
        self.champion += time

class Spectator():      #新类，没有继承任何类
    def __init__(self,spectator_num=180000):    #除self外，有另一个形参spectator_num
        self.spectator_num=spectator_num        #初始化观众的属性
    def describe_spectator(self):               #方法describe_spectator也移到这个类中
        print("\nThis gymnasium have " + str(self.spectator_num) +" spectator!")
class Group(Basketball_teams):
    def __init__(self,name,city,player_number):     #初始化父类的属性，再初始化spectator特有的属性
        super(Group, self).__init__(name, city, player_number)
        self.spectator_num = Spectator()        #添加一个名为self.spectator_num的属性，让python创建一个新的Spectator实例，并将该实例存储在属性self.spectator_num中
                                                #因此每当方法 __init__（）被调用时，都将执行该操作，每个Group实例都包含一个自动创建的Spectator的实例
my_love = Group('leaker','san Francisco',13)    #创建一个球队，将其存储在变量my_love中，要描述球队可容纳的观众时，需要使用Spectator的属性spectator
print(my_love.get_descriptive_name())
my_love.spectator_num.describe_spectator()      #让python在实例my_love中查找属性spectator_num，并对存储在该属性中的Spectator实例调用方法describe_spectator()

#导入类
#给类添加功能，文件变得很长，即使使用继承也如此，python允许将类存储在模块中，然后在主程序中导入所需的模块
#导入单个类
class Lunch():
    def __init__(self,time,type,expense):   #初始化描述午餐的属性
        self.time=time
        self.type=type
        self.expense=expense
        self.parter=1
    def get_describe_name(self):            #返回整洁的描述性名称
        long_name=str(self.time) + ' ' + self.expense + ' ' +self.type
        return long_name.title()
    def read_parter(self):
        print("I have " +str(self.parter) + " ")    #指出吃午餐同行的伙伴数量
    def update_num(self,times):     #将人数设定为特定的值，拒绝更改
        if times > self.parter:
            self.parter=times
        else:
            print("you can't change")
    def increment_parter(self,times):
        self.parter += times

#from lunch import Lunch     #python打开模块lunch,并导入其中的Lunch类，

my_love = Lunch('12','steamed bread','12')
print(my_love.get_describe_name())

my_love.parter = 2
my_love.read_parter()

#在一个模块中存储多个类
class Dinner(object):
    def __init__(self,time,type,expense):   #初始化描述午餐的属性
        self.time=time
        self.type=type
        self.expense=expense
        self.parter=1
    def get_descriptive_name(self):
        long_name = str(self.time) + ' ' +self.type + ' ' + self.expense
class Soup():       #描述汤
    def __init__(self,litre=0.3):
        self.litre=litre
    def describe_name(self):
        print("This soup has " + str(self.litre) + "L")
    def get_range(self):
        if self.litre == 0.3:
            range == 3
        elif self.litre == 0.4:
            range == 4
    expense = "This soup spend " + str(range)
    expense += "litre on a full charge"
    print(expense)

class Money(Dinner):
    def __init__(self,time,type,expense):
        super(Money,self).__init__(time,type,expense)
        self.soup=Soup()
#for dinner import Money
my_dinner = Money('18','noodle','10')
print(my_dinner.get_descriptive_name())
my_dinner.soup.describe_name()
my_dinner.soup.get_range()

#从一个模块中导入多个类
# from dinner import Dinner,Money
# friday =Dinner('17','rice','18')
# print(friday.get_descriptive_name())
#
# saturday =Money('19','biscuit','10')
# print(saturday.get_descriptivee_name())

#导入整个模块
# import dinner     #导入整个模块
#
# monday=dinner.Dinner('13','pizza','30')       #用句点表示访问需要的类
# print(monday.get_descriptive_name())
#
# tuesday=dinner.Money('14','kfc','20')
# print(tuesday.get_descriptive_name())

#导入模块中的所有类
#from module_name import *
#没有明确指出使用模块中的哪些类,不推荐

#在一个模块中导入另一个模块

"""
dic
"""

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#字典
feature = {'color':'red','points':100}
print(feature['color'])
print(feature['points'])

#添加键值对，字典是一种动态结构，可随时在其中添加键值对
feature = {'color':'red','points':100}
print(feature)
feature['height']=175
feature['weight']=150
print(feature)

#修改
feature = {'color':'red','points':100}
feature['color']='green'
print(feature)

#删除
feature = {'color':'red','points':100}
del feature['points']
print(feature)

#由类似对象组成的字典
favourite_languages={
    'python':'python',
    'go':'go',
    'c':'c',
}
print(favourite_languages['c'].title())

#遍历字典
favourite_languages={
    'python':'python',
    'go':'go',
    'c':'c',
}
for k,v in favourite_languages.items(): #items返回一个键-值对列表
    print("\nkey: " + k)
    print("value: " + v)

#遍历字典中的所有键
favourite_sports={
    'basketball':'basketball',
    'football':'football',
    'badminton':'badminton',
}
for k in favourite_sports.keys():
    print(k.title())

for v in favourite_sports.values():
    print(v)

favourite_colors={
    'red':'red',
    'green':'green',
    'blue':'blue'
    ,
}
keys=['red','blue']
for color in favourite_colors.keys():
    print(color.title())
    if color in keys:
        print ( "Hi ," + color.title() + ", you favourite_color is " + favourite_colors[color].title())

#按顺序遍历字典中的所有键#
favourite_colors={
    'red':'red',
    'green':'green',
    'blue':'blue'
    ,
}

for color in sorted(favourite_colors.keys()):
    print(color.title())

#遍历字典中的所有值#
#set:剔除重复项#
favourite_colors={
    'red':'red',
    'green':'green',
    'blue':'blue',
    'visionguo':'red',
}

for color in set(favourite_colors.values()):
    print(color.title())

#嵌套
visionguo={'favourite_colors':'red','favourite_languages':'python','favourite_sports':'basketball'}
visionguo1={'favourite_colors':'green','favourite_languages':'go','favourite_sports':'football'}
visionguo2={'favourite_colors':'yellow','favourite_languages':'shell','favourite_sports':'badminton'}

favourites = [visionguo,visionguo1,visionguo2]
for favourite in favourites:
    print(favourite)

favourites = []
for number in range(30):
    visionguo={'favourite_colors':'red','favourite_languages':'python','favourite_sports':'football'}
    favourites.append(visionguo)
for favourite in favourites[0:3]:
    if favourite['favourite_colors']=='red':
        favourite['favourite_colors'] = 'black'
        favourite['favourite_languages'] ='c'
        favourite['favourite_sports'] = 'badminton'
    elif favourite['favourite_colors']=='black':
        favourite['favourite_colors'] = 'white'
        favourite['favourite_languages'] ='java'
        favourite['favourite_sports'] = 'tennis'
for favourite in favourites[0:5]:
    print(favourite)
print(str(len(favourites)))

#在字典中存储列表
visionguo = {'favourite_color':'red','favourite_sports':['basketball','football']}
for favourite_sport in visionguo['favourite_sports']:
    print(favourite_sport)

favourite_languages = {'vision':['python','go'],'allen':['java'],'tom':['c++','c','c#']}
for name,languages in favourite_languages.items():
    print("\n" + name.title() + " favourite language is:")
    for language in languages:
        print(language.title())

#在字典中存储字典
users = {
    'visionguo' : {
    'xing': 'vision',
    'ming': 'guo',
    'location': 'xian',
    },
    'allensu' : {
    'xing': 'allen',
    'ming': 'su',
    'location': 'beijing',
},
}

for username,user_info in users.items():
    print("\n" + "username: " + username.title())
    fullname = user_info['xing'] + " " + user_info['ming']
    location = user_info['location']

    print("\tFullname : " + fullname.title())
    print("\tLocation : " + location.title())

"""
file_Traceback
"""

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#从文件中读取数据
with open('digits.txt') as file:
    contents = file.read()
 #   print(contents)            #read()到达文件末尾时返回一个空字符串
    print(contents.rstrip())    #删字符串末尾的空白

#逐行读取
filename='digits.txt'

with open('digits.txt') as file:
    for line in file:
        print(line.rstrip())

#创建一个包含文件各行内容的列表
filename = 'digits.txt'
with open(filename) as file:
    lines = file.readlines()    #readlines()从文件中读取每一行，并将其存储在一个列表中

for line in lines:
    print(line.rstrip())

#使用文件的内容
filename='digits.txt'
with open(filename) as file:
    lines = file.readlines()

string = ''
for line in lines:
    string += line.rstrip()
print(string)
print(len(string))

#包含一百万位的大型文件
filename='digits.txt'
with open(filename) as file:
    lines = file.readlines()

string = ''
for line in lines:
    string += line.rstrip()
print(string[:10] + "...")
print(len(string))

#写入文件
filename = 'programming.txt'
with open(filename,'w') as file:
    file.write("Yeah,I love programming.")

#验证写入文件是否正常
filename = 'programming.txt'
with open('programming.txt') as files:
    for file in files:
        print(file)

#写入多行
filename ='programming.txt'

with open(filename,'w') as file:
    file.write('I love programming.\n')     #换行符\n，每个字符独占一行
    file.write('I like moving.\n')
filename = 'programming.txt'

with open(filename,'a') as file:
    file.write('I love creating apps that can run in a browser.\n')     #a,追加，不会覆盖原文件
with open('programming.txt') as files:
    for file in files:
        print(file)

#异常
#处理ZeroDivisionError异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")      #看到友好的错误消息，而不是traceback

#使用异常避免崩溃
#捕获错误后程序将继续运行的示例
# print("Give me two numbers, and I'll divide them.")
# print("Please 'q' to quit.")

# while True:
#     first_num=input("enter first_num:")
#     if first_num == 'q':
#        break
#
#     final_num=input("enter first_num:")
#     if final_num == 'q':
#        break
#     answer = int(first_num) / int(final_num)
#     print("The answer is:" + str(answer))

#else代码块
# print("Give me two numbers, and I'll divide them.")
# print("Please 'q' to quit.")
#
# while True:
#     first_number=input("enter first_number:")
#     if first_number == 'q':
#         break
#     second_number=input("enter second_number:")
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero")
#     else:
#         print(answer)

#处理FileNotFoundError异常
# filename = 'notexist.txt'
# with open(vision.txt) as file:
#     contents = file.read()

filename='notexist.txt'
try:        #这个异常是open引起的，try语句放到open()之前
    with open('noexist.txt') as file:
        contents = file.read()
#except FileNotFoundError:  #python3使用的文本不存在异常处理方法
except IOError:             #python2.7
    print("Sorry,The file " +filename +" doesn't exist.")

#分析文本
filename='alice.txt'
try:
    with open(filename) as file:
        contents=file.read()
except IOError:
    message="Sorry,The file " + filename + " doesn't exist."
    print(message)
else:
    words = contents.split()
    num_words =len(words)
    info ="The file "+ filename +" has about "  +str(num_words) +" words"
    print(info)

#使用多个文件
def count_words(filename):      #计算一个文件大致包含多少个单词
    try:
        with open(filename) as file:
            contents = file.read()
    except IOError:
        message = "Sorry,The file " + filename + " doesn't exist."
        print(message)
    else:       #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        info = "\nThe file " + filename + " has about " + str(num_words) + " words"
        print(info)
filename='alice.txt'
count_words(filename)

#循环遍历
def count_words(filename):      #计算一个文件大致包含多少个单词
    try:
        with open(filename) as file:
            contents = file.read()
    except IOError:
        #message = "Sorry,The file " + filename + " doesn't exist."
        #print(message)
        pass    #失败时一声不吭
    else:       #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        info = "\nThe file " + filename + " has about " + str(num_words) + " words"
        print(info)
filenames=['alice.txt','Animals.txt','Months.txt','not.txt']
for filename in filenames:
    count_words(filename)

#存储数据
import json
numbers = [1,3,5,7,9]
filename='numbers.json'             #数字列表存储到其中的文件的名称
with open(filename,'w') as file:    #写入模式打开文件，让json能够将数据写入其中
    json.dump(numbers,file)         #使用函数json.dump()将数字列表存储到文件numbers.json中

#使用json.load()将这个列表读取到内存中
import json
filename ='numbers.json'
with open(filename) as file:
    numbers=json.load(file)
print(numbers)

#保存和读取用户生成的数据
# import json
# username=input("What's your name:")
# filename='username.json'
# with open(filename,'w') as file:
#     json.dump(username,file)        #将用户名和一个文件对象传递给它
#     print("Welcome, " +str(username))
#
# #向其名字被存储的用户发出问候
# import json
# filename ='username.json'
# with open(filename) as file:
#     username=json.load(file)
#     print("Welcome back, " +str(username))

#remember_me.py
import json     #如果以前存储了用户名，就加载它，否则，就提示用户输入用户名并加载它
filename='username.json'
try:
    with open(filename) as file:    #尝试打开文件username.json
        username =json.load(file)   #如果文件存在，就将其中的用户名读取到内存中
except IOError:
    username = input("What is your name?")
    with open(filename,'w') as file:
        json.dump(username,file)    #存储该用户名
        print("come back, " +str(username))
else:
    print("Back, " +str(username))

#重构
#代码能够正确地运行，但可做进一步的改造，将代码划分为一系列完成具体工作的函数，这过程称为重构

import json
def greet_user():
    filename = 'username.json'  #问候用户，并指出其名字
    try:
        with open(filename) as file:
            username=json.load(file)
    except IOError:
        username =input("What's your name?")
        with open(filename,'w') as file:
            json.dump(username,file)
            print("we'll remember you when you come back, " +str(username))
    else:
        print("Hi, "+str(username) +" you are back!")
greet_user()

#将获取存储的用户名的代码转移到另一个函数中
import json
def get_stored_username():
    filename = 'username.json'      #如果存储了用户名，就获取它
    try:
        with open(filename) as file:
            username = json.load(file)
    except IOError:         #如果文件username.json不存在，这个函数就返回None
        return None
    else:
        return username

def greet_user():        #问候用户，并指出其名字
    username = get_stored_username()
    if username:        #如果成功地获取了用户名，就打印一条欢迎用户回来的消息
        print("\nYeah, Welcome back, " +str(username))
    else:
        username=input("What is your name?")    #否则就提示用户输入用户名
        filename='username.json'
        with open(filename,'w') as file:
            json.dump(username,file)
            print("We will remember you when you come back, " +username)
greet_user()

#将greet_user()中的另一个代码块提取出来，将没有存储用户名时提示用户输入的代码放在一个独立的函数中
import json
def get_stored_usernamee():     #只负责获取存储的用户名
    filename = 'username.json'
    try:
        with open(filename) as file:
            username =json,load(file)
    except IOError:
        return None
    else:
        return username

def get_new_username():         #负责获取并存储新用户的用户名
    username=input("What is your name?")    #提示用户输入用户名
    filename = 'username.json'
    with open(filename,'w') as file:
        json.dump(username,file)
    return username

def greet_user():
    username = get_stored_username()    #问候用户，并指出其名字
    if username:
        print("Wel back, " + str(username) + "!")
    else:
        username =get_stored_username()
        print("We will remember you when you come back, " + str(username) + "!")
greet_user()

"""
func
"""

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

"""
if
"""
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

"""
list
"""

#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#list 一系列按特定顺序排列的元素组成
#展示
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
print(fruit)
print(fruit[0])         #索引取值
print(fruit[-1])        #最后一个值
print(fruit[0].title())
message = "My favourite fruit is " + fruit[0].title() + "."
print(message)

#修改
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
print(fruit[0])
fruit[0] = "Apple"
print(fruit[0])

#append,在列表末尾添加
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
print(fruit[-1])
fruit.append('lichee')
print(fruit[-1])

#insert,插入，
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
print(fruit[2])
fruit.insert(3,'durian')
print(fruit)

#del,删除,和pop的区别：del是从列表中删除一个元素，且不再以任何方式使用它
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
fruit.insert(0,'test')
print(fruit[0])
del fruit[0]
print(fruit[0])

#pop,删除列表末尾的元素相当于弹出栈顶元素，和del的区别：pop在删除元素后还能继续使用它
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
fruit.append('test')
print(fruit)
pop_fruit=fruit.pop()
print(fruit)
print(pop_fruit) #删除的test值被存储在pop_fruit这个变量中，并可以进行访问
#pop()删除列表中任何位置的元素#
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
favourite_fruit=fruit.pop(2)
print("My favourite fruit is " + favourite_fruit + ".")
print(fruit)

#remove，只删除第一个制定的值，如果要删除的值出现多次，需要循环来判断，然后删除
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
fruit.remove("grape")
print(fruit)
#可以接着使用删除的值#
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
sour = fruit[4]
fruit.remove(sour)
print(fruit)

#sort()对列表进行永久性排序
cars = ['bmw','audi','toyota']
cars.sort()                     #按字母顺序排序
print(cars)

cars = ['bmw','audi','toyota']
cars.sort(reverse=True)         #按字母相反的顺序排序
print(cars)

#sorted()对列表进行临时排序
cars = ['bmw','audi','toyota']
print("Here is the original list:")
print(cars)

print("\nHere is the original list:")
print(sorted(cars))

print("Here is the original list again:")
print(cars)

#reverse 倒着打印列表
cars = ['bmw','audi','toyota']
print(cars)

cars.reverse()                  #反转列表元素的排列顺序，不是按与字母顺序相反的顺序排列列表元素
print(cars)

cars.reverse()                  #再次反转
print(cars)

#len()确定列表的长度
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
print(len(fruit))

#遍历整个列表
fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
for fruitage in fruit:      #从fruit列表中取值，并将其存储在变量fruitage中
    print(fruitage)

fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
for fruitage in fruit:
    print(fruitage.title() + ", It is so goluptious!")

fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
for fruitage in fruit:
    print(fruitage.title() + ", It is so goluptious!")
    print("Yeah,Eating fruit is good for your health ,Include " + fruitage.title() + ".\n")

fruit = ['apple','banana','cherry','grape','lemon','mongo','orange','peach','pear','strawberry','watermelon']
for fruitage in fruit:
    print(fruitage.title() + ", It is so goluptious!")
    print("Yeah,Eating fruit is good for your health ,Include " + fruitage.title() + ".\n")
print("I like to eat fruit everyday")

#函数range()
for age in range(20,25):
    print(age)

#range()创建数字列表
for age in list(range(1,11)):
    print(age)

age=list(range(1,11))
print age

age=list(range(1,11,2))  #指定步长
print age

ages=[]
for age in range(11,21):
    ages.append(age**2)
print(ages)

digit=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print max(digit)
print min(digit)
print sum(digit)

#列表解析
ages = [age**2 for age in range(1,11)]
print(ages)

#切片
sports = ['basketball','football','badminton','tennis','table tennis']
print(sports[0:2])
print(sports[:3])
print(sports[2:])
print(sports[-2:])

#遍历切片#
sports = ['basketball','football','badminton','tennis','table tennis']
for sport in sports[:2]:
    print(sport.title())

#复制列表#
sports = ['basketball','football','badminton','tennis','table tennis']
sport = sports[:]

print(sports)
print(sport)

#将sports的副本存储到sport
sports = ['basketball','football','badminton','tennis','table tennis']
sport = sports[:]

sports.append('volleyball')

sport.append('cycling')
print(sports)
print(sport)

#将sports赋给sport，而不是将sports的副本存储到sport
sports = ['basketball','football','badminton','tennis','table tennis']
sport = sports                  #让python将新变量sport关联到包含在sports中的列表，因此这两个列表都指向同一个列表

sports.append('volleyball')

sport.append('cycling')
print(sports)
print(sport)

#列表适合于存储在程序运行期间可能变化的数据集，列表是可以修改的，#

#元组
#不可变的列表#
age = (23,25)
print(age[0])
print(age[1])
print(age[-1])

#遍历元组
ages = (24,25)
for age in ages:
    print(age)

#修改元组变量
ages = (18,19)
for age in ages:
    print(age)

ages = (20,24)
for age in ages:
    print(age)

"""
while
"""
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
