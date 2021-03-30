#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/07/15
# Brief:
#    views
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello, World!')

def login(request):
    return render(request, 'accounts_login.html')
    pass
