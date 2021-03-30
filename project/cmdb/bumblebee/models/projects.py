#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    project
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .sub_business import SubBusiness
from .asset import Asset

__all__ = ['Project']

class Project(models.Model):
    MONITOR_CHOICES = (
        ('Null', '------'),
        ('Yes', u'监控'),
    )

    MONITOR_STATUS = (
        ('Null', '------'),
        ('Gray', u'监控灰度'),
        ('Online', u'监控线上'),
        ('GrOn', u'监控灰度和线上'),
    )

    name = models.CharField(max_length=255, verbose_name=_('项目名'))
    port = models.CharField(max_length=6, verbose_name=_('端口'))
    language = models.CharField(max_length=8, verbose_name=_('开发语言'))
    prehost = models.CharField(max_length=1024, blank=True, null=True, verbose_name=_('pre主机'))
    grayhost = models.CharField(max_length=1024, blank=True, null=True, verbose_name=_('gray主机'))
    onlinehost = models.CharField(max_length=1024, blank=True, null=True, verbose_name=_('online主机'))
    sub_business = models.ForeignKey(SubBusiness, blank=True, null=True, on_delete=models.CASCADE)
    tag = models.CharField(max_length=12,  blank=True, null=True, verbose_name=_('项目标签'))
    git = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('git地址'))
    git_group = models.CharField(max_length=255, blank=True, null=True,  verbose_name=_('git组'))
    exporter_port = models.CharField(max_length=8, blank=True, null=True, verbose_name=_('应用监控端口'))
    monitor_url = models.CharField(max_length=255, blank=True, null=True, verbose_name=('监控url'))
    db_used = models.CharField(max_length=255, blank=True, null=True, verbose_name=('所使用数据库'))
    monitorchoice = models.CharField(choices=MONITOR_CHOICES, default='None', max_length=32, verbose_name=_('监控选择'))
    monitorenv = models.CharField(choices=MONITOR_STATUS, default='None', max_length=32, verbose_name=_('监控环境'))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'projects'
        ordering = ['name']