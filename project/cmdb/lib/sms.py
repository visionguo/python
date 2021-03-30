#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    sms
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import requests
import time
import base64
import hashlib
import hmac
import uuid
from urllib.parse import urlencode, quote_plus

SENDURL = 'http://misc.xxx-int.com/api/sms/sendMessage'
CHECKURL = 'http://misc.xxx-int.com/api/sms/getPhoneCode'

SMS_APP_KEY = ''
APP_SECRET = ''
serviceId = ''

def signature(payload):
    """
    签名
    """
    sort_tuple = [(k, payload[k]) for k in sorted(payload)]
    urlencoded = urlencode(sort_tuple, quote_via=quote_plus)
    m = hmac.new(APP_SECRET, urlencoded.encode('utf-8'), hashlib.sha256)
    m = base64.b64encode(m.digest())
    m = hashlib.md5(m).hexdigest()
    return m[5:15]

def sendmsm(phone):
    """
    发送短信
    """
    payload = {
        'appkey': SMS_APP_KEY,
        'expires': int(time.time()) + 200,
        'nonce': str(uuid.uuid4()),
        'phones': phone,
        'serviceId': serviceId,
    }
    sig = signature(payload)
    payload['signature'] = sig
    r = requests.post(SENDURL, data=payload)
    return r.json()

def getphonecode(phone):
    """
    获取手机号码
    """
    payload = {
        'appkey': SMS_APP_KEY,
        'expires': int(time.time()) + 200,
        'nonce': str(uuid.uuid4()),
        'phone': phone,
        'serviceId': serviceId,
    }
    sig = signature(payload)
    payload['signature'] = sig
    r = requests.get(CHECKURL, params=payload)
    if len(r.json()['data']) != 0:
        return r.json()['data']['code']