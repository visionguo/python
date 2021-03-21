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
110_practice
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/02/21 09:57
# @Author  : Abel

"""
1、一行代码实现1-100之和
"""
a = sum(range(0,101))
print(a)

"""
2、一个函数内部修改全局变量
"""
a = 5
def func():
    global a
    a = 4
func()

print(a)

"""
3、字典如何删除和合并两个字典
"""
dic = {"name":"Abel","age":26}
del dic["name"]                 #删除键
print(dic)
dic2 = {"name":"messi"}
dic.update(dic2)                #update合并字典
print(dic)

"""
4、列表去重
"""
listx = [1,2,3,3,4,5]
a = set(listx)
print(a)

'''
*args、**kwargs区别
*args是用来发送一个非键值对的可变数量的参数列表列表给一个函数；不知道向函数传递多少参数时，比如列表或元组
'''
def demo(args_f,*args_v):
    print args_f
    for x in args_v:
        print x
a = demo('a','b','c','d')
print(a)

'''
**kwargs允许你将不定长度的键值对，作为参数传递给一个函数，想要在一个函数里处理带名字的参数，不知道该传递多少关键字参数时，使用**kwargs来收集关键字参数
'''
def demo1(**args_v):
    for k,v in args_v.items():
        print(k,v)
b = demo1(name='Abel')
print(b)

"""
5、面向对象中 __new__ 和 __init__区别
__init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数
__new__至少要有一个参数cls，代表当前类，此参数在实例化时由python解释器自动识别
__new___必须要有返回值，可以return父类 __new__出来的实例，或直接是object的__new__出来的实例
__init__不需要返回值，__init__有一个参数self，就是这个__new__返回的实例
如果__new__创建的是当前类的实例，会自动调用__init__函数
"""
'''
1、__init__:对象初始化方法
2、__new__:创建对象时侯执行的方法，单列模式会用到
3、__str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，就会打印从这个方法中return的数据
4、__del__:删除对象执行的方法
'''
class Bike:
    def __init__(self, newWheelNum, newColor):  #__init__方法自动被调用，可以创建对象接收参数
        self.wheelNum = newWheelNum
        self.color = newColor
    def move(self):
        print("移动")
#创建对象
BMW = Bike(2,'white')
print('车轮子数量为:%d'%BMW.wheelNum)
print('车的颜色为:%s'%BMW.color)

"""
6、with
按照常规的f.open写法，需要try,except,finally做异常判断，且最终都会执行finally f.close()关闭文件，with能代替这一步
"""
f=open("./1.txt","wb")
try:
    f.write("hello world!")
except:
    pass
finally:
    f.close()

"""
7、map
"""
listx = [1,2,3,4,5]
def func(x):
    return x**2

result = map(func,listx)
result = [i for i in result if i > 10]
print(result)

"""
8、python生成
随机整数：random.randint(a,b),生成区间内的整数
随机小数：numpy库，利用np.random.randn(5)生成5个随机小数
0 - 1随机小数：random.random(),括号中不传参
"""
import random
import numpy as np
result = random.randint(10,20)
result1 = np.random.randn(5)
result2 = random.random()
print("正整数",result)
print("5个随机小数",result1)
print("0-1随机小数",result2)

'''0-100随机数'''
res1 = 100*random.random()
res2 = random.choice(range(0,101))
res3 = random.randint(1,100)
print(res1)
print(res2)
print(res3)

"""
9、去除空格
"""
str9 = "hello world yeah"
res = str9.replace(" ","")
print(res)

list9 = str9.split(" ")
res = "".join(list9)
print(res)

"""
10、断言：assert
"""
a = 3
assert(a>1)
print("断言成功，程序继续向下执行")

b = 4
assert(b>1)
print("断言失败，程序报错")

"""
11、可变数据类型和不可变数据类型
"""
a = 3
b = 3
c=id(a)
print(c)
d=id(b)
print(d)
'''
不可变数据类型：数值型、字符串型string和元组tuple
不允许变量的值发生变化 ，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象(一个地址)
'''

a = [1,2]
b = [1,2]
c=id(a)
print(c)
d=id(b)
print(d)

'''
可变数据类型：列表list和字典dict
允许变量的值发生变化，即如果对变量进行append、+=等操作后，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，
不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象
'''

"""
12、去重并排序
"""
s = 'aaacccbbb'
s = set(s)
s = list(s)
s.sort(reverse=False)
result = "".join(s)
print(result)
'''
s = 'aaacccbbb',去重并从小到大排序输出'abc'
set去重，去重转成list，利用sort方法排序，reverse=False是从小到大排
list是不变数据类型
'''

"""
13、lambda函数
"""
sum = lambda a,b:a*b
print(sum(5,4))

'''lambda匿名函数：精简代码，lambda省去了定义函数，map省去了写for循环过程'''
a = ["北京","上海","重庆","天津"]
res = list(map(lambda x:"填充值" if x=="" else x,a))
print(res)

"""
14、字典根据键从小到大排序
"""
dictx={"name":"Abel","age":26,"city":"Beijing","tel":123456}
list14 = sorted(dictx.items(),key=lambda i:i[0],reverse=False)  #dict.items()结果是字典的键值对元组，i[0]表示键，i[1]表示值，通过lambda函数根据键排序
print("sorted根据字典键排序",list14)
new_dict={}
for i in list14:
    new_dict[i[0]]=i[1]
print("新字典",new_dict)

"""
15、counter统计
"""
from collections import Counter
a = "Abel,guo,leo,messi"
result = Counter(a)
print(result)

"""
16、引用计数机制
"""
'''
  python垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，是为了处理循环引用的难题
  当有1个变量保存了对象的引用时，此对象的引用计数就会加1
  del删除变量指向对象，依次减1
'''
import time
class Animal(object):
    def __init__(self, name):       # 创建完对象后会自动被调用
        print('__init__方法被调用')
        self.__name = name
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..."%self.__name)
cat = Animal("美短")
cat2 = cat
cat3 = cat
print(id(cat),id(cat2),id(cat3))    #cat和cat2和cat3的内存ID一致，说明是同一个对象
print("删除cat对象")
del cat
print("删除cat2对象")
del cat2
print("删除cat3对象")
del cat3                #del方法只有在对象真正被删除时候才调用打印（也就是cat3被删除的时候）
print("程序2秒钟后结束")
time.sleep(2)

"""
17、filter方法求出列表所有奇数并构建新列表
filter()函数用于过滤序列，接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回True或False，最后将返回True的元素放到新列表
"""
a = [1,2,3,4,5,6,7,8,9,10]
def func(a):
    return a%2 == 1
newlist = filter(func,a)
newlist = [i for i in newlist]
print(newlist)
result = [i for i in a if i%2==0]
print(result)

"""
18、数据类型
"""
a=type((1))
print(a)
a=type(("1"))
print(a)
a=type((1,))
print(a)

"""
19、列表合并
"""
list1=[1,3,5,7,9]
list2=[2,4,6,8,10]

list1.extend(list2)
print(list1)

list1.sort(reverse=False)
print(list1)

"""
20、datetime
"""
import datetime
a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' 星期：' +str(datetime.datetime.now().isoweekday())
print(a)

"""
21、异常
"""
'''
自定义异常用raise抛出异常
'''
def func():
    try:
        for i in range(5):
            if i>2:
                raise Exception("数字大于2")
    except Exception as result:
        print(result)
func()

'''
try...except...else没有捕获到异常，执行else语句
try...except...finally不管是否捕获到异常，都执行finally语句
'''
try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了：%s'%errorMsg)
else:
    print('没有捕获到异常，则执行该语句')

try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了：%s'%errorMsg)
finally:
    print('不管是否捕获到异常，都执行该句')

