#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    outipform
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django import forms
from django.utils.translation import ugettext_lazy as _
from bumblebee.models import Business, SubBusiness, OutIPS

class OutIPForm(forms.Form):
    ipaddress = forms.CharField(max_length=16,label=_('外网IP地址'), help_text='最大16个字符',required=True)
    innerip = forms.CharField(max_length=16,label=_('映射内网IP'), help_text='最大16个字符',required=True)
    business = forms.ModelChoiceField(label=_('所属业务线'), queryset=Business.objects.all(), required=True)
    subbusiness = forms.ModelChoiceField(label=_('所属子业务'), queryset=SubBusiness.objects.all(), empty_label="---------", required=False)
    domain = forms.ChoiceField(label=_('服务器环境'), choices=OutIPS.DOMAIN_CHOICES, required=True)