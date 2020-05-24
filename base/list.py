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