"""
22、列表转换
"""
'''
列表推导式
运行过程：for i in a,每个i是【1，2】，【3，4】，【5，6】，for j in i,每个j就是1，2，3，4，5，6，合并后就是结果
'''
a = [[1,2],[3,4],[5,6]]
x = [j for i in a for j in i]
print(x)

'''
将列表转成numpy矩阵，通过numpy的flatten()方法
'''
import numpy as np
b = np.array(a).flatten().tolist()
print(b)

a = [1,2,3]
b = [4,5,6]
result = a+b
print(result)

'''
python字典和json字符串相互转化方法
json.dumps()字典转json字符串，json.loads()json转字典
'''
import json
dic = {"name":"Abel"}
res = json.dumps(dic)
print(res,type(res))
res1 = json.loads(res)
print(res1,type(res1))

"""
23、join
"""
'''
join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串，结果一致
'''
x = "abc"
y = "def"
z = ["d","e","f"]

m = x.join(y)
n = x.join(z)
print(m)
print(n)

"""
24、交换数值
"""
a,b =3,4
print(a,b)
a,b=b,a
print(a,b)

"""
25、zip
"""
'''
zip函数在运算时，会以一个或多个序列（可迭代对象）作为参数，返回一个元组的列表。同时将这些序列中并排的元素配对
zip（）参数可以接受任何类型的序列，同时也可以有两个以上的参数；当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组
'''
a = [1,2]
b = [3,4]
result1 = [i for i in zip(a,b)]
print(result1)

a = (1,2)
b = (3,4)
result2 = [i for i in zip(a,b)]
print(result2)

a = "ab"
b = "xyz"
result3 = [i for i in zip(a,b)]
print(result3)

A = zip(("a","b","c","d","e"),(1,2,3,4,5))
A0 = dict(A)
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
print("A0",A0)
print(list(zip(("a","b","c","d","e"),(1,2,3,4,5))))
print(A2)
print(A3)

s = dict([["name","Abel"],["age",26]])    #dict创建字典新方法，列表
print(s)
s = dict([("name","Messi"),("age",33)])   #dict创建字典新方法，元组
print(s)

"""
26、正则表达式
"""
'''1、re模块'''
import re

a = "张明 98分"
result = re.sub(r"\d+", "100", a)
print(result)

'''2、正则匹配，匹配日期'''
url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2019-02-20%7C2019-02-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
result = re.findall(r'dateRange=(.*?)%7C(.*?)&',url)
print(result)

'''3、正则切分字符串输出'''
s = "info:Abel 18 Beijing"
result = re.split(r":| ",s)
print(result)

'''4、匹配以163.com结尾的邮箱'''
email_list = ["pony@163.com","pony@163.cn","pony@qq.com"]

for email in email_list:
    ret = re.match("[\w]{4,20}@163\.com$",email)
    if ret:
        print("%s 符合规定，匹配的结果是：%s" % (email, ret.group()))
    else:
        print("%s 不符合要求" % email)

'''
5、正则过滤英文和数字
  (.*)是贪婪匹配，会把满足正则的尽可能多的往后匹配
  (.*？)是非贪婪匹配，会把满足正则的尽可能少匹配
'''
import re
a = 'not 404.0 found 错误 404 编码'
list16 = a.split(" ")
print(list16)
result = re.findall('\d+|[a-zA-Z]+',a)        #匹配数字
result = re.findall('\d+\.?\d*|[a-zA-Z]+',a)
for i in result:
    if i in list16:
        list16.remove(i)
new_dict = " ".join(list16)
print(result)
print(new_dict)

s = "<a>哈哈哈</a><a>呵呵呵</a>"
import re
result1=re.findall("<a>(.*)</a>",s)
print("贪婪匹配",result1)
result2=re.findall("<a>(.*?)</a>",s)
print("非贪婪匹配",result2)

'''6、用正则匹配出标签里面的内容("中国")，其中class的类名是不确定的'''
import re
str1 = '<div class="name">中国</div>'
result =re.findall(r'<div class=".*">(.*?)</div>',str1)  #.代表可有可无，*代表任意字符，满足类名可以变化；(.*?)提取文本
print(result)

'''7、匹配不是以4和7结尾的手机号'''
tels = ['12345678910','10086','10000','1234567']
for tel in tels:
    ret = re.match("1\d{9}[0-3,5-6,8-9]",tel)
    if ret:
        print("想要的结果",ret.group())
    else:
        print("%s 不是想要的手机号" % tel)

'''
8、正则表达式匹配第一个URL
  findall结果无需加group(),search需要加group()提取
'''
s = '<img data-original="https://www.baidu.com/smile.jpg" src="https://www.sina.com/weibo.jpg" style="display:inline;">'
res = re.findall(r"https://.*?\.jpg",s)[0]
print(res)
res = re.search(r"https://.*?\.jpg",s)
print(res.group())

'''9、正则匹配中文'''
title = '明天，hi，你好'
pattern = re.compile(r'[\u4e00-\u9fa5]+')
result  = pattern.findall(title)
print(result)

