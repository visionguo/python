#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    idc
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = ['IDC']

class IDC(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('机房'))
    yd_bandwidth =  models.CharField(max_length=32, blank=True, null=True, verbose_name=_('移动带宽'))
    lt_bandwidth = models.CharField(max_length=32, blank=True, null=True, verbose_name=_('联通带宽'))
    dx_bandwidth = models.CharField(max_length=32, blank=True, null=True, verbose_name=_('联通带宽'))
    contactor = models.CharField(max_length=128, blank=True, verbose_name=_('联系人'))
    phone = models.CharField(max_length=32, blank=True, verbose_name=_('联系号码'))
    address = models.CharField(max_length=128, blank=True, verbose_name=_("地址"))
    created_by = models.CharField(max_length=32, blank=True, verbose_name=_('创建人'))
    comment = models.TextField(blank=True, verbose_name=_('备注'))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'idc'
        ordering = ['name']