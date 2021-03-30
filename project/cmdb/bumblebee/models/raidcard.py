#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    raidcard
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = ['RaidCard']

class RaidCard(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('Raid卡类型'))
    cache = models.CharField(max_length=16, verbose_name=_('缓存'))
    created_by = models.CharField(max_length=32, null=True, blank=True,
                                  verbose_name=_('创建人'))
    date_created = models.DateTimeField(auto_now_add=True, null=True,
                                        blank=True, verbose_name=_('创建时间'))
    last_oper = models.CharField(max_length=32, null=True, blank=True,
                                  verbose_name=_('最后修改人'))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'raidcard'
        ordering = ['name']