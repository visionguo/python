#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS      #应用于图表的Pygal样式

URL ='https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)               #执行API调用并存储响应
print("Status Code:",r.status_code)

response_dict = r.json()            #将API响应存储在一个变量中
print("Total repositories:", response_dict['total_count'])

repo_dicts= response_dict['items']  #研究有关仓库的信息

names, stars = [], []               #创建两个空列表，用于存储将包含在图表中的信息
for repo_dict in repo_dicts:
    names.append(repo_dict['name']) #将项目的名称和获得的星数附加到这些列表的末尾
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366', base_style=LCS)        #使用LightenStyle类定义类一种样式，并将其基色设置为深蓝色，传递实参base_style，以使用LightColorizedStyle类
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)   #使用Bar()创建一个简单的条形图，并向它传递my_style,并传递了样式实参；
# 让标签绕x轴旋转45度，并隐藏了图例，因为只在图表中绘制了一个数据系列
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)        #不需给这个数据系列添加标签
chart.render_to_file('python_repos.svg')
"""

"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("Status Code:", r.status_code)

response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()      #创建一个Pygal类config的实例，将其命名为my_config
my_config.x_label_rotation = 45 #两个属性，在创建Bar实例时以关键字实参的方式传递的
my_config.show_legend = False
my_config.title_font_size = 24  #设置图表标题，副标题和主标签的字体大小
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15   #使用truncate_label将较长的项目名缩短为15个字符
my_config.show_y_guides = False #隐藏图表中的水平线
my_config.width = 1000          #自定义宽度，让图表更充分地利用浏览器中的可用空间

chart =pygal.Bar(my_config,style=my_style)  #创建Bar实例时，将my_config作为第一个实参，从而通过一个实参传递了所有的配置设置
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos_1.svg')
"""

#将鼠标指向条形将显示项目的描述
import requests
import pygal

import sys  #配合使用str()
reload(sys)
sys.setdefaultencoding('utf-8')

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("Status Code:",r.status_code)

response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Number of items:",len(repo_dicts))

names, plot_dicts = [], []      #生成空列表
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {               #在循环内部，对于每个项目，都创建了字典plot_dict
        'value': repo_dict['stargazers_count'],     #value存储了星数，label存储了项目描述
        'label': str(repo_dict['description']),     #"空类型"对象没有属性"decode"
        'xlink':repo_dict['html_url'],              #在图表中添加可单击的链接
        }       #解决报错，AttributeError:'NoneType' object has no attribute 'decode'
    plot_dicts.append(plot_dict)    #将字典plot_dict附加到plot_dicts末尾

#可视化
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()      #创建一个Pygal类config的实例，将其命名为my_config
my_config.x_label_rotation = 45 #两个属性，在创建Bar实例时以关键字实参的方式传递的
my_config.show_legend = False
my_config.title_font_size = 24  #设置图表标题，副标题和主标签的字体大小
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15   #使用truncate_label将较长的项目名缩短为15个字符
my_config.show_y_guides = False #隐藏图表中的水平线
my_config.width = 1000          #自定义宽度，让图表更充分地利用浏览器中的可用空间

chart =pygal.Bar(my_config,style=my_style)  #创建Bar实例时，将my_config作为第一个实参，从而通过一个实参传递了所有的配置设置
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('',plot_dicts)        #将列表plot_dicts传递给了add()
chart.render_to_file('python_repos_links.svg')
