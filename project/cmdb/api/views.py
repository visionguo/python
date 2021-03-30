#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    views
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import mixins, generics, status
from django.shortcuts import HttpResponse
from dss.Serializer import serializer

from bumblebee.models import Asset, Business, SubBusiness, Domain, Project
from bumblebee.models import *

from .serializers import AssetSerializer, BusinessSerializer, SubBusinessSerializer, DomainSerializer, ProjectSerializer, AppsSerializer

__all__ = ['AssetList', 'GetAssetByHostname', 'GetAssetByBusiness', 'GetAssetBySubBusiness', 'BusinessList',
           'GetBusinessByName', 'SubBusinessList', 'GetProjectByGrayHost', 'GetSubBusinessByName', 'DomainList',
           'ProjectList', 'GetProjectByName', 'GetProjectByOnlineHost', 'GetProjectByPreHost', 'GetAppsByLaguage',
           'GetProjectByMonitorStatu', 'AppstList', 'GetAllSubBusinessByBusiness', 'GetAssetByIP']

@api_view(['GET'])
def api_root(request, format=None):
    return  Response({
        'assets': reverse('GetAllAssets', request=request, format=format)
    })

class GetAllAssets(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

@api_view(['GET'])
def AssetList(request):
    """
    list all assets
    """
    if request.method == 'GET':
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetAssetByHostname(request, hostname, format=None):
    """
    Get info of specific asset by hostname
    """
    try:
        asset = Asset.objects.get(hostname=hostname)
    except Asset.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AssetSerializer(asset)
        return Response(serializer.data)

@api_view(['GET'])
def GetAssetByBusiness(request, businessname, format=None):
    """
    Get all assets by business name
    """
    try:
        busi = Business.objects.filter(name__contains=businessname).first()
        asset = Asset.objects.filter(business=busi.id)
    except Business.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssetSerializer(asset, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetAssetBySubBusiness(request, subbusinessname, format=None):
    """
    Get all assets by subbusiness name
    """
    try:
        sub = SubBusiness.objects.filter(name__contains=subbusinessname).first()
        asset = Asset.objects.filter(sub_business=sub.id)
    except SubBusiness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssetSerializer(asset, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def BusinessList(request):
    """
    list all businesses
    """
    if request.method == 'GET':
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetBusinessByName(request, business, format=None):
    """
    Get info of specific business by name
    """
    try:
        asset = Business.objects.get(name=business)
    except Business.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BusinessSerializer(asset)
        return Response(serializer.data)

@api_view(['GET'])
def GetAllSubBusinessByBusiness(reqeust, businessname):
    ret = {}
    business = Business.objects.filter(name=businessname)
    if reqeust.method == 'GET':
        if len(business) == 0:
            ret['code'] = 200
            ret['msg'] = 'business not exist'
            ret['data'] = 'null'
            data = serializer(ret, output_type='json')
            return HttpResponse(data)
        else:
            ret['code'] = 200
            ret['msg'] = 'success'
            ret['data'] = {}
            ret['data']['sub'] = []
            bus = Business.objects.get(name=businessname)
            ret['data']['id'] = bus.id
            ret['data']['name'] = bus.name
            ret['data']['leader'] = bus.person_duty
            ret['data']['sre'] = bus.sre
            subs = SubBusiness.objects.filter(business=bus.id)
            for sub in subs:
                s = {}
                s['id'] = sub.id
                s['name'] = sub.name
                s['leader'] = sub.person
                s['sre'] = sub.sre
                ret['data']['sub'].append(s)
            data = serializer(ret, output_type='json')
            return HttpResponse(data)

@api_view(['GET'])
def GetAssetByIP(reqeust, IP):
    ret = {}
    IPList = IP.strip().split('.')
    if reqeust.method == 'GET':
        if len(IPList) != 4:
            ret['code'] = 200
            ret['msg'] = 'illegal ip'
            ret['data'] = 'null'

            data = serializer(ret, output_type='json')
            return HttpResponse(data)
        else:
            ret['code'] = 200
            for i in range(4):
                try:
                    IPList[i] = int(IPList[i])
                except:
                    ret['msg'] = 'ip not int'
                    ret['data'] = 'null'
                    data = serializer(ret, output_type='json')
                    return HttpResponse(data)
            for i in range(4):
                if int(IPList[i]) <= 255 and int(IPList[i]) >= 0:
                    asset = Asset.objects.filter(ip=IP)
                    if len(asset) == 0:
                        ret['code'] = 200
                        ret['msg'] = 'ip not exist'
                        ret['data'] = 'null'
                        data = serializer(ret, output_type='json')
                        return HttpResponse(data)
                    else:
                        ret['code'] = 200
                        ret['msg'] = 'success'
                        ret['data'] = {}
                        host = Asset.objects.get(ip=IP)

                        ret['data']['hostname'] = host.hostname
                        if host.business is not None:
                            ret['data']['business'] = host.business_name
                            business = Business.objects.get(id=host.business_id)
                            ret['data']['business_manager'] = business.person_duty
                            if host.sub_business is not None:
                                ret['data']['sub_business'] = host.subbusiness_name
                                sub = SubBusiness.objects.get(id=host.sub_business_id)
                                ret['data']['sub_manager'] = sub.person
                        else:
                            ret['data']['business'] = 'None'
                            ret['data']['business_manager'] = "None"
                            ret['data']['sub_business'] = "None"
                            ret['data']['sub_manager'] = "None"
                        data = serializer(ret, output_type='json')
                        return HttpResponse(data)

@api_view(['GET'])
def SubBusinessList(request):
    """
    list all subbusinesses
    """
    if request.method == 'GET':
        subbusinesses = SubBusiness.objects.all()
        serializer = SubBusinessSerializer(subbusinesses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetSubBusinessByName(request, subbusiness, format=None):
    """
    Get info of specific subbusiness by name
    """
    try:
        asset = SubBusiness.objects.get(name=subbusiness)
    except SubBusiness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SubBusinessSerializer(asset)
        return Response(serializer.data)

@api_view(['GET'])
def DomainList(request):
    """
    get all domains
    """
    if request.method == 'GET':
        domain = Domain.objects.all()
        serializer = DomainSerializer(domain, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def ProjectList(request):
    """
    get all projects from earthworm
    """
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetProjectByName(request, projectname, format=None):
    """
    Get info of specific project by name
    """
    try:
        project = Project.objects.get(name=projectname)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

@api_view(['GET'])
def GetProjectByOnlineHost(request, onlinehost, format=None):
    """
    Get all projects by OnlineHost
    """
    try:
        project = Project.objects.filter(onlinehost__contains=onlinehost)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetProjectByGrayHost(request, grayhost, format=None):
    """
    Get all projects by OnlineHost
    """
    try:
        project = Project.objects.filter(grayhost__contains=grayhost)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetProjectByPreHost(request, prehost, format=None):
    """
    Get all projects by PreHost
    """
    try:
        project = Project.objects.filter(prehost__contains=prehost)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetProjectByMonitorStatu(request, statu, format=None):
    """
    Get all projects by monitor statu
    """
    try:
        project = Project.objects.filter(monitorchoice__contains=statu)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def GetAppsByLaguage(request, language, format=None):
    """
    Get all projects  by program language
    """
    try:
        project = Project.objects.filter(language__contains=language)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def AppstList(request):
    """
    Get all app or service monitoring
    """
    if request.method == 'GET':
        apps = Apps.objects.all()
        serializer = AppsSerializer(apps, many=True)
        return Response(serializer.data)