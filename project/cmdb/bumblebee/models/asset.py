#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    asset
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

__all__ = ['Asset']

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .business import Business
from .idc import IDC
from .nic import Nic
from .purpose import Purpose
from .raidcard import RaidCard
from .raidtype import RaidType
from .sub_business import SubBusiness

class Asset(models.Model):
    """
    定义资产状态
    """
    STATUS_CHOICES = (
        ('Used', u'使用中'),
        ('Offline', u'下线'),
        ('Power Off', u'关机'),
        ('Free', u'空闲'),
        ('FailOver', u'故障'),
        ('Preloader', u'预装机'),
    )
    ENV_CHOICES = (
        ('Prod', u'生产'),
        ('PreProd', u'预生产'),
        ('Dev', u'开发'),
        ('Gray', u'灰度'),
        ('Test', u'测试'),
    )
    PLATFORM_CHOICES = (
        ('CentOS', 'CentOS'),
        ('Redhat', 'Redhat'),
        ('Ubuntu', 'Ubuntu'),
        ('XenServer', 'XenServer'),
        ('Windows', 'Windows'),
        ('Other', 'Other'),
    )
    HOST_TYPE_CHOICES = (
        ('PM', u'物理机'),
        ('VM', u'虚拟机'),
        ('Route', u'路由器'),
        ('Switch', u'交换机'),
        ('FireWall', u'防火墙'),
        ('Sec', u'安全设备'),
    )
    
    hostname = models.CharField(max_length=32, unique=True, verbose_name=_('主机名'))
    ip = models.CharField(max_length=16, unique=True, verbose_name=_('IP地址'))
    cip = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('管理IP'))
    vip = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('虚拟IP'))
    mem = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('内存'))
    cpu = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('CPU'))
    disk = models.CharField(max_length=128,blank=True, null=True, verbose_name=_('磁盘'))
    os = models.CharField(max_length=32, blank=True, null=True,  verbose_name=_('系统版本'))
    hosttype = models.CharField(choices=HOST_TYPE_CHOICES, max_length=16, blank=True, null=True, default='VM', verbose_name=_('主机类型'))
    env = models.CharField(choices=ENV_CHOICES, max_length=8, blank=True, null=True, default='Prod', verbose_name=_('服务器环境'))
    statu = models.CharField(choices=STATUS_CHOICES, max_length=16, null=True, blank=True, default='Used', verbose_name=_('服务器状态'))
    exist = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('宿主机'))
    platform = models.CharField(choices=PLATFORM_CHOICES, max_length=16, blank=True, null=True, default='CentOS', verbose_name=_('系统类别'))

    """
    information of server
    """
    manufacture = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('厂商'))
    server_model = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('服务器型号'))
    sn = models.CharField(max_length=32, blank=True, null=True, verbose_name=_('序列号'))
    out_use = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('过保时间'))

    """
    information of servers's postion in idc
    """
    idc = models.ForeignKey(IDC, blank=True, null=True, related_name='assets', on_delete=models.SET_NULL, verbose_name=_('所在机房'))
    cabinet_no = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('机柜号'))
    cabinet_pos = models.CharField(max_length=11, null=True, blank=True, verbose_name=_('托盘位置'))

    """
    information of servers's creation time
    """
    created_by = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('创建人'))
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('创建时间'))
    comment = models.CharField(max_length=128, default='', blank=True, null=True,  verbose_name=_('备注'))

    """
    other information
    """
    business = models.ForeignKey(Business, blank=True, null=True, related_name='assets', on_delete=models.SET_NULL, verbose_name=_('所属业务线'))
    nic = models.ForeignKey(Nic, blank=True, null=True, related_name='assets', on_delete=models.SET_NULL, verbose_name=_('网卡'))
    mac = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('MAC地址'))

    purpose = models.ForeignKey(Purpose, null=True, blank=True, related_name='assets', on_delete=models.SET_NULL, verbose_name=_('用途'))
    raidcard = models.ForeignKey(RaidCard, null=True, blank=True, related_name='assets', on_delete=models.SET_NULL, verbose_name=_('Raid卡'))
    raidtype = models.ForeignKey(RaidType, null=True, blank=True, related_name='assets',  on_delete=models.SET_NULL, verbose_name=_('Raid类型'))
    sub_business = models.ForeignKey(SubBusiness, null=True, blank=True, related_name='assets',  on_delete=models.SET_NULL, verbose_name=_('子业务'))

    def __repr__(self):
        return self.hostname
    
    def __str__(self):
        return self.__repr__()
    
    class Meta:
        db_table = 'asset'
        ordering = ['hostname']

    @property
    def business_name(self):
        return self.business.name

    @property
    def subbusiness_name(self):
        return self.sub_business.name