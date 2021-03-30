#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    business
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = ['Business']

class Business(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('业务线'))
    name_english = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('英文简写'))
    person_duty = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('总负责人'))
    manager = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('负责人中文名'))
    org_id = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('ORG编号'))
    sre = models.CharField(max_length=252, default="None", verbose_name=_("SRE"))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'business'
        ordering = ['name']