'''10、匹配出www.tencent.com'''
labels = ["<html><h1>www.google.com</h1></html>","<html><h1>www.tencent.com</h2></html>"]
for label in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*?</\2></\1>", label)
    if ret:
        print("%s 是服务要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)

"""
27、
"""

"""
28、写一个单列模式
"""
class Singleton(object):    #实例化一个单例
    __instance = None
    def __new__(cls,age,name):  #如果类属性__instance的值为None,就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时能知道之前已经创建过对象了，保证只有一个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton(18, "Abel")
b = Singleton(18, "Messi")

print(id(a))
print(id(b))

a.age = 19      #给a指向的对象添加一个属性
print(b.age)    #获取b指向的对象的age属性

"""
29、round,保留两位小数
"""
a = "%.03f"%1.3335
print(a,type(a))
b = round(float(a),1)
print(b)
b = round(float(a),2)
print(b)

A = zip(("a","b","c","d","e"),(1,2,3,4,5))
A0 = dict(A)

"""
30、打印结果
"""
def fn(k,v,dic={}):
    dic[k]=v
    print(dic)
fn("one",1)         #直接将键值对传给字典
fn("two",2)         #因为字典在内存中是可变数据类型，所以指向同一个地址，传了新的参数后，会相当于给字典增加键值对
fn("three",3,{})    #因为传了一个新字典，所以不再是原先默认参数的字典

"""
31、pop和del删除字典字段
"""
dic = {"name":"Abel","age":26}
dic.pop("name")
print(dic)
dic = {"name":"Abel","age":26}
del dic["name"]
print(dic)

"""
32、排序
"""
'''1、'''
list31 = [0,-1,1,-10,2,3]
list31.sort(reverse=False)               #sort对列表排序
print("list.sort在list基础上修改，无返回值",list31)

list310 = [0,-1,1,-10,2,3]
result = sorted(list310,reverse=False)
print("sorted有返回值是新的list",list310)  #sorted对列表排序
print("返回值",result)

foo = [1,10,-1,2,9,-2,3,8,-3,4,7,5,6]
a = sorted(foo, key=lambda x:x)             #从小到大
b = sorted(foo, key=lambda x:(x<0,abs(x)))  #正数从小到大，负数从大到小
print(a)
print(b)

'''
2、列表嵌套字典的排序，分别根据年龄和姓名排序
'''
foo = [{"name":"Abel","age":26},{"name":"Leo","age":18},{"name":"Messi","age":16},{"name":"pony","age":30}]
a = sorted(foo, key=lambda x:x["age"],reverse=True)    #年龄从大到小
print(a)
b = sorted(foo, key=lambda x:x["name"])     #姓名从小到大
print(b)

'''
3、列表嵌套元组，分别按字母和数字排序
'''
foo = [("Abel",26),("leo",18),("uber",16),("pony",30)]
a = sorted(foo, key=lambda x:x[1],reverse=True)
print(a)
b = sorted(foo, key=lambda x:x[0])
print(b)

''' 
4、list从小到大排序，不许用sort，利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作
'''
listz=[1,2,5,3,4]
new_list=[]
def get_min(listz):
    a = min(listz)       #获取列表最小值
    listz.remove(a)      #删除最小值
    new_list.append(a)  #将最小值加入新列表
    if len(listz) > 0:
        get_min(listz)
    return new_list     #保证最后列里面有值，递归调用获取最小值，直到所有值获取完，并加入新列表返回
new_list=get_min(listz)
print(new_list)

"""
33、求和
"""
'''递归求和'''
def get_num(num):
    if num>=1:
        res = num + get_num(num-1)
    else:
        res = 0
    return res
res = get_num(10)
print(res)

"""
34、传参
"""
'''
python中函数参数是引用传递（不是值传递）
对于不可变类型（数值型、字符串、元组），因变量不能修改，运算不会影响到变量自身
对于可变类型（列表、字典），函数体运算可能会更改传入到参数变量
'''
def selfAdd(a):
    a += a

int34 = 1
print(int34)
selfAdd(int34)
print(int34)

list34 = [1,2]
print(list34)
selfAdd(list34)
print(list34)

"""35、华为一道编程"""
'''
有两个序列a,b，大小都为n，序列元素的值任意整形数，无序
要求：通过交换a,b中的元素，使【序列a元素的和】与【序列b元素的和】之间的差最小
1、将两序列合并为一个序列，并排序，为序列source
2、拿出最大元素Big,次大的元素Small
3、在余下的序列S[:-2]进行平分，得到序列max,min
4、将Small加到max序列，将Big加到min序列，重新计算新序列和，和大的为max，小的为min
'''

"""
100_practice
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/02/19 17:47
# @Author  : Abel

"""
'''
【程序3】
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
1.程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后的结果满足如下条件，即是结果。请看具体分析：
2.程序源代码：
'''

# include "math.h"
main()
{
    long
int
i, x, y, z;
for (i=1;i < 100000;i++)
　{x = sqrt(i + 100); 　　 / *x为加上100后开方后的结果 * /
　　y = sqrt(i + 268); 　　 / *y为再加上168后开方后的结果 * /
　　　if (x * x == i + 100 & & y * y == i + 268) / * 如果一个数的平方根的平方等于该数，这说明此数是完全平方数 * /
　　　　printf("\n%ld\n", i);
　}
}

import math
for i in range(10000):
    #转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print i

'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
1.
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
　　　　　　情况，闰年且输入月份大于3时需考虑多加一天。
2.
程序源代码：
'''
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <= month <= 12:
    sum = months[month - 1]
else:
    print 'data error'
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum

'''
【程序5】
题目：输入三个整数x, y, z，请把这三个数由小到大输出。
1.
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x > y则将x与y的值进行交换，
　　　　　　然后再用x与z进行比较，如果x > z则将x与z的值进行交换，这样能使x最小。
2.
程序源代码：
'''
l = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print l

'''
【程序6】
题目：用 * 号输出字母C的图案。
1.
程序分析：可先用
'*'
号在纸上写出字母C，再分行输出。
2.
程序源代码：
'''
print 'Hello Python world!\n'
print '*' * 10
for i in range(5):
    print '*        *'
print '*' * 10
print '*\n' * 6

'''
【程序7】
题目：输出特殊图案，请在c环境中运行，看一看，Very
Beautiful!
1.
程序分析：字符共有256个。不同字符，图形不一样。　　　　　　
2.
程序源代码：
'''
a = 176
b = 219
print chr(b),chr(a),chr(a),chr(a),chr(b)
print chr(a),chr(b),chr(a),chr(b),chr(a)
print chr(a),chr(a),chr(b),chr(a),chr(a)
print chr(a),chr(b),chr(a),chr(b),chr(a)
print chr(b),chr(a),chr(a),chr(a),chr(b)

'''
【程序8】
题目：输出9 * 9
口诀。
1.
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
2.
程序源代码：
# include "stdio.h"
main()
{
　int
i, j, result;
　printf("\n");
　for (i=1;i < 10;i++)
　　{for (j=1;j < 10;j++)
　　　　{
　　　　　result=i * j;
　　　　　printf("%d*%d=%-3d", i, j, result); / * -3d表示左对齐，占3位 * /
　　　　}
　　　printf("\n"); / * 每一行后换行 * /
　　}
}
'''
for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print '%d * %d = % -3d' % (i,j,result)
    print ''

'''
【程序9】
题目：要求输出国际象棋棋盘。
1.
程序分析：用i控制行，j来控制列，根据i + j的和的变化来控制输出黑方格，还是白方格。
2.
程序源代码：
# include "stdio.h"
main()
{
    int
i, j;
for (i=0;i < 8;i++)
　{
　　for (j=0;j < 8;j++)
　　　 if ((i+j) % 2 == 0)
　　　　printf("%c%c", 219, 219);
　　　 else
　　　　printf(" ");
　　　printf("\n");
　}
}
'''
import sys
for i in range(8):
    for j in range(8):
        if(i + j) % 2 == 0:
            sys.stdout.write(chr(219))
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write(' ')
    print ''

'''
【程序10】
题目：打印楼梯，同时在楼梯上方打印两个笑脸。
1.
程序分析：用i控制行，j来控制列，j根据i的变化来控制输出黑方格的个数。
2.
程序源代码：
'''
import sys
sys.stdout.write(chr(1))
sys.stdout.write(chr(1))
print ''

for i in range(1,11):
    for j in range(1,i):
        sys.stdout.write(chr(219))
        sys.stdout.write(chr(219))
    print ''

'''
【程序11】
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
1.
程序分析：　兔子的规律为数列1, 1, 2, 3, 5, 8, 13, 21....
2.
程序源代码：
main()
{
    long
f1, f2;
int
i;
f1 = f2 = 1;
for (i=1;i <= 20;i++)
　{printf("%12ld %12ld", f1, f2);
　　　if (i % 2 == 0) printf("\n"); / * 控制输出，每行四个 * /
　　　f1=f1+f2; / * 前两个月加起来赋值给第三个月 * /
　　　f2=f1+f2; / * 前两个月加起来赋值给第三个月 * /
　}
}
'''
f1 = 1
f2 = 1
for i in range(1,21):
    print '%12d %12d' % (f1,f2)
    if (i % 2) == 0:
        print ''
    f1 = f1 + f2
    f2 = f1 + f2

'''
【程序12】
题目：判断101 - 200
之间有多少个素数，并输出所有素数。
1.
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
　　　　　　则表明此数不是素数，反之是素数。 　　　　　　
2.
程序源代码：
'''
h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print '%-4d' % m
        h += 1
        if h % 10 == 0:
            print ''
    leap = 1
print 'The total is %d' % h

'''
【程序13】
题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数
　　　本身。例如：153
是一个“水仙花数”，因为153 = 1
的三次方＋5
的三次方＋3
的三次方。
1.
程序分析：利用for循环控制100 - 999
个数，每个数分解出个位，十位，百位。
2.
程序源代码：
'''
for n in range(100,1001):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if i * 100 + j * 10 + k == i + j ** 2 + k ** 3:
        print "%-5d" % n

'''
【程序14】
题目：将一个正整数分解质因数。例如：输入90, 打印出90 = 2 * 3 * 3 * 5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)
如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)
如果n <> k，但n能被k整除，则应打印出k的值，并用n除以k的商, 作为新的正整数你n,
　重复执行第一步。
(3)
如果n不能被k整除，则用k + 1
作为k的值, 重复执行第一步。

