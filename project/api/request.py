#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
#request包让python程序能够轻松地向网站请求信息以及检查返回的响应

#处理API响应
import requests

#执行API调用并存储响应
url ='https://api.github.com/search/repositories?q=language:python&sort=stars'
r =requests.get(url)    #执行调用
print("Status code:", r.status_code)    #响应对象中，包含一个名为status_code的属性，让我们知道请求是否成功

#将API响应存储在一个变量中
response_dict =r.json()     #json()将这些信息转换为一个python字典

#处理结果
print(response_dict.keys())
"""
"""
#处理响应字典
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r =requests.get(url)
print("Status Code:",r.status_code)

response_dict =r.json()     #将API响应存储在一个变量中
print("Total repositories:",response_dict['total_count'])

repo_dicts = response_dict['items']   #探索有关仓库的信息，将这个字典列表存储在repo_dicts中
print("Repositorites returned:",len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))         #打印这个字典包含的键数，看看其中有多少信息
for key in sorted(repo_dict.keys()):    #打印字典的所有键
    print(key)
"""

"""
#单个仓库的详细信息
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:",r.status_code)

response_dict =r.json()
print("Total repositories:",response_dict['total_count'])

repo_dicts = response_dict['items']     #研究有关仓库的信息
print("Repositories returned:",len(repo_dicts))

repo_dict = repo_dicts[0]      #研究第一个仓库

print("\nSelected information about first repository:")
print("Name:",repo_dict['name'])            #打印项目的名称
print("Owner:",repo_dict['owner']['login']) #使用owner表示所有者的字典，使用键key来获取所有者的登录名
print("Stars:",repo_dict['stargazers_count'])
print("Repository:",repo_dict['html_url'])
print("Created:",repo_dict['created_at'])
print("Updates:",repo_dict['updated_at'])
print("Description:",repo_dict['description'])
"""

#for循环描述 多个库信息
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:",r.status_code)

response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print '\nName:',repo_dict['name']
    print 'Owner:',repo_dict['owner']['login']
    print 'Stars:',repo_dict['stargazers_count']
    print 'Repository:',repo_dict['html_url']
    print 'Description:',repo_dict['description']
