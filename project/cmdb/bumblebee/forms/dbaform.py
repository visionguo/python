#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    dbaform
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from bumblebee.models import Business, SubBusiness, DBA
from django import forms
from django.forms import fields,widgets
from django.utils.translation import ugettext_lazy as _

class DBAForm(forms.Form):
    name = forms.CharField(label=_('数据库集群名'),max_length=255, required=True)
    instance = forms.CharField(label=_('数据库实例'), max_length=255, required=True)
    db_name = forms.CharField(label=_('数据库名'), max_length=255, required=True)
    db_port = forms.CharField(label=_('实例端口'), max_length=255, required=True)
    db_type = forms.ChoiceField(label=_('数据库类型'), choices=DBA.DBTYPE_CHOICES)
    db_statu = forms.ChoiceField(label=_('数据库状态'), choices=[('Used', u'使用中'),('Offline', u'下线')], widget=widgets.Select, required=True)
    person_duty = forms.CharField(label=_('负责人'), max_length=32, required=True)
    business = forms.ModelChoiceField(label=_('所属业务线'), queryset=Business.objects.all())
    subbusiness = forms.ModelChoiceField(label=_('所属子业务'), queryset=SubBusiness.objects.all(), empty_label="---------", required=False)