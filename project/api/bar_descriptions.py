#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotatuon=45,show_legend=False)

chart.title  = 'Python Projects'
chart.x_labels = ['httpie','django','flask']

plot_dicts = [      #定义名为plot_dicts的列表，包含三个字典
#Pygal根据与键'value'相关联的数字来确定条形的高度，并使用与'label'相关联的字符串给条形创建工具提示
    {'value': 16101, 'label': 'Description of httpie.'},    #此字典将创建一个条形，表示获得了16101颗星、工具提示为Description of httpie的项目
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
]

chart.add('',plot_dicts)        #接受一个字符串和一个列表，调用add()时，传入来一个由表示条形的字典组成的列表(plot_dicts)
chart.render_to_file('bar_descriptions.svg')