2.
程序源代码：
'''
from sys import stdout
n = int(raw_input("input number:\n"))
print "n = %d" % n

for i in range(2,n + 1):
    while n != i:
        if n % i == 0:
            stdout.write(str(i))
            stdout.write("*")
            n = n / i
        else:
            break
print "%d" % n

'''
【程序15】
题目：利用条件运算符的嵌套来完成此题：学习成绩 >= 90
分的同学用A表示，60 - 89
分之间的用B表示，
　　　60
分以下的用C表示。
1.
程序分析：(a > b)?a:b这是条件运算符的基本例子。
2.
程序源代码：
不支持这个运算符
'''
score = int(raw_input('input score:\n'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print '%d belongs to %s' % (score,grade)

'''
【程序17】
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
1.
程序分析：利用while语句, 条件为输入的字符不为
'\n'.
　　　　　　
2.
程序源代码：
'''
import string
s = raw_input('input a string:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others)

'''
题目：求s = a + aa + aaa + aaaa + aa...a的值，其中a是一个数字。例如2 + 22 + 222 + 2222 + 22222(此时
　　　共有5个数相加)，几个数相加有键盘控制。
1.
程序分析：关键是计算出每一项的值。
2.
程序源代码：
'''
Tn = 0
Sn = []
n = int(raw_input('n = :\n'))
a = int(raw_input('a = :\n'))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn

Sn = reduce(lambda x,y : x + y,Sn)
print Sn

'''
【程序19】
题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6 = 1＋2＋3.
编程
　　　找出1000以内的所有完数。
1.
程序分析：请参照程序 < --上页程序14.
2.
程序源代码：
'''
from sys import stdout
for j in range(2,1001):
    k = []
    n = -1
    s = j
    for i in range(1,j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)

    if s == 0:
        print j
        for i in range(n):
            stdout.write(k[i])
            stdout.write(' ')
        print k[n]

'''
【程序20】
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
　　　第10次落地时，共经过多少米？第10次反弹多高？
1.
程序分析：见下面注释
2.
程序源代码：
'''
Sn = 100.0
Hn = Sn / 2

for n in range(2,11):
    Sn += 2 * Hn
    Hn /= 2

print 'Total of road is %f' % Sn
print 'The tenth is %f meter' % Hn

'''
【程序1】
题目
：有1、2、3、4
个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
1.
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去
　　　　　　掉不满足条件的排列。
2.
程序源代码：
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print i,j,k

'''
【程序2】
题目：企业发放的奖金根据利润提成。利润(I)
低于或等于10万元时，奖金可提10 %；利润高
　　　于10万元，低于20万元时，低于10万元的部分按10 % 提成，高于10万元的部分，可可提
　　　成7
.5 %；20
万到40万之间时，高于20万元的部分，可提成5 %；40
万到60万之间时高于
　　　40
万元的部分，可提成3 %；60
万到100万之间时，高于60万元的部分，可提成1
.5 %，高于
　　　100
万元时，超过100万元的部分按1 % 提成，从键盘输入当月利润I，求应发放奖金总数？
1.
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。　　　　　　
2.
程序源代码：
'''
bonus1 = 100000 * 0.1
bonus2 = bonus1 + 100000 * 0.500075
bonus4 = bonus2 + 200000 * 0.5
bonus6 = bonus4 + 200000 * 0.3
bonus10 = bonus6 + 400000 * 0.15

i = int(raw_input('input gain:\n'))
if i <= 100000:
    bonus = i * 0.1
elif i <= 200000:
    bonus = bonus1 + (i - 100000) * 0.075
elif i <= 400000:
    bonus = bonus2 + (i - 200000) * 0.05
elif i <= 600000:
    bonus = bonus4 + (i - 400000) * 0.03
elif i <= 1000000:
    bonus = bonus6 + (i - 600000) * 0.015
else:
    bonus = bonus10 + (i - 1000000) * 0.01
print 'bonus = ',bonus

'''
【程序3】
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
1.
程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后
　　　　　　的结果满足如下条件，即是结果。请看具体分析：
2.
程序源代码：

# include "math.h"
main()
{
    long
int
i, x, y, z;
for (i=1;i < 100000;i++)
　{x = sqrt(i + 100); 　　 / *x为加上100后开方后的结果 * /
　　y = sqrt(i + 268); 　　 / *y为再加上168后开方后的结果 * /
　　　if (x * x == i + 100 & & y * y == i + 268) / * 如果一个数的平方根的平方等于该数，这说明此数是完全平方数 * /
　　　　printf("\n%ld\n", i);
　}
}
'''
import math
for i in range(10000):
    #转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print i

'''
【程序30】
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。　　　
1.
程序分析：同29例
2.
程序源代码：
'''
x = int(raw_input('please input a number:\n'))
x = str(x)
for i in range(len(x)/2):
    if x[i] != x[-i - 1]:
        print 'This number is not a huiwen'
        break
    print 'This number is a huiwen'
'''
【程序29】
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
1.
程序分析：学会分解出每一位数，如下解释：(这里是一种简单的算法，师专数002班赵鑫提供)
2.
程序源代码：
'''
x = int(raw_input('please input a number:\n'))
a = x / 10000
b = x % 10000 / 1000
c = x % 1000  / 100
d = x % 100   / 10
e = x % 10

if a != 0:
    print "There are 5",e,d,c,b,a
elif b != 0:
    print "There are 4",d,c,b,a
elif c != 0:
    print "There are 3",e,d,c
elif d != 0:
    print "There are 2",e,d
else:
    print "There are 1",e
'''
【程序28】
题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第
　　　3
个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后
　　　问第一个人，他说是10岁。请问第五个人多大？
1.
程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道
　　　　　　第四人的岁数，依次类推，推到第一人（10
岁），再往回推。
'''
def age(n):
    if n == 1:c = 10
    else: c = age(n -1) + 2
    return c
print age(5)
'''
【程序27】
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
1.
程序分析：
2.
程序源代码：
'''
ef palin(n):
    next = 0
    if n <= 1:
        next = input()
        print
        print next
    else:
        next = input()
        palin(n-1)
        print next

i = 5
palin(i)
print
'''
【程序26】
题目：利用递归方法求5!。
1.
程序分析：递归公式：fn = fn_1 * 4!
2.
程序源代码：
'''
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j*fact(j - 1)
    return sum

for i in range(5):
    print '%d! = %d' % (i,fact(i))

'''
【程序25】
题目：求1 + 2!+3!+... + 20!的和
1.
程序分析：此程序只是把累加变成了累乘。
2.
程序源代码：
'''
n = 0
s = 0
t = 1

for n in range(1,21):
    t *= n
    s += t
print '1! + 2! + 3! + ... + 20! = %d' % s

方法二
s = 0
t = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r
s = sum(map(op,t))
print '1! + 2! + 3! + ... + 20! = %d' % s

'''
【程序24】
题目：有一分数序列：2 / 1，3 / 2，5 / 3，8 / 5，13 / 8，21 / 13...求出这个数列的前20项之和。
1.
程序分析：请抓住分子与分母的变化规律。
2.
程序源代码：
'''
方法一
a = 2.0
b = 1.0
s = 0
for n in range(1,21):
    s += a / b
    t = a
    a = a + b
    b = t
print s
方法二
a = 2.0
b = 1.0
s = 0
s = 0.0
for n in  range(1,21):
    s += a /b
    b,a = a, a + b
print s

方法三
a = 2.0
b = 1.0
s = 0
l = []
for n in range(1,21):
    b,a = a,a + b
    l.append(a / b)
print reduce(lambda x,y: x + y,l)

