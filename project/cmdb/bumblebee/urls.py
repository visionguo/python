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

from django.views.static import serve
from django.conf import settings
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *
from .api_views import GetAllAssets, GetAllProjects, GetAllBusiness, GetAllSubBusiness
from .forms import *

app_name = 'bumblebee'

urlpatterns = [
    """
    资产
    """
    re_path(r'^assetslist/$', AssetList, name='assetlist'),
    re_path(r'^assetadd/$', AssetAdd, name='assetadd'),
    re_path(r'^assetsedit/(?P<asset_id>[0-9]+)$', AssetEdit, name='assetedit'),
    re_path(r'^assetdelete/(?P<asset_id>[0-9]+)$', AssetsDelete, name='assetdelete'),
    re_path(r'^assetsedatail/(?P<asset_id>[0-9]+)$', AssetDatail, name='assetdatail'),

    """
    域名
    """
    re_path(r'^domainlist/$', DomainList, name='domainlist'),
    re_path(r'^domainadd/$', DomainAdd, name='domainadd'),
    re_path(r'^domaindelete/(?P<domain_id>[0-9]+)$', DomainDelete, name='domaindelete'),
    re_path(r'^domainedit/(?P<domain_id>[0-9]+)$', DomainEdit, name='domainedit'),

    """
    机房
    """
    re_path(r'^idclist/$', IdcList, name='idclist'),
    re_path(r'^idcdatail/(?P<idc_id>[0-9]+)$', IdcDatail,name='idcdatail'),
    re_path(r'^idcedit/(?P<idc_id>[0-9]+)$', IdcEdit,name='idcedit'),
    re_path(r'^idcdelete/(?P<idc_id>[0-9]+)$', IdcDelete,name='idcdelete'),
    re_path(r'^idcadd/$', IdcAdd, name='idcadd'),

    """
    主业务线
    """
    re_path(r'^businessdatail/$', BusinessDatail, name='businessdatail'),
    re_path(r'^businessadd/$', BusinessAdd, name='businessadd'),
    re_path(r'^businesedit/(?P<business_id>[0-9]+)$', BusinessEdit, name='businessedit'),

    """
    子业务线
    """
    re_path(r'^subbisedatail/$', SubBiseDatail, name='subbisedatail'),
    re_path(r'^subbiseadd/$', SubBiseAdd, name='subbiseadd'),
    re_path(r'^subbiseedit/(?P<subbusiness_id>[0-9]+)$', SubBusibessEdit, name='subbiseedit'),
    re_path(r'^subbisedelete/(?P<subbusiness_id>[0-9]+)$', SubBusibessDelete, name='subbisedelete'),
    re_path(r'^allbusi/$', BusiInfo, name='businfo'),

    """
    网卡
    """
    re_path(r'^niclist/$', NicList, name='niclist'),
    re_path(r'^nicadd/$', NicAdd, name='nicadd'),

    """
    用途
    """
    re_path(r'^purposelist/$', PurposeList, name='purposelist'),
    re_path(r'^purposeadd/$', PurposeAdd, name='purposeadd'),

    """
    项目
    """
    re_path(r'^projectlist/$', ProjectList, name='projectlist'),
    re_path(r'^projectadd/$', ProjectAdd, name='projectadd'),
    re_path(r'^projectdatail/(?P<project_id>[0-9]+)$', ProjectDatail, name='projectdatail'),
    re_path(r'^projectedit/(?P<project_id>[0-9]+)$', ProjectEdit, name='projectedit'),

    """
    RAID卡
    """
    re_path(r'^raidcardlist/$', RaidCardList, name='raidcardlist'),
    re_path(r'^raidcardadd/$', RaidCardAdd, name='raidcardadd'),
    re_path(r'^raidcarddelete/(?P<raidcard_id>[0-9]+)$', RaidCardDelete, name='raidcarddelete'),
    re_path(r'^raidcardedit/(?P<raidcard_id>[0-9]+)$', RaidCardEdit, name='raidcardedit'),

    """
    RAID类型
    """
    re_path(r'^raidtypelist/$', RaidTypeList, name='raidtypelist'),
    re_path(r'^raidtypeadd/$', RaidTypeAdd, name='raidtypeadd'),
    re_path(r'^raidtypedelete/(?P<raidtype_id>[0-9]+)$', RaidTypeDelete, name='raidtypedelete'),

    """
    数据库
    """
    re_path(r'^dbalist/$', DBList, name='dblist'),
    re_path(r'^dbadd/$', DBAdd, name='dbadd'),

    """
    服务或应用
    """
    re_path(r'^appslist/$', AppsList.as_view(), name='appslist'),
    re_path(r'^appsadd/$', AppsAdd.as_view(form_class=AppAddForm), name='appsadd'),
    re_path(r'^appsdelete/(?P<app_id>[0-9]+)$', AppsDelete, name='appdelete'),

    """
    jumpserver
    """
    re_path(r'^fort/$', Fort, name='fort'),
    re_path(r'^activefort/$', ActiveFort, name='activefort'),
    re_path(r'^updatefort/$', UpFortUser, name='updatefort'),
    re_path(r'^changephone/$', GetCheckNum, name='changephone'),

    """
    ip management
    """
    re_path(r'^outiplist/$', OutIPList.as_view(), name='outiplist'),
    re_path(r'^outipadd/$', OutIPAdd, name='outipadd'),

    """
    API
    """
    """
    assets
    """
    re_path(r'^api/allassets/$', GetAllAssets.as_view()),

    """
    projects
    """
    re_path(r'^api/projects/$', GetAllProjects.as_view()),

    """
    business
    """
    re_path(r'^api/business/$', GetAllBusiness.as_view()),
    re_path(r'^api/subbusiness/$', GetAllSubBusiness.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)