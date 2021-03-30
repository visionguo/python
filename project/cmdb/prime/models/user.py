#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    user
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .department import Department
from .group import Groups
from bumblebee.models import Business
from bumblebee.models import SubBusiness

__all__ = ['User']

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True, verbose_name=_('用户名'))
    password = models.CharField(max_length=255, verbose_name=_('密码'))
    name = models.CharField(max_length=20, verbose_name=_('姓名'))
    email = models.EmailField(max_length=64, unique=True, verbose_name=_('邮箱'))
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('手机'))
    department = models.ForeignKey(Business, null=True, blank=True,
                                   related_name='department',
                                   on_delete=models.SET_NULL,
                                   verbose_name=_('所属部门'))
    group = models.ForeignKey(SubBusiness, related_name='group', blank=True,
                              null=True, on_delete=models.SET_NULL,
                              verbose_name=_('所属小组'))
    date_created = models.DateTimeField(auto_now_add=True, null=True,
                                        verbose_name=_('创建日期'))
    comment = models.TextField(max_length=200, blank=True, verbose_name=_('备注'))

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'users'
        ordering = ['date_created']
