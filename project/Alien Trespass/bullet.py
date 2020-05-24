#!/usr/bin/env python
# -*- coding:utf-8 -*-

#创建Bulllet类
import pygame
from pygame.sprite import Sprite        #Bullet类继承了我们从模块pygame.sprite中导入的Sprite类

class Bullet(Sprite):   #一个对飞船发射的子弹进行管理的类
    def __init__(self,ai_settings,screen,ship):     #在飞船所处的位置创建一个子弹对象
        super(Bullet,self).__init__()   #调用super()来继承Sprite
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)     #创建了子弹的属性rect
        #子弹并非基于图像，使用pygame.Rect()类从空白开始创建一个矩形，创建这个类的实例时，必须提供矩形左上角的x坐标和y坐标，还有矩形的宽度和高度
        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置，接下来的两行代码将其移到了正确的位置，子弹的初始位置取决于飞船当前的位置，子弹的宽度和高度是从ai_settings中获取的
        self.rect.centerx = ship.rect.centerx   #将子弹的centerx设置为飞船的rect.centerx,子弹应从飞船顶部射出，将表示子弹的rect的top属性设置为飞船的rect的top属性
        self.rect.top = ship.rect.top           #让子弹看起来像是从飞船中射出的

        self.y =float(self.rect.y)  #存储用小数表示的子弹位置，以便能够微调子弹的速度

        self.color = ai_settings.bullet.color                #将子弹的颜色和速度设置分别存储到self.color和self.speed_factor
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):   #向上移动子弹
        self.y -= self.speed_factor     #更新表示子弹位置的小数值
        self.rect.y = self.y            #更新表示子弹的rect的位置

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)      #在屏幕上绘制子弹，draw.rect()使用存储在self.color中的颜色填充表示子弹的rect占据的屏幕部分