'''
【程序23】
题目：打印出如下图案（菱形）

*
** *
** ** *
** ** ** *
** ** *
** *
*
1.
程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重
　　　　　　for循环，第一层控制行，第二层控制列。
2.
程序源代码：
'''
from sys import stdout
for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print
'''
【程序22】
题目：两个乒乓球队进行比赛，各出三人。甲队为a, b, c三人，乙队为x, y, z三人。已抽签决定
　　　比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x, z比，请编程序找出
　　　三队赛手的名单。
1.
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
　　　　　　则表明此数不是素数，反之是素数。 　　　　　　
2.
程序源代码：
'''
for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print 'order is a -- %s\t b -- %s\tc -- %s' % (chr(i),chr(j),chr(k))
'''
【程序21】
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
　　　第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下
　　　的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
1.
程序分析：采取逆向思维的方法，从后往前推断。
2.
程序源代码：
'''
x2 = 1
for day in range(9,0,-1):
    x1 = (x2 + 1) * 2
    x2 = x1
print x1

'''
【程序40】
题目：将一个数组逆序输出。
1.
程序分析：用第一个与最后一个交换。
2.
程序源代码：
'''
if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a)
    print a
    for i in range(len(a) / 2):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print a
'''
【程序39】
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
1.
程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后
　　　　　此元素之后的数，依次后移一个位置。
2.
程序源代码：
'''
if __name__ == '__main__':
    a = [1,4,6,9,13,16,19,28,40,100,0]
    print 'original list is:'
    for i in range(len(a)):
        print a[i]
    number = int(raw_input("please insert a new number:\n"))
    end =a[9]
    if number > end:
        a[10] = number
    else:
        for i in range(10):
            if a[i] > number:
                temp1 = a[i]
                a[i] = number
                for j in range(i + 1,11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    for i in range(11):
        print a[i]

    number = int(raw_input('please input a number:\n'))
    if number > a[len(a) - 1]:
        a.append(number)
    else:
        for i in range(len(a)):
            if a[i] > number:
                a.insert(i,number)
    print a

'''
【程序41】
题目：学习static定义静态变量的用法　　　
1.
程序分析：
2.
程序源代码：
'''
# python没有这个功能了,只能这样了:)
def varfunc():
    var = 0
    print 'var = %d' % var
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()

# attribut of class

class Static:
        StaticVar = 5
        def varfunc(self):
            self.StaticVar += 1
            print self.StaticVar
print Static.StaticVar
a = Static()
for i in range(3):
    a.varfunc()

'''
【程序42】
题目：学习使用auto定义变量的用法
1.
程序分析：　　　　　　
2.
程序源代码：
没有auto关键字，使用变量作用域来举例吧
'''
num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1

for i in range(3):
    print 'The num = %d' % num
    num += 1
    autofunc()

'''
【程序43】
题目：学习使用static的另一用法。　　　
1.
程序分析：
2.
程序源代码：
有一个static变量的用法，python是没有，演示一个python作用域使用方法
'''
class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print 'nNum = %d' % self.nNum

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print 'The num = %d' % nNum
        inst.inc()

'''
【程序44】
题目：学习使用external的用法。
1.
程序分析：
2.
程序源代码：
external.py代码：
'''
import external
if __name__ == '__main__':
    print external.add(10,20)

'''
【程序45】
题目：学习使用register定义变量的方法。
1.
程序分析：
2.
程序源代码：
没有register关键字，用整型变量代替
'''
tmp = 0
for i in range(1,101):
    tmp += i
print 'The sum is %d' % tmp

'''
【程序46】
题目：宏  # define命令练习(1)　　　
1.
程序分析：
2.
程序源代码：
没有C语言的宏，就这么写了
'''
TRUE = 1
FALSE = 0
def SQ(x):
    return x * x
print 'Program will stop if input value less than 50.'
again = 1
while again:
    num = int(raw_input('please input number:\n'))
    print 'The square for this number is %d' % (SQ(num))
    if num >= 50:
        agina = TRUE
    else:
        again = FALSE

'''
【程序47】
题目：宏  # define命令练习(2)
1.
程序分析：　　　　　　　　　　　　
2.
程序源代码：
# include "stdio.h"
# define exchange(a,b) { \ /*宏定义中允许包含两道衣裳命令的情形，此时必须在最右边加上"\"*/
　　　　　　　　　　　　int
t; \
    　　　　　　　　　　　　t = a; \
    　　　　　　　　　　　　a = b; \
    　　　　　　　　　　　　b = t; \
    　　　　　　　　　　　}'
这个宏定义python不支持
'''
def exchange(a,b):
    a,b = b,a
    return (a,b)

if __name__ == '__main__':
    x = 10
    y = 20
    print 'x = %d,y = %d' % (x,y)
    x,y = exchange(x,y)
    print 'x = %d,y = %d' % (x,y)

'''
【程序48】
题目：宏
# define命令练习(3)　　　
1.
程序分析：
2.
程序源代码：
# define LAG >
# define SMA <
# define EQ ==
# include "stdio.h"
void
main()
{
int
i = 10;
int
j = 20;
if (i LAG j)
    printf("\40: %d larger than %d \n", i, j);
else if (i EQ j)
printf("\40: %d equal to %d \n", i, j);
else if (i SMA j)
    printf("\40:%d smaller than %d \n", i, j);
else
    printf("\40: No such value.\n");
}
不知道如何用python实现类似的功能
'''
if __name__ == '__main__':
    i = 10
    j = 20
    if i > j:
        print '%d larger than %d' % (i,j)
    elif i == j:
        print '%d equal to %d' % (i,j)
    elif i < j:
        print '%d smaller than %d' % (i,j)
    else:
        print 'No such value'


'''
【程序49】
题目：  # if #ifdef和#ifndef的综合应用。
1.
程序分析：
2.
程序源代码：
# include "stdio.h"
# define MAX
# define MAXIMUM(x,y) (x>y)?x:y
# define MINIMUM(x,y) (x>y)?y:x
void
main()
{
int
a = 10, b = 20;
# ifdef MAX
printf("\40: The larger one is %d\n", MAXIMUM(a, b));
# else
printf("\40: The lower one is %d\n", MINIMUM(a, b));
# endif
# ifndef MIN
printf("\40: The lower one is %d\n", MINIMUM(a, b));
# else
printf("\40: The larger one is %d\n", MAXIMUM(a, b));
# endif
# undef MAX
# ifdef MAX
printf("\40: The larger one is %d\n", MAXIMUM(a, b));
# else
printf("\40: The lower one is %d\n", MINIMUM(a, b));
# endif
# define MIN
# ifndef MIN
printf("\40: The lower one is %d\n", MINIMUM(a, b));
# else
printf("\40: The larger one is %d\n", MAXIMUM(a, b));
# endif
}
这个还是预处理的用法，python不支持这样的机制，演示lambda的使用。
'''
MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print 'The largar one is %d' % MAXIMUM(a,b)
    print 'The lower one is %d' % MINIMUM(a,b)

'''
【程序51】
题目：学习使用按位与 & 。　　　
1.
程序分析：0 & 0 = 0;
0 & 1 = 0;
1 & 0 = 0;
1 & 1 = 1
2.
程序源代码：
'''
if __name__ == '__main__':
    a = 077
    b = a & 3
    print 'a & b = %d' % b
    b &= 7
    print 'a & b = %d' % b
'''
【程序52】
题目：学习使用按位或 | 。
1.
程序分析：0 | 0 = 0;
0 | 1 = 1;
1 | 0 = 1;
1 | 1 = 1　　　　　　　　　　　　
2.
程序源代码：
'''

if __name__ == '__main__':
    a = 077
    b = a | 3
    print 'a | b is %d' % b
    b |= 7
    print 'a | b is %d' % b
'''
【程序53】
题目：学习使用按位异或 ^ 。　　　
1.
程序分析：0 ^ 0 = 0;
0 ^ 1 = 1;
1 ^ 0 = 1;
1 ^ 1 = 0
2.
程序源代码：
'''
if __name__ == '__main__':
    a = 077
    b = a ^ 3
    print 'The a ^ 3 = %d' % b
    b ^= 7
    print 'The a ^ b = %d' % b

'''
【程序54】
题目：取一个整数a从右端开始的4～7
位。
程序分析：可以这样考虑：
(1)
先使a右移4位。
(2)
设置一个低4位全为1, 其余全为0的数。可用
~(~0 << 4)
(3)
将上面二者进行 & 运算。
'''
if __name__ == '__main__':
    a = int(raw_input('please input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print '%o\t%o' %(a,d)
'''
【程序55】
题目：学习使用按位取反
~。　　　
1.
程序分析：~0 = 1;
~1 = 0;
2.
程序源代码：
如何查看复数的16进制数
'''
f __name__ == '__main__':
    a = 234
    b = ~a
    print 'The a\'s 1 complement is %d' % b
    a = ~a
    print 'The a\'s 2 complement is %d' % a

'''
【程序56】
题目：画图，学用circle画圆形。　　　
1.
程序分析：
2.
程序源代码：
# include "graphics.h"
main()
{
int
driver, mode, i;
float
j = 1, k = 1;
driver = VGA;
mode = VGAHI;
initgraph( & driver, & mode, "");
setbkcolor(YELLOW);
for (i=0;i <= 25;i++)
    {
        setcolor(8);
    circle(310, 250, k);
    k = k + j;
    j = j + 0.3;
    }
    }

    '''
if __name__ == '__main__':
    from Tkinter import *

    canvas = Canvas(width=800, height=600, bg='yellow') 
    canvas.pack(expand=YES, fill=BOTH)               
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
        k += j
        j += 0.3

    mainloop()
'''
    【程序57】
    题目：画图，学用line画直线。
    1.
    程序分析：　　　　　　　　　　　
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    from Tkinter import *

    canvas = Canvas(width=300, height=300, bg='green')  
    canvas.pack(expand=YES, fill=BOTH)                 
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0,y0,x0,y1, width=1, fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0,y0,x0,y1,fill = 'red')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()
'''
    【程序58】
    题目：画图，学用rectangle画方形。　　　
    1.
    程序分析：利用for循环控制100 - 999
    个数，每个数分解出个位，十位，百位。
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    from Tkinter import *
    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root,width = 400,height = 400,bg = 'yellow')
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_rectangle(x0,y0,x1,y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    canvas.pack()
    root.mainloop()
'''
    【程序59】
    题目：画图，综合例子。
    1.
    程序分析：
    2.
    程序源代码：
    '''
if __name__  == '__main__':
    from Tkinter import *
    canvas = Canvas(width = 300,height = 300,bg = 'green')
    canvas.pack(expand = YES,fill = BOTH)
    x0 = 150
    y0 = 100
    canvas.create_oval(x0 - 10,y0 - 10,x0 + 10,y0 + 10)
    canvas.create_oval(x0 - 20,y0 - 20,x0 + 20,y0 + 20)
    canvas.create_oval(x0 - 50,y0 - 50,x0 + 50,y0 + 50)
    import math
    B = 0.809
    for i in range(16):
        a = 2 * math.pi / 16 * i
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 * math.sin(a) * B)
        canvas.create_line(x0,y0,x,y,fill = 'red')
    canvas.create_oval(x0 - 60,y0 - 60,x0 + 60,y0 + 60)


    for k in range(501):
        for i in range(17):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 + math.sin(a) * B)
            canvas.create_line(x0,y0,x,y,fill = 'red')
        for j in range(51):
            a = (2 * math.pi / 16) * i + (2* math.pi / 180) * k - 1
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 * math.sin(a) * B)
            canvas.create_line(x0,y0,x,y,fill = 'red')
    mainloop()
