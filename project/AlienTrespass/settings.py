#!/usr/bin/env python
# -*- coding:utf-8 -*-

#info:文件settings.py包含Settings类，这个类只包含方法__init__()，它初始化控制游戏外观和飞船速度的属性
class Settings():
    """
    存储所有设置的类
    """
    def __init__(self):
        """
        初始化游戏的设置
        """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3     #存储所允许的最大子弹数，未消失的子弹数量
