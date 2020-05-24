#!/usr/bin/env python3
# -*- coding:utf-8 -*-

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