'''
    【程序60】
    题目：画图，综合例子。　　　
    1.
    程序分析：
    2.
    程序源代码：
    键盘不知道如何响应，先不写这个
    # include "graphics.h"
    # define LEFT 0
    # define TOP 0
    # define RIGHT 639
    # define BOTTOM 479
    # define LINES 400
    # define MAXCOLOR 15
    main()
    {
    int
    driver, mode, error;
    int
    x1, y1;
    int
    x2, y2;
    int
    dx1, dy1, dx2, dy2, i = 1;
    int
    count = 0;
    int
    color = 0;
    driver = VGA;
    mode = VGAHI;
    initgraph( & driver, & mode, "");
    x1 = x2 = y1 = y2 = 10;
    dx1 = dy1 = 2;
    dx2 = dy2 = 3;
    while (!kbhit())
    {
        line(x1, y1, x2, y2);
    x1 += dx1;
    y1 += dy1;
    x2 += dx2;
    y2 + dy2;
    if (x1 <= LEFT | | x1 >= RIGHT)
    dx1=-dx1;
    if (y1 <= TOP | | y1 >= BOTTOM)
    dy1=-dy1;
    if (x2 <= LEFT | | x2 >= RIGHT)
    dx2=-dx2;
    if (y2 <= TOP | | y2 >= BOTTOM)
    dy2=-dy2;
    if (++count > LINES)
    {
    setcolor(color);
    color=(color >= MAXCOLOR)?0:++color;
    }
    }
    closegraph();
    }

    '''
【程序61】
题目：打印出杨辉三角形（要求打印出10行如下图）　　　
1.程序分析：
'''
    if __name__ == '__main__':
        a = []
    for i in range(10):
        a.append([])
    for j in range(10):
        a[i].append(0)
    for i in range(10):
        a[i][0] = 1
    a[i][i] = 1
    for i in range(2, 10):
        for
    j in range(1, i):
    a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    from sys import stdout

    for i in range(10):
        for
    j in range(i + 1):
    stdout.write(a[i][j])
    stdout.write(' ')
    print

    '''
【程序62】
题目：学习putpixel画点。
1.程序分析：　　　　　　　　　　　　
2.程序源代码：
'''
    include
    "stdio.h"
    # include "graphics.h"
    main()
    {
    int
    i, j, driver = VGA, mode = VGAHI;
    initgraph( & driver, & mode, "");
    setbkcolor(YELLOW);
    for (i=50;j <= 230;i += 20)
        for (j=50;j <= 230;j++)
            putpixel(i, j, 1);
        for (j=50;j <= 230;j += 20)
            for (i=50;j < 230;i++)
                putpixel(i, j, 1);
    }

    【程序63】
    题目：画椭圆ellipse　　　
    1.
    程序分析：
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    from Tkinter import *
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width = 400,height = 600,bg = 'white')
    for i in range(20):
        canvas.create_oval(250 - top,250 - bottom,250 + top,250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()
'''
    【程序64】
    题目：利用ellipse and rectangle
    画图。
    1.
    程序分析：
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    from Tkinter import *
    canvas = Canvas(width = 400,height = 600,bg = 'white')
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
        canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
        canvas.create_rectangle(20 - 2 * i,20 - 2 * i ,10 * (i + 2),10 * (i +2 ))
        right += 5
        left += 5
        top += 10
    canvas.pack()
    mainloop()

'''
    【程序65】
    题目：一个最优美的图案。　　　
    1.
    程序分析：
    2.
    程序源代码：
    '''
import math
class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0
points = []

