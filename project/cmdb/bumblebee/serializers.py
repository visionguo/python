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
from .models.asset import Asset
from .models.projects import Project
from .models.business import Business
from .models.sub_business import SubBusiness

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'name', 'name_english', 'org_id')

class SubBusinessSerializer(serializers.ModelSerializer):
    business_name = serializers.ReadOnlyField()
    class Meta:
        model = SubBusiness
        fields = ('id', 'name', 'name_english', 'business_name', 'person')

class AssetSerializer(serializers.ModelSerializer):
    business_name = serializers.ReadOnlyField()
    subbusiness_name = serializers.ReadOnlyField()
    class Meta:
        model = Asset
        fields = ('id', 'hostname', 'ip', 'cip', 'sn', 'platform', 'business_name', 'subbusiness_name', 'os', 'statu', 'cabinet_no', 'cabinet_pos', 'hosttype')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Asset.objects.create(**validated_data)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'port', 'language', 'sub_business', 'grayhost', 'onlinehost', 'prehost', 'tag', 'git', 'git_group', 'exporter_port')

        def create(self, validated_data):
            """
            Create and return a new `Snippet` instance, given the validated data.
            """
            return Asset.objects.create(**validated_data)
