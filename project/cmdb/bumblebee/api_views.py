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

from .models.asset import Asset
from .models.projects import Project
from .models.business import Business
from .models.sub_business import SubBusiness

from .serializers import AssetSerializer, ProjectSerializer, BusinessSerializer, SubBusinessSerializer
from rest_framework import mixins
from rest_framework import generics

class GetAllAssets(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class GetAllProjects(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class GetAllBusiness(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class GetAllSubBusiness(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = SubBusiness.objects.all()
    serializer_class = SubBusinessSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)