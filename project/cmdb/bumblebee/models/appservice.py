#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    appservice
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _
__all__ = ['Apps']

class Apps(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('应用名'))
    host = models.CharField(max_length=255, verbose_name=_('监控主机'))
    port = models.CharField(max_length=8, verbose_name=_('监控端口'))
    uri = models.CharField(max_length=8, default='metrics', verbose_name=_('监控路径'))

    def __repr__(self):
        return self.host

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'apps'
        ordering = ['host']