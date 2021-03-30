#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    fort
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import requests

Basic = "http://fortuser.xxx-int.com/fort/"
Appkey = "89951655"
FortApi = 'https://fort.xxx-int.com:8081/'

ActiveApi = "{}api/sysUser/regist".format(Basic)

headers = {
    'identity': '1',
    'token': '123456'
}

def ActiveUser(username):
    payload = {
        "loginName": username
    }
    ret = requests.post(ActiveApi,data=payload)
    return ret.json()

def UpdateFortUser(username):
    UpApi = "{}api/identity/reset/totpmobile/byname/".format(FortApi)
    payload = {
        "login": username
    }

    ret = requests.post(UpApi, headers=headers, data=payload)
    return ret.json()