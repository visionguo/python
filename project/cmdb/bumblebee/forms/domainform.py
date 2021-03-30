#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    domainform
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django import forms
from django.utils.translation import ugettext_lazy as _
from bumblebee.models import Project, Domain, Business, SubBusiness

class DomainForm(forms.Form):
    name = forms.CharField(max_length=128, label=_('域名'), help_text='最大128个字符', required=True)
    ip = forms.CharField(max_length=16,label=_('IP地址'), help_text='最大16个字符',required=False)
    oip = forms.CharField(max_length=16, label=_('外网IP地址'), help_text='最大16个字符', required=False)
    inner_outner = forms.CharField(max_length=16, label=_('对内对外'), help_text='最大16个字符', required=False)
    use_for = forms.CharField(max_length=32, label=_('用途'), help_text='最大32个字符', required=False)
    person_duty = forms.CharField(max_length=32, label=_('负责人'), help_text='最大32个字符', required=False)
    project = forms.ModelChoiceField(label=_('项目'), queryset=Project.objects.all(), empty_label="---------", required=False)
    env = forms.ChoiceField(label=_('环境'), choices=Domain.ENV_CHOICES, required=True)
    business = forms.ModelChoiceField(label=_('所属业务线'), queryset=Business.objects.all(), required=True)
    subbusiness = forms.ModelChoiceField(label=_('所属子业务'), queryset=SubBusiness.objects.all(), empty_label="---------", required=False)