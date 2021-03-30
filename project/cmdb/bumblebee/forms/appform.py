#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    appform
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.forms import ModelForm
from bumblebee.models import Apps
from django.utils.translation import gettext_lazy as _

class AppAddForm(ModelForm):
    class Meta:
        model = Apps
        fields = ['host', 'port']