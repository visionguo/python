#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    group
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import gettext_lazy as _
from .department import Department

__all__ =['Groups']

class Groups(models.Model):
    name = models.CharField(max_length=16, db_index=True, verbose_name=_('小组'))
    manager = models.CharField(max_length=32, blank=True, null=True, verbose_name=_("小组负责人"))
    simple_name = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('简写'))
    department = models.ForeignKey(Department, related_name='departments', blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('所属部门'))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'groups'
        ordering = ['name']