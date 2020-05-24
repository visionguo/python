#!/usr/bin/env python
# -*- coding:utf-8 -*-

#info:包含Ship类，这个类包含方法__init__(),管理飞船位置的方法update()以及在屏幕上绘制飞船的方法blitme()。表示飞船的图像存储在文件夹images下的文件ship.bnp中

import pygame
class Ship():
    def __init__(self,ai_settings,screen):      #Ship的方法 __init__() 接受两个参数，引用self和screen,screen指定了要将飞船绘制到什么地方
                                                #__init__()的形参列表中添加了ai_settings,让飞船能够获取其速度设置
        """
        初始化飞船并设置其初始值
        """
        self.screen = screen
        self.ai_settings = ai_settings          #将形参ai_settings的值存储在一个属性中，以在update()中使用它

        self.moving_right = False   #移动标志
        self.moving_left  = False

        """
        加载飞船图像并获取其外接矩形
        """
        self.image = pygame.image.load('images/ship.bmp')       #为加载图像，调用pygame.image.load(),这个函数返回一个表示飞船的surface,这个surface存储到了self.image中
        self.rect = self.image.get_rect()       #加载图像后，使用get_rect()获取相应surface的属性rect
        self.screen_rect = screen.get_rect()    #将表示屏幕的矩形存储在self.screen_rect

        """
        将每艘新飞船放在屏幕底部中央
        """
        self.rect.centerx = self.screen_rect.centerx    #再将self.rect.centerx设置为表示屏幕的矩形的属性centerx
        self.rect.bottom = self.screen_rect.bottom      #将self.rect.bottom设置为表示屏幕的矩形的属性bottom

        self.center = float(self.rect.centerx)      #在飞船的属性centerx中存储小数值

        self.moving_right = False   #移动标志
        self.moving_left  = False

    def update(self):                  #根据移动标志调整飞船的位置
        # 更新飞船的centerx值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:  #self.rect.right返回飞船外接矩形的右边缘的x坐标
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:      #rect的左边缘的x坐标大于零，说明飞船未触及屏幕左边缘
            self.center -= self.ai_settings.ship_speed_factor

        # if self.moving_right:
        #     self.rect.centerx += 1
        # if self.moving_left:        #用if不用elif的原因，存在玩家同时按下左右箭头
        #     self.rect.centerx -= 1

        self.rect.centerx = self.center     #根据self.center更新rect对象
    def blitme(self):
        """
        在指定位置绘制飞船
        """
        self.screen.blit(self.image, self.rect)