def LineToDemo():
    from Tkinter import *
    screenx = 400
    screeny = 400
    canvas = Canvas(width = screenx,height = screeny,bg = 'white')

    AspectRatio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
 for i in range(MAXPTS):
        rads = angle * math.pi /100.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
        angle += step
        point.append(p)

    canvas.create_oval(xcenter - radius,ycenter - radius,
                       xcenter + radius,ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i,MAXPTS):
            canvas.create_line(point[i].x,points[i].y,point[j].x,point[j].y)
    canvas.pack()
    mainloop()
if __name__ == '__main__':
    LineToDemo()

'''
    【程序66】
    题目：输入3个数a, b, c，按大小顺序输出。　　　
    1.
    程序分析：利用指针方法。
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    a = int(raw_input('please input the a:\n'))
    b = int(raw_input('please input the b:\n'))
    c = int(raw_input('please input the c:\n'))

    def swap(p1,p2):
        return p2,p1

    if a > b :
        a,b = swap(a,b)
    if a > c :
        a,c = swap(a,c)
    if b > c :
        b,c = swap(b,c)
    print a,b,c

'''
    【程序67】
    题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
    1.
    程序分析：谭浩强的书中答案有问题。　　　　　　
    2.
    程序源代码：
    '''
def inp(numbers):
    for i in range(9):
        numbers.append(int(raw_input('please input a number:\n')))
    numbers.append(int(raw_input('please input a number:\n')))
p = 0
def max_min(array):
    max = min = 0
    for i in range(1,len(array) - 1):
        p = i
        if array[p] > array[max] : max = p
        elif array[p] < array[min] : min = p
    k = max
    l = min
    array[0],array[1] = array[1],array[0]
    array[9],array[k] = array[k],array[9]

def outp(numbers):
    for i in range(len(numbers)):
        print numbers[i]

if __name__ == '__main__':
    array = []
    inp(array)
    max_min(array)
    outp(array)

'''
    【程序68】
    题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
    1.
    程序分析：
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    n = int(raw_input('The totle number is:\n'))
    m = int(raw_input('back m:\n'))

    def move(array,n,m):
        array_end = array[n - 1]
        for i in range(n - 1,-1,-1):
            array[i] = array[i - 1]
        array[0] = array_end
        m -= 1
        if m > 0:move(array,n,m)

    number = []
    for i in range(n):
        number.append(int(raw_input('please input a number:\n')))
    print 'orignal number:',number

    move(number,n,m)

    print 'after moved:',number

【程序69】
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出
　　　圈子，问最后留下的是原来第几号的那位。
1. 程序分析：
2.程序源代码：
'''
    if __name__ == '__main__':
        nmax = 50
    n = int(raw_input('please input the total of number:\n'))
    num = []
    for i in range(n):
        num.append(i + 1)

    i = 0
    k = 0
    m = 0

    while m < n - 1:
        if num[i] != 0: k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 0
        i += 1
        if i == n: i = 0

    i = 0
    while num[i] == 0: i += 1
    print num[i]

    '''
【程序70】
题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。　　　
1.程序分析：
2.程序源代码
就这样吧
'''
    if __name__ == '__main__':
        str = raw_input('please input the str:\n')
        print 'The string has %d characters:' % len(str)

    '''

 '''
    【程序71】
    题目：编写input()
    和output()
    函数输入，输出5个学生的数据记录。
    1.
    程序分析：
    2.
    程序源代码：
    使用list来模拟结构（不使用class）
    stu = [string, string, list]
    '''
N = 3
#stu
    # num : string
    # name : string
    # score[4] : list
student = []
for i in range(5):
    student.append(['','',[]])

def input_stu(stu):
    for i in range(N):
        stu[i][0] = raw_input('please input student num:\n')
        stu[i][1] = raw_input('please input student name:\n')
        for j in range(3):
            stu[i][2].append(int(raw_input('score:\n')))

def output_stu(stu):
    for i in range(N):
        print '%-6s%-10s' % ( stu[i][0],stu[i][1])
        for j in range(3):
            print '%-8d' % stu[i][2][j]

if __name__ == '__main__':
    input_stu(student)
    print student
    output_stu(student)

'''
    【程序72】
    题目：创建一个链表。
    1.
    程序分析：　　　　　　　　　　　
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(raw_input('please input a number:\n'))
        ptr.append(num)
    print ptr
'''
    【程序73】
    题目：反向输出一个链表。　　　
    1.
    程序分析：
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(raw_input('please input a number:\n'))
        ptr.append(num)
    print ptr
    ptr.reverse()
    print ptr

'''
    【程序74】
    题目：连接两个链表。
    1.
    程序分析：
    2.
    程序源代码：
    代码上好像只有，列表排序
    '''
if __name__ == '__main__':
    arr1 = (3,12,8,9,11)
    ptr = list(arr1)
    print ptr
    ptr.sort()
    print ptr

'''
    【程序75】
    题目：放松一下，算一道简单的题目。
    1.
    程序分析：
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1: n += 1
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        if i == 3: print 64 + i
'''
    【程序76】
    题目：编写一个函数，输入n为偶数时，调用函数求1 / 2 + 1 / 4 + ... + 1 / n, 当输入n为奇数时，调用函数
    　　　1 / 1 + 1 / 3 + ... + 1 / n(利用指针函数)
    1.
    程序分析：
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    def peven(n):
        i = 0
        s = 0.0
        for i in range(2,n + 1,2):
            s += 1.0 / i
        return s
    def podd(n):
        s = 0.0
        for i in range(1,n + 1,2):
            s += 1 / i
        return s
    def dcall(fp,n):
        s = fp(n)
        return s

    if __name__ == '__main__':
        n = int(raw_input('please input a number:\n'))
        if n % 2 == 0:
            sum = dcall(peven,n)
        else:
            sum = dcall(podd,n)
        print sum

'''
    【程序77】
    题目：填空练习（指向指针的指针）
    1.
    程序分析：　　　　　
    2.
    程序源代码：
    main()
    {
        char * s[] = {"man", "woman", "girl", "boy", "sister"};
    char ** q;
    int
    k;
    for (k=0;k < 5;k++)
    {; / * ÕâÀïÌîÐ´Ê²Ã´Óï¾ä * /
    printf("%s\n", * q);
    }
    }
    '''
if __name__ == '__main__':
    s = ["man","woman","girl","boy","sister"]
    for i in range(len(s)):
        print s[i]

'''
    【程序78】
    题目：找到年龄最大的人，并输出。请找出程序中有什么问题。
    1.
    程序分析：
    2.
    程序源代码
    '''
if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key
    print '%s,%d' % (m,person[m])

