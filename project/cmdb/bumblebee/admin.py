#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    admin
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.contrib import admin
# Register your models here.
from .models import Asset

class AssetAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip', 'mem', 'cpu', 'business')

admin.site.register(Asset, AssetAdmin)

