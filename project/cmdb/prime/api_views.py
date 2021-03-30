#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    api_views
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from .models.department import Department

from .serializers import DepartmentSerializer

from rest_framework import mixins
from rest_framework import generics

class GetDepartments(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)