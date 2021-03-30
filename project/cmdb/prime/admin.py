#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    templates/admin
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.contrib import admin
# Register your models here.

from .models import User, Department, Groups

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name', 'phone', 'department', 'group')

admin.site.register(User, UserAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader')

admin.site.register(Department, DepartmentAdmin)

class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'department')

admin.site.register(Groups, GroupsAdmin)