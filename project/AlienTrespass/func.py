#!/usr/bin/env python
# -*- coding:utf-8 -*-

#info:包含一系列函数
#函数check_events()检测相关的事件，如按键和松开，并使用辅助函数check_keydown_events()和check_keyup_events()来处理这些事件，这些函数管理飞船的移动
#模块game_functions还包含函数update_screen(),它用于在每次执行主循环时都重绘屏幕

import sys
import pygame
from bullet import Bullet

"""
def check_events(ship): #把管理事件的代码转移至此，以简化run_game（）并隔离事件管理循环，可将事件管理与游戏的其它方面（如更新屏幕）分离
#函数包含形参ship,玩家按右箭头键时，需要将飞船向右移动
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#每当用户按键时，都将在Pygame中注册一个事件，事件都是通过方法pygame.event.get()获取的，因此在函数check_events()中，需指定要检查哪些类型的事件，每次按键都被注册为一个KEYDOWN事件
#检测到KEYDOWN事件时，需检查按下的是否是特定的键，如果按下的是右箭头键，就增大飞船的rect.centerx值，将飞船向右移动
        elif event.type == pygame.KEYDOWN:      #检测到KEYDOWN事件时作出响应
            if event.key == pygame.K_RIGHT:
                #ship.rect.centerx +=100     #向右移动飞船
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings,screen,ship):     #更新屏幕上的图像，并切换到新屏幕
    screen.fill(ai_settings.bg_color)           #每次循环时都重绘屏幕
    ship.blitme()

    pygame.display.flip()   #让最近绘制从屏幕可见
"""

#def check_keydown_events(event,ship):
def check_keydown_events(event,ai_settings,screen,ship,bullets):    #编组bullets传递给了check_keydown_events()
    #响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right =True
    elif event.key == pygame.K_LEFT:
        ship.moving_left  =True
    elif event.key == pygame.K_SPACE:   #按空格键时，创建一颗子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings,screen,ship,bullets)   #一个名为new_bullet的Bullet实例
            bullets.add(new_bullet)        #使用add()将其加入编组

        #fire_bullet(ai_settings,screen,ship,bullets)
"""
def fire_bullet(ai_settings,screen,ship,bullets):
    #如果还未到达限制，就发射一颗子弹
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

    按空格键时，检查bullets的长度，如果len(bullets)小于3，就创建一个新子弹；
    如果已有3颗未消失的子弹，那么按空格键时什么都不会发生；
    现在运行时，屏幕上最多只能有3颗子弹
"""
            #ship.moving_space =True

def check_keyup_events(event,ship):
    #响应松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left  = False

#def check_events(ship):
def check_events(ai_settings,screen,ship,bullets):  #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #check_keydown_events(event,ship)
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

#def update_screen(ai_settings,screen,ship):     #更新屏幕上的图像，并切换到新屏幕
def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)           #每次循环时都重绘屏幕，注释掉的结果是：bg black,ship 两侧有重影
    for bullet in bullets.sprites():            #方法bullets.sprites()返回一个列表，其中包含编组bullets中的所有精灵
        bullet.draw_bullet()
    ship.blitme()

    pygame.display.flip()   #让最近绘制从屏幕可见

def update_bullets(bullets):
    #更新子弹的位置，并删除已消失的子弹
    #更新子弹的位置

    bullets.update()

    """
    删除已消失的子弹
    """
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
