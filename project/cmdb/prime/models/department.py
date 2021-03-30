#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    department
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = ['Department']

class Department(models.Model):
    name = models.CharField(max_length=16, db_index=True, verbose_name=_('部门'))
    leader = models.CharField(max_length=31, blank=True, null=True, verbose_name=_('部门负责人'))
    departmentid = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('部门ID'))
    simple_name = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('简写'))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'departments'
        ordering = ['name']