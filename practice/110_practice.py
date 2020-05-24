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
