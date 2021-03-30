#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    serializers
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from rest_framework import serializers
from bumblebee.models import Asset, Business, SubBusiness, Domain, Project
from bumblebee.models import *

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = (
        'id', 'hostname', 'ip', 'cip', 'vip', 'mem', 'cpu', 'disk', 'os',
        'hosttype', 'env', 'statu', 'exist', 'platform', 'manufacture',
        'server_model', 'sn', 'out_use', 'idc', 'cabinet_no', 'cabinet_pos',
        'created_by', 'date_created', 'comment', 'business_name', 'nic', 'mac',
        'purpose', 'raidcard', 'raidtype', 'subbusiness_name')

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'name', 'name_english', 'person_duty', 'org_id', 'sre')

class SubBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubBusiness
        fields = ('id', 'name', 'name_english', 'business', 'person', 'sre')

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('id', 'name', 'ip', 'oip', 'inner_outner', 'use_for', 'person_duty', 'project', 'env', 'business', 'subbusiness')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'port', 'language', 'prehost', 'grayhost', 'onlinehost', 'sub_business', 'tag', 'git', 'git_group', 'monitorchoice', 'monitorenv', 'monitor_url')

class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = ('id', 'name', 'host', 'port', 'uri')