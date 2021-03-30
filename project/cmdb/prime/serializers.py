#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    templates/serializers
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from rest_framework import serializers
from .models.department import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'leader', 'departmentid')
        def create(self, validated_data):
            """
            Create and return a new `Snippet` instance, given the validated data.
            """
            return Department.objects.create(**validated_data)