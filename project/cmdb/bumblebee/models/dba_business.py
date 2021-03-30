#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    dba_business
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .business import Business
from .sub_business import SubBusiness
__all__ = ['DBA']

class DBA(models.Model):
    STATUS_CHOICES = (
        ('Used', u'使用中'),
        ('Offline', u'下线'),
    )

    DBTYPE_CHOICES = (
        ('MySQL', _('MySQL')),
        ('Oracle', _('Oracle')),
        ('Redis', _('Redis')),
        ('Mongo', _('Mongodb')),
        ('Memcache', _('Memcache')),
        ('PostSQL', _('Postgresql')),
    )

    dbid = models.CharField(max_length=128, auto_created=True, null=False, blank=False, verbose_name=_('编号'))
    name = models.CharField(max_length=256, blank=False, null=False, verbose_name=_('数据库集群名'))
    instance = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('数据库实例'))
    db_name = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('数据库名'))
    db_type = models.CharField(choices=DBTYPE_CHOICES, max_length=32,default='MySQl', verbose_name=_('数据库类型'))
    db_port = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('实例端口'))
    db_statu = models.CharField(choices=STATUS_CHOICES, max_length=16, null=True, blank=True, default='Used', verbose_name=_('数据库状态'))
    business = models.ForeignKey(Business, blank=True, null=True, related_name='db_business', on_delete=models.SET_NULL, verbose_name=_('所属业务线'))
    subbusiness = models.ForeignKey(SubBusiness, null=True, blank=True, related_name='db_subbusiness',  on_delete=models.SET_NULL, verbose_name=_('子业务'))
    person_duty = models.CharField(max_length=32, null=True, blank=True, default='None', verbose_name=_('负责人'))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'dba'
        ordering = ['name']