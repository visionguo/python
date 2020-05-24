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


