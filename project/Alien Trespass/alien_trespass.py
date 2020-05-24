#!/usr/bin/env python
# -*- coding:utf-8 -*-

#info:主文件alien_trespass创建一系列整个游戏都用到都对象
#包括存储在ai_settings中的设置，存储在screen中的主显示surface以及一个飞船实例
#还包含主循环，调用check_events(),ship.update()和update_screen()
#只需运行主文件，其它文件包含的代码被直接或间接地导入到这个文件中

#创建Pygame窗口以及响应用户输入
#import sys      #使用sys来退出游戏
import pygame

from pygame.sprite import Group     #导入pygame.sprite中的Group类
from settings import Settings       #导入Settings类
from ship import Ship
import func as f

def run_game():     #初始化游戏并创建一个屏幕对象
    pygame.init()   #初始化背景设置，让pygame能够正确地工作
    ai_settings =Settings()         #调用pygame.init(),再创建一个Settings实例,并将其存储在变量ai_settings中
    #screen = pygame.display.set_mode((1200,800))    #调用函数创建显示窗口
    """
    对象screen是一个surface，surface是屏幕的一部分，用于显示游戏元素
    每个元素都是一个surface，display.set_mode返回的surface表示整个游戏窗口
    激活游戏的动画循环后，每次循环都将自动重绘这个surface
    """
    screen =pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))       #调用ai_settings属性 screen_width和screen_height
    pygame.display.set_caption('Alien Invasion')

    ship =Ship(ai_settings,screen)      #在创建屏幕后创建一个名为ship的Ship实例,创建一艘飞船
    bullets = Group()       #创建一个用于存储子弹的编组，创建一个Group实例，命名为bullets

    #bg_color = (230,230,230)
    """
    设置背景色
    以RGB值指定的，红绿蓝取值范围均为0-255，(255,0,0)为红色，（0，255，0）为绿色，（0，0，255）为蓝色，可创建1600万种颜色
    """
    while True:     #开始游戏的主循环,事件是用户玩游戏时执行的操作，如按键或移动鼠标
        # for event in pygame.event.get():    #监视键盘和鼠标event
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #screen.fill(bg_color)
        """
        screen.fill(ai_settings.bg_color)
        ship.blitme()       #将飞船绘制到屏幕上，确保它出现在背景前面

        f.check_events(ship)    #让最近绘制的屏幕可见
        #f.check_events(ship)
        ship.update()
        f.update_screen(ai_settings,screen,ship)

        每次循环时，都重绘屏幕
        pygame.display.flip()       #让最近绘制的屏幕可见,不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果
        执行while循环时都绘制一个空屏幕，并擦去旧屏幕
        """

        #将bullets传递给了check_events()和update_screen()
        """
        f.check_events(ai_settings,screen,ship,bullets)     #在check_events()中，需要玩家按空格键时处理bullets
        ship.update()
        bullets.update()    #对编组调用update()时，编组将自动对其中的每个精灵调用update(),bullets.update()将为编组bullets中的每颗子弹调用bullet.update()
        f.update_screen(ai_settings,screen,ship,bullets)    #在update_screen()中，需要更新要绘制到屏幕上的bullets
        """

        """
        f.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        """

        """
        删除已消失的子弹
        """
        f.check_events(ai_settings,screen,ship,bullets)     #主循环检查玩家的输入
        ship.update()                                       #更新飞船的位置
        f.update_bullets(bullets)                           #所有未消失的子弹的位置
        f.update_screen(ai_settings,screen,ship,bullets)    #使用更新后的位置来绘制新屏幕

        for bullets in bullets.copy():      #for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本，使用copy，可以在循环中修改bullets
            if bullet.rect.bottom <= 0:     #检查每颗子弹，看它是否已从屏幕顶端消失
                bullets.remove(bullet)      #如果是这样，就将其从bullets中删除
        print(len(bullets))                 #显示当前还有多少颗子弹，从而核实已消失的子弹确实删除了
        #f.update_screen(ai_settings,screen,ship,bullets)
run_game()      #初始化游戏并开始主循环

