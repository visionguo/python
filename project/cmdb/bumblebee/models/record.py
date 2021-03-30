#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    record
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ['Record']

class Record(models.Model):
    name = models.CharField(max_length=16, verbose_name=_('统计类别名'))
    year = models.CharField(max_length=8, verbose_name=_('年份'))
    month = models.CharField(max_length=8, verbose_name=_('月份'))
    count = models.CharField(max_length=8, verbose_name=_('数量'))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'record'
        ordering = ['name']