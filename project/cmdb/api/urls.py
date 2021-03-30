#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    urls
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
app_name = 'api'

urlpatterns = [
   """
   Get assest base on hostname
   """
   re_path(r'^asset/$', AssetList, name='queryallasset'),
   re_path(r'^asset/business/(?P<businessname>.+)$', GetAssetByBusiness),
   re_path(r'^asset/subbusiness/(?P<subbusinessname>.+)$', GetAssetBySubBusiness),
   re_path(r'^asset/ip/(?P<IP>.+)$', GetAssetByIP),
   re_path(r'^asset/(?P<hostname>.+)$', GetAssetByHostname, name='queryasset'),

   """
   Get business
   """
   re_path(r'^business/allsub/(?P<businessname>.+)$', GetAllSubBusinessByBusiness, name='queryallsubbyname'),
   re_path(r'^business/$', BusinessList, name='querybusiness'),
   re_path(r'^business/(?P<business>.+)$', GetBusinessByName, name='querybusinessbyname'),

   """
   Get subbusiness
   """
   re_path(r'^subbusiness/$', SubBusinessList, name='querysubbusiness'),
   re_path(r'^subbusiness/(?P<subbusiness>.+)$', GetSubBusinessByName, name='querysubbusinessbyname'),

   """
   Get domain
   """
   re_path(r'^domain/$', DomainList, name='domainlist'),

   """
   Get projects
   """
   re_path(r'^project/$', ProjectList, name='projectslist'),
   re_path(r'^project/name/(?P<projectname>.+)$', GetProjectByName, name='getprojectbyname'),
   re_path(r'^project/online/(?P<onlinehost>.+)',  GetProjectByOnlineHost),
   re_path(r'^project/gray/(?P<grayhost>.+)',  GetProjectByGrayHost),
   re_path(r'^project/pre/(?P<prehost>.+)',  GetProjectByPreHost),
   re_path(r'^project/language/(?P<language>.+)',  GetAppsByLaguage),
   re_path(r'^project/statu/(?P<statu>.+)',  GetProjectByMonitorStatu),

   """
   Get apps
   """
   re_path(r'^apps/$', AppstList, name='applist'),
]

urlpatterns = format_suffix_patterns(urlpatterns)