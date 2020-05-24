#!/usr/bin/env python
# -*- coding-utf-8 -*-

#执行API调用，返回Hacker News上当前热门文章的ID，再查看每篇排名靠前的文章

import requests

from operator import itemgetter

url ='https://hacker-news.firebaseio.com/v0/topstories.json'    #执行API调用并存储响应
r = requests.get(url)
print("Status Code:", r.status_code)

hn_ids = r.json()   #处理有关每篇文章的信息,将响应文本转换为一个python列表，使用id来创建一系列字典，每个字典都存储来一篇文章的信息
hn_dicts = []       #创建空列表，存储前面所说的字典
for hn_id in hn_ids[:30]:   #遍历前30篇文章的id，对于每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' +str(hn_id) + '.json')
    hn_r = requests.get(url)
    print(hn_r.status_code)
    response_dict = hn_r.json()

    hn_dict = {     #为当前处理的文章创建一个字典
        'title': response_dict['title'],    #字典存储标题
        'link': 'http://news.ycombinator.com/item?id=' +str(hn_id), #字典存储讨论页面的链接
        'comments':response_dict.get('descendants',0)   #字典中存储了评论数，如果文章还没有评论，响应字典中将没有键'descendants'
        }   #不确定某个键是否包含在字典中时，可使用方法dict.get(),在指定的键存在时返回与之相关联的值，在指定的键不存在时返回你指定的值，0
    hn_dicts.append(hn_id)

hn_dicts = sorted(hn_dicts,key=itemgetter('comments'),reverse=True)  #使用模块operator中的函数itemgetter()
    #向这个函数传递了键'comments',将从这个列表的每个字典中提取与键'comments'相关联的值

for hn_dict in hn_dicts:
    print "\nTitle:", hn_dict['title']
    print "Discussion link:",hn_dict['link']
    print "Comments:",hn_dict['comments']



