#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    outips
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .business import Business
from .sub_business import SubBusiness

__all__ = ['OutIPS']

class OutIPS(models.Model):
    DOMAIN_CHOICES = (
        ('xxx', u'xxx'),
        ('yyy', u'yyy'),
    )
    ipaddress = models.CharField(max_length=16,verbose_name=_('外网IP地址'))
    innerip = models.CharField(max_length=16,default='None',verbose_name=_('映射内网IP'))
    business = models.ForeignKey(Business, null=True, blank=True, related_name='ip_bu', on_delete=models.SET_NULL, verbose_name=_('所属主业务'))
    subbusiness = models.ForeignKey(SubBusiness, null=True, blank=True, related_name='ip_sub', on_delete=models.SET_NULL, verbose_name=_('所属子业务'))
    domain = models.CharField(choices=DOMAIN_CHOICES, max_length=8, blank=True, null=True, default='Prod', verbose_name=_('域名归属'))

    def __repr__(self):
        return self.ipaddress

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'outip'
        ordering = ['ipaddress']
        default_permissions = ()
        permissions = (
            ("view_outip", u"查看外网IP"),
            ("edit_outip", u"编辑外网IP"),
            ("delete_outip", u"删除外网IP"),
            ("add_outip", u"添加外网IP"),
        )
        verbose_name = u'外网IP管理'
        verbose_name_plural = u'外网IP管理'