#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    domain
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .projects import Project
from .sub_business import SubBusiness, Business
__all__ = ['Domain']

class Domain(models.Model):
    ENV_CHOICES = (
        ('Prod', _('生产')),
        ('PreProd', _('预生产')),
        ('Gray', _('灰度')),
        ('Test', _('测试')),
    )

    name = models.CharField(max_length=128,verbose_name=_('域名'))
    ip = models.CharField(max_length=16,verbose_name=_('IP地址'))
    oip = models.CharField(max_length=16,verbose_name=_('外网IP'))
    inner_outner = models.CharField(max_length=16, null=False, blank=False, verbose_name=_('对内对外'))
    use_for = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('用途'))
    person_duty = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('负责人'))
    project = models.ForeignKey(Project, null=True, blank=True, related_name='projects', on_delete=models.SET_NULL, verbose_name=_('项目'))
    env = models.CharField(choices=ENV_CHOICES, max_length=8, blank=True,
                           null=True, default='Prod', verbose_name=_('环境'))
    business = models.ForeignKey(Business, null=True, blank=True, related_name='domain', on_delete=models.SET_NULL, verbose_name=_('主业务'))
    subbusiness = models.ForeignKey(SubBusiness, null=True, blank=True, related_name='subbusiness',  on_delete=models.SET_NULL, verbose_name=_('子业务'))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'domain'
        ordering = ['name']