'''
    【程序79】
    题目：字符串排序。
    1.
    程序分析：
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    str1=(raw_input('please input the first string:\n'))
    str2=(raw_input('please input the second string:\n'))
    str3=(raw_input('please input the third string:\n'))
    print str1,str2,str3

    if str1 > str2 : str1,str2 = str2,str1
    if str1 > str3 : str1,str3 = str3,str1
    if str2 > str3 : str2,str3 = str3,str2

    print 'After being sorted.'
    print str1,str2,str3

'''
    【程序80】
    题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子凭据分为五份，多了一个，这只
    　　　猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了
    　　　一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，
    　　　问海滩上原来最少有多少个桃子？
    1.
    程序分析：
    2.
    程序源代码：
    '''
if __name__ == '__main__':
    for i in range(4,10000,4):
        count = 0
        m = i
        for k in range(5):
            j = i /4 * 5 + 1
            i = j
            if j % 4 == 0:
                count += 1
            else:
                break
        i = m
        if count == 4:
            print count
            break

'''
    【程序81】
    题目：809 *??=800 *??+9 *??+1
    其中??代表的两位数, 8 *??的结果为两位数，9 *??的结果为3位数。求??代表的两位数，及809 *??后的结果。
    1.
    程序分析：
    2.
    程序源代码
    这个程序实在是奇怪
    0 = 1:(
              就写个程序而已，不去追究了
    '''
a = 809
for i in range(10,100):
    b = i * a + 1
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print b,'/',i,' = 809 * ',i, ' + ' , b % i
'''
    【程序82】
    题目：八进制转换为十进制
    1.程序分析：　　　　　　　　　　　
    2.程序源代码：
    '''
if __name__ == '__main__':
    n = 0
    p = (raw_input('please input a octal number:\n'))
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print n

'''
    【程序83】
    题目：求0―7所能组成的奇数个数。
    1.程序分析：
    2.程序源代码：
    '''
if __name__ == '__main__':
    sum = 4
    s = 4
    for i in range(2,9):
        print sum
        if i <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print 'sum = %d' % sum

'''
    【程序84】
    题目：一个偶数总能表示为两个素数之和。
    1.程序分析：
    2.程序源代码：
    此代码有问题，待修改
    '''
import math
if __name__ == '__main__':
    a = int(raw_input('input an odd number:\n'))
    d = 0
    c = 2
    for b in range(3,a / 2 + 1,2):
        m = 0
        for c in range(2,int(math.sqrt(b)) + 1):
            if b % c == 0 :
                m = c
                break

        if m > math.sqrt(b):
            d = a - b
        else:
            break

        for c in range(2,int(math.sqrt(d)) + 1):
            if d % c == 0:
                m = c
                break
        if m > math.sqrt(d):
            print '%d = %d + %d' % (a,b,d)
'''
    【程序85】
    题目：判断一个素数能被几个9整除
    1.程序分析：
    2.程序源代码：
    '''
if __name__ == '__main__':
    zi = int(raw_input('input a number:\n'))
    n1 = 1
    c9 = 1
    m9 = 9
    sum = 9
    while n1 != 0:
        if sum % zi == 0:
            n1 = 0
        else:
            m9 *= 10
            sum += m9
            c9 += 1
    print '%d can be divided by %d 9' % (sum,c9)

'''
    【程序86】
    题目：两个字符串连接程序
    1.程序分析：
    2.程序源代码：
    '''
if __name__ == '__main__':
    import string
    str1 = (raw_input('please input a string:\n'))
    str2 = (raw_input('please input a string:\n'))
    print str1 + str2

a = 'vision'
b = 'guo'
c = a + b
print c

'''
    【程序87】
    题目：回答结果（结构体变量传递）
    1.程序分析：　　　　　
    2.程序源代码：
    '''
if __name__ == '__main__':
    class student:
        X = 0
C = 0
    def f(stu):
stu.X = 20
stu.C = 'C'
    a = student()
    a.X = 3
    a.C = 'a'
    f(a)
    print a.X,a.C

'''
    【程序88】
    题目：读取7个数（1―50）的整数值，每读取一个值，程序打印出该值个数的＊。
    1.程序分析：
    2.程序源代码：
    '''
if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(raw_input('please input a number:\n'))
while a > 50 or a < 1:
a = int(raw_input('please input a number:\n'))
print a * '*'
    n += 1

'''
    【程序89】
    题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
    　　　每位数字都加上5, 然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
    1.程序分析：
    2.程序源代码：
    '''from sys import stdout
if __name__ == '__main__':
    a = int(raw_input('please input a number:\n'))
    aa = []
    aa.append(a % 10)
    aa.append(a % 100 /10)
    aa.append(a % 1000 / 100)
    aa.append(a / 1000)

    for i in range(4):
        aa[i] += 5
        aa[i] %= 10
    for i in range(2):
        aa[i],aa[3 - i] = aa[3 - i],aa[i]
    for i in range(3,-1,-1):
        stdout.write(aa[i])

'''
    【程序90】
    题目：专升本一题，读结果。
    1.程序分析：
    2.程序源代码：
    '''
if __name__ == '__main__':
    M = 5
    a = [1,2,3,4,5]
    i = 0
    j = M -1
    while i < M:
        a[i],a[j] = a[j],a[i]
       print a
i += 1
i -= 1
    for i in range(5):
print a[i]

'''
    【程序91】
    题目：时间函数举例1
    1.程序分析：
    2.程序源代码：
    '''
if __name__ == '__main__':
    import time
    print time.ctime(time.time())
    print time.asctime(time.localtime(time.time()))
    print time.asctime(time.gmtime(time.time()))

'''
    【程序92】
    题目：时间函数举例2
    1.程序分析：　　　　　　　　　　　
    2.程序源代码：
    '''
if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print i
    end = time.time()
    print end - start

'''
    【程序93】
    题目：时间函数举例3
    1.程序分析：
    2.程序源代码：
    '''
if __name__ == '__main__':
    import time
    start = time.clock()
    for i in range(10000):
        print i
    end = time.clock()
    print 'Different is %6.3f' % (end - start)

'''
    【程序94】
    题目：时间函数举例4, 一个猜数游戏，判断一个人反应快慢。（版主初学时编的）
    1.程序分析：
    2.程序源代码：
    '''
if __name__ == '__main__':
    import time
    import random

    play_it = raw_input('Do you want to play it.(\'y\' or \'n\')')
    while play_it == 'y':
        c = raw_input('please input a character:\n')
        i = random.randint(0,2**32) % 100
        print 'please input number you guess:\n'
        start = time.clock()
        a = time.time()
        guess = int(raw_input('please input your guess:\n'))
        while guess != i:
            if guess > i:
            print 'please input a litter smaller'
guess = int(raw_input('please input your guess:\n'))
else:
             print 'please input a litter bigger'
guess = int(raw_input('please input your guess:\n'))
end = time.clock()
b = time.time()
var = (end - start) / 18.2
if var < 15:
print 'Yor are very clever!'
elif var < 25:
print 'Yor are very clever!'
else:
print 'Yor are stupid!'
print 'Congradulations'
print 'The number you guess is %d' % i
       play_it = raw_input('Do you want to play it.')

'''
    【程序96】
    题目：计算字符串中子串出现的次数
    1.程序分析：
    2.程序源代码：
    '''
if __name__ == '__main__':
    str1 = raw_input("please input a string:\n")
    str2 = raw_input("please input a sub string:\n")
    ncount = str1.count(str2)
    print ncount

'''
    【程序97】
    题目：从键盘输入一些字符，逐个把它们送到磁盘上去，直到输入一个  # 为止。
    1.程序分析：　　　　　
    2.程序源代码：
    '''
if __name__ == '__main__':
    from sys import stdout
    filename = raw_input("please input a file name:\n")
    fp = open('filename','w')
    ch = raw_input("please input string:")
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = raw_input('')
    fp.close()

'''
    【程序98】
    题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件“test”中保存。
    　　　输入的字符串以！结束。
    1.程序分析：
    2.程序源代码：
    '''
if __name__ == '__main__':
    import string
    i = (raw_input("please input:"))
    i = i.upper()
    fp = open('A.txt','w')
    fp.write(i)
    fp.close()
示例
if __name__ == '__main__':
    fp = open('test.txt','w')
    string = raw_input('please input a string:\n')
    string = string.upper()
    fp.write(string)
    fp = open('test.txt','r')
    print fp.read()
    fp.close()
'''
    程序99】
    题目:有两个磁盘文件A和B, 各存放一行字母, 要求把这两个文件中的信息合并(按字母顺序排列),
          输出到一个新文件C中.
    1.
    程序分析:
    2.
    程序源代码:
    '''
if __name__ == '__main__':
    import string
    fp = open('JCP099.py')
    a = fp.read()
    fp.close()

    fp = open('JCP098.py')
    b = fp.read()
    fp.close()

    fp = open('C.txt','w')
    l = list(a + b)
    l.sort()
    s = ''
    s = s.join(l)
    fp.write(s)
    fp.close()
"""

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
