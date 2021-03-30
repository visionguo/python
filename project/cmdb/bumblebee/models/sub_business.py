#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    sub_business
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .business import Business

__all__ = ['SubBusiness']

class SubBusiness(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('子业务线'))
    name_english = models.CharField(max_length=16, blank=True, null=True,
                                    verbose_name=_('英文简写'))
    business = models.ForeignKey(Business, null=True, blank=True, related_name='business', on_delete=models.SET_NULL,verbose_name=_('所属业务线'))
    person = models.CharField(max_length=32, verbose_name=_('业务负责人'))
    manager = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('负责人中文名'))
    sre = models.CharField(max_length=252, default="None", verbose_name=_("SRE"))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'subbusiness'
        ordering = ['name']

    @property
    def business_name(self):
        return self.business.name