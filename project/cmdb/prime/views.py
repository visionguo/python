#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    templates/views
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.shortcuts import render

# Create your views here.

__all__ = ['Login', 'UserAdd', 'UserList', 'UserDatail', 'UserEdit', 'Register']

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from .models import *
from bumblebee.models import Business, SubBusiness

from django.contrib.auth.models import Permission

def Login(request):
    """
    登录
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            print("{} 不存在".format(username))
            return render(request, '../templates/login.html')
    return render(request, '../templates/login.html')

def Logou(request):
    """
    注销
    """
    logout(user)
    return HttpResponseRedirect(reverse("prime:login"))

def Register(request):
    """
    注册
    """
    if request.method == 'POST':
        username = request.POST['username']
        passwd = make_password(str(request.POST['passwd']))
        email = request.POST['email']
        name = request.POST['name']
        find_user = User.objects.filter(username=username).first()
        if find_user == None:
            user = User.objects.create(username=username, password=passwd,
                                       email=email, name=name, is_staff=1)
            user.save()
            return redirect(reverse('prime:login'))
        else:
            print("{}已存在".format(username))
    return render(request, '../templates/register.html')

@login_required(login_url='prime.login')
@permission_required('prime.Can add user', login_url='/prime/userlist/')
@require_http_methods(['GET', 'POST'])
def UserAdd(request):
    """
    添加用户
    """
    permissions = Permission.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        permission_select = request.POST.getlist('permission')
        permission = [Permission.objects.get(id=p_id) for p_id in permission_select]
        password = make_password(str(request.POST['password']))
        email = request.POST['email']
        name = request.POST['name']
        find_user = User.objects.filter(username=username).first()
        if find_user == None:
            user = User.objects.create(username=username, password=password, email=email, name=name, is_staff=1)
            user.user_permissions.set(permission)
            user.save()
            return redirect(reverse('prime:userlist'))
        else:
            print("{}已存在".format(username))
    return render(request, '../templates/useradd.html', {'permissions': permissions})

@login_required(login_url='prime.login')
def UserList(request):
    """
    用户列表
    """
    users = User.objects.all()
    return render(request,'../templates/userlist.html', {'users':users})

@login_required(login_url='prime.login')
@permission_required('prime.change_user', login_url='/prime/userlist/')
def UserEdit(request, user_id):
    """
    用户编辑
    """
    permissions = Permission.objects.all()
    user = User.objects.filter(id=user_id)
    groups = SubBusiness.objects.all()
    departments = Business.objects.all()

    return render(request, '../templates/useredit.html', locals())

@login_required(login_url='prime.login')
def UserDatail(request, user_id):
    user_ret = User.objects.filter(id=user_id)
    return render(request, '../templates/userdatail.html', locals())