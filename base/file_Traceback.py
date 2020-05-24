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
