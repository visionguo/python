#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    templates/usrls
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *
from .api_views import GetDepartments

app_name = 'prime'

urlpatterns = [
   re_path(r'^useradd/$', UserAdd, name='useradd'),
   re_path(r'^userlist/$', UserList, name='userlist'),
   re_path(r'^useredit/(?P<user_id>[0-9]+)$', UserEdit, name='useredit'),
   re_path(r'^userdatail/(?P<user_id>[0-9]+)$', UserDatail, name='userdatail'),
   re_path(r'^login/$', Login, name='login'),
   re_path(r'^register/$', Register, name='register'),

   # API
   re_path(r'^api/departments/$', GetDepartments.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)