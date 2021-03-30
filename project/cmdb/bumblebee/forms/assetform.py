#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    assetform
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from bumblebee.models import Asset, Business, SubBusiness, IDC, Nic, Purpose, RaidCard, RaidType

class AssetForm(forms.Form):
    hostname = forms.CharField(max_length=32, label=_('主机名'), help_text='最大32个字符', required=True)
    ip = forms.CharField(max_length=16, label=_('IP地址'), help_text='最大16个字符', required=True)
    cip = forms.CharField(max_length=16, label=_('远程管理卡IP'), help_text='最大16个字符', required=False)
    vip = forms.CharField(max_length=16, label=_('虚拟IP'), help_text='最大255个字符', required=False)
    disk = forms.CharField(max_length=128, label=_('磁盘'), help_text='最大128个字符', required=False)
    mac = forms.CharField(max_length=32, help_text='最大32个字符', label=_('MAC地址'), required=False)
    hosttype = forms.ChoiceField(label=_('主机类型'), choices=Asset.HOST_TYPE_CHOICES, required=True)
    env =  forms.ChoiceField(label=_('服务器环境'), choices=Asset.ENV_CHOICES, required=True)
    statu = forms.ChoiceField(label=_('服务器状态'), choices=Asset.STATUS_CHOICES, required=True)
    platform = forms.ChoiceField(label=_('系统类型'), choices=Asset.PLATFORM_CHOICES, required=True)
    exist = forms.CharField(max_length=32, label=_('宿主机'), required=False)
    manufacture = forms.CharField(max_length=128, help_text='最大128个字符', label=_('服务器厂商'), required=False)
    server_model = forms.CharField(max_length=16, help_text='最大16个字符', label=_('服务器型号'), required=False)
    sn = forms.CharField(max_length=32, help_text='最大32个字符', label=_('服务器序列号'), required=False)
    out_use = forms.CharField(label=_('过保时间'), required=False)
    idc = forms.ModelChoiceField(queryset=IDC.objects.all(), label=_('所在机房'), required=True)
    cabinet_no = forms.CharField(help_text='最大32个字符', label=_('所在机柜'), required=False)
    cabinet_pos = forms.IntegerField(help_text='最大32个字符', label=_('托盘位置'), required=False)
    business = forms.ModelChoiceField(label=_('所属业务线'), queryset=Business.objects.all(), required=True)
    subbusiness = forms.ModelChoiceField(label=_('所属子业务'), queryset=SubBusiness.objects.all(), empty_label="---------", required=False)
    nic = forms.ModelChoiceField(label=_('网卡'), queryset=Nic.objects.all(), empty_label="---------", required=False)
    purpose = forms.ModelChoiceField(label=_('用途'), queryset=Purpose.objects.all(), empty_label="---------")
    raidcard = forms.ModelChoiceField(label=_('RAID卡'), queryset=RaidCard.objects.all(), empty_label="---------", required=False)
    raidtype = forms.ModelChoiceField(label=_('RAID类型'), queryset=RaidType.objects.all(), empty_label="---------", required=False)