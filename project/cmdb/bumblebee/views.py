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

# Create your views here.

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from lib.getres import GetCpu, GetMem, GetOS

from config import Config

from .models import *
from prime.models import *
import requests
import json
import logging
from lib.fort import ActiveUser, UpdateFortUser
from lib.c4log import LogInfo

from .forms import AppAddForm
from .forms.dbaform import DBAForm
from .forms.assetform import AssetForm
from .forms.domainform import DomainForm
from .forms.outipform import OutIPForm

"""
use generic view
"""
from django.views.generic import ListView, View
from django.db.models import Count

logger = logging.getLogger(__name__)

__all__ = ['Index', 'AssetList', 'AssetAdd', 'AssetEdit', 'AssetDatail', 'AssetsDelete', 'DomainList', 'DomainAdd', 'DomainDelete', 'DomainEdit', 'IdcList',
           'IdcDatail', 'IdcEdit', 'IdcAdd', 'IdcDelete', 'BusinessDatail', 'BusinessAdd', 'BusinessEdit', 'SubBiseDatail', 'SubBiseAdd', 'SubBusibessEdit', 'SubBusibessDelete', 'BusiInfo', 'NicList', 'NicAdd', 'PurposeList',
           'PurposeAdd', 'ProjectList', 'ProjectAdd', 'ProjectDatail', 'ProjectEdit', 'RaidCardList', 'RaidCardAdd', 'RaidCardDelete', 'RaidCardEdit', 'RaidTypeList', 'RaidTypeAdd', 'RaidTypeDelete',
           'DBList', 'DBAdd', 'AppsList', 'AppsAdd', 'AppsDelete', 'Fort', 'ActiveFort', 'UpFortUser', 'GetCheckNum', 'OutIPList', 'OutIPAdd']

@login_required
def Index(request):
    server_count = Asset.objects.count()
    vm_count = Asset.objects.filter(hosttype='VM').count()
    pm_count = Asset.objects.filter(hosttype='PM').count()
    xen_count = Asset.objects.filter(platform__contains='XenServer').count()
    earthworm_count = Project.objects.count()

    ## 新零售
    nr = Business.objects.get(name='新零售')
    nr_count = Asset.objects.filter(business=nr.id).count()
    ##  智能电销服务器数
    kf = Business.objects.get(name='智能电销')
    kf_count = Asset.objects.filter(business=kf.id).count()
    ## 智能平台服务器数
    ai = Business.objects.get(name='智能平台')
    ai_count = Asset.objects.filter(business=ai.id).count()
    ##  车后服务服务器数
    am = Business.objects.get(name='车后服务')
    am_count = Asset.objects.filter(business=am.id).count()
    ## 智能创新平台服务器数
    iip = Business.objects.get(name='智能创新平台')
    iip_count = Asset.objects.filter(business=iip.id).count()
    ## 金融
    jr = Business.objects.get(name='金融')
    jr_count = Asset.objects.filter(business=jr.id).count()
    ## 数据平台
    bi = Business.objects.get(name='数据平台')
    bi_count = Asset.objects.filter(business=bi.id).count()
    ## 大交易交易平台
    trade = Business.objects.get(name="大交易增长平台")
    trade_count = Asset.objects.filter(business=trade.id).count()
    ## 基础架构
    infra = Business.objects.get(name='基础架构')
    infra_count = Asset.objects.filter(business=infra.id).count()
    ## 新车
    nc = Business.objects.get(name='新车')
    nc_count = Asset.objects.filter(business=nc.id).count()
    ## 车速拍
    c2b = Business.objects.get(name='车速拍')
    c2b_count = Asset.objects.filter(business=c2b.id).count()
    ## 共享平台
    sp = Business.objects.get(name='共享平台')
    sp_count = Asset.objects.filter(business=sp.id).count()
    ## 质量保障部
    qa = Business.objects.get(name='质量保障')
    qa_count = Asset.objects.filter(business=qa.id).count()
    ## 运维部
    op = Business.objects.get(name='运维部')
    op_count = Asset.objects.filter(business=op.id).count()
    ## 信息安全部
    sec = Business.objects.get(name='信息安全部')
    sec_count = Asset.objects.filter(business=sec.id).count()
    ## 技术保障部
    it = Business.objects.get(name='技术保障部')
    it_count = Asset.objects.filter(business=it.id).count()
    ## 无线技术部
    wx = Business.objects.get(name='无线技术部')
    wx_count = Asset.objects.filter(business=wx.id).count()
    ## 云平台
    med = Business.objects.get(name='云平台')
    med_count = Asset.objects.filter(business=med.id).count()

    return render(request, 'index.html', locals())

@login_required
def AssetList(request):
    assets = Asset.objects.all()
    return render(request, '../templates/assetlist.html', locals())

@login_required
@permission_required('bumblebee.change_asset', login_url='/asset/assetslist/')
def AssetEdit(request, asset_id):
    asset_types = Asset.HOST_TYPE_CHOICES
    envs = Asset.ENV_CHOICES
    status = Asset.STATUS_CHOICES
    platforms = Asset.PLATFORM_CHOICES
    asset_ret = Asset.objects.filter(id=asset_id)
    idcs = IDC.objects.all()
    purposes = Purpose.objects.all()
    nics = Nic.objects.all()
    raidcards = RaidCard.objects.all()
    raidtypes = RaidType.objects.all()
    businesses = Business.objects.all()
    subbusinesses = SubBusiness.objects.all()
    if request.method == 'POST':
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        cip = request.POST.get('cip', '')
        vip = request.POST.get('vip', '')
        disk = request.POST.get('disk', None)
        sn = request.POST.get('sn', 'N')
        mem = request.POST.get('mem', 'N')
        cpu = request.POST.get('cpu', 'N')
        os = request.POST.get('os', None)
        hosttype = request.POST.get('hosttype', None)
        env = request.POST.get('env', None)
        statu = request.POST.get('statu', None)
        exist = request.POST.get('exist', None)
        platform = request.POST.get('platform', None)
        idc = request.POST.get('idc', None)
        cabinet_no = request.POST.get('cabinet_no', None)
        cabinet_pos = request.POST.get('cabinet_pos', None)
        purpose = request.POST.get('purpose', '')
        nic = request.POST.get('nic', None)
        raidcard = request.POST.get('raidcard', None)
        raidtype = request.POST.get('raidtype', None)
        business = request.POST.get('business', '')
        subbusiness = request.POST.get('subbusiness', '')
        if business == '' and subbusiness == '' and purpose == '' and nic == '' and raidcard == '' and raidtype == '' and idc == '':
            asset_ret.update(hostname=hostname, ip=ip, cip=cip, vip=vip,
                             disk=disk, sn=sn, mem=mem, cpu=cpu,
                             os=os, hosttype=hosttype, env=env,
                             statu=statu, exist=exist, platform=platform,
                             cabinet_no=cabinet_no, cabinet_pos=cabinet_pos)
        else:
            asset_ret.update(hostname=hostname,ip=ip,cip=cip,vip=vip,disk=disk,os=os,hosttype=hosttype,env=env,statu=statu,exist=exist, platform=platform, idc=idc, cabinet_no=cabinet_no, cabinet_pos=cabinet_pos, nic=nic, raidcard=raidcard, raidtype=raidtype,
                         purpose=purpose, business=business,sub_business=subbusiness,sn=sn)
        return redirect(reverse('bumblebee:assetlist'))

    return render(request, '../templates/assetedit.html', locals())

@login_required
def AssetDatail(request, asset_id):
    asset_ret = Asset.objects.filter(id=asset_id)
    return render(request, '../templates/assetdatail.html', locals())

@login_required
@permission_required('bumblebee.add_asset', login_url='/asset/assetslist/')
def AssetAdd(request):
    if request.method == 'POST':
        res = {'code': 0}
        form = AssetForm(request.POST)
        if form.is_valid():
            hostname = form.cleaned_data['hostname'].strip()
            ip = form.cleaned_data['ip'].strip()
            cip = form.cleaned_data['cip'].strip()
            vip = form.cleaned_data['vip'].strip()
            disk = form.cleaned_data['disk'].strip()
            mac = form.cleaned_data['mac'].strip()
            hosttype = form.cleaned_data['hosttype']
            env = form.cleaned_data['env']
            statu = form.cleaned_data['statu']
            platform = form.cleaned_data['platform']
            exist = form.cleaned_data['exist']
            manufacture = form.cleaned_data['manufacture']
            server_model = form.cleaned_data['server_model']
            sn = form.cleaned_data['sn'].strip()
            out_use = form.cleaned_data['out_use']
            idc = form.cleaned_data['idc']
            cabinet_no = form.cleaned_data['cabinet_no'].strip()
            cabinet_pos = form.cleaned_data['cabinet_pos']
            business = form.cleaned_data['business']
            subbusiness = form.cleaned_data['subbusiness']
            nic = form.cleaned_data['nic']
            purpose = form.cleaned_data['purpose']
            raidcard = form.cleaned_data['raidcard']
            raidtype = form.cleaned_data['raidtype']
            check_host = Asset.objects.filter(hostname=hostname).first()
            check_ip = Asset.objects.filter(ip=ip).first()

            if check_host != None:
                res['code'] = 1
                res['errmsg'] = "资产 {} 已存在".format(hostname)
                res = json.dumps(res)
                return render(request, 'assetadd.html', locals())
            elif check_ip != None:
                res['code'] = 1
                res['errmsg'] = "IP {} 已被 {} 使用".format(ip, check_ip.hostname)
                res = json.dumps(res)
                return render(request, 'assetadd.html', locals())
            elif platform == 'CentOS' or platform == 'Ubuntu' or platform == 'Redhat':
                mem = GetMem(ip)
                cpu = GetCpu(ip)
                os = GetOS(ip)
                if hosttype == 'PM':
                    if cip == '':
                        res['code'] = 1
                        res['errmsg'] = "当资产类型为物理机器，远程管理卡IP 不能为空"
                        res = json.dumps(res)
                        return render(request, 'assetadd.html', locals())
                    elif mac == '':
                        res['code'] = 1
                        res['errmsg'] = "当资产类型为物理机器，mac 不能为空"
                        res = json.dumps(res)
                    elif manufacture == '':
                        res['code'] = 1
                        res['errmsg'] = "当资产类型为物理机器，服务器厂商 不能为空"
                        res = json.dumps(res)
                    elif server_model == '':
                        res['code'] = 1
                        res[
                            'errmsg'] = "当资产类型为物理机器，服务器型号 不能为空"
                        res = json.dumps(res)
                    elif sn == '':
                        res['code'] = 1
                        res[
                            'errmsg'] = "当资产类型为物理机器，序列号 不能为空"
                        res = json.dumps(res)
                    elif out_use == '':
                        res['code'] = 1
                        res[
                            'errmsg'] = "当资产类型为物理机器，过保时间 不能为空"
                        res = json.dumps(res)
                    elif cabinet_no == None:
                        res['code'] = 1
                        res['errmsg'] = "当资产类型为物理机器, 所在机柜 不能为空"
                        res = json.dumps(res)
                    elif cabinet_pos == None:
                        res['code'] = 1
                        res['errmsg'] = "当资产类型为物理机器，托盘位置 不能为空"
                        res = json.dumps(res)
                    elif nic == None:
                        res['code'] = 1
                        res['errmsg'] = "当资产类型为物理机器，网卡 不能为空"
                        res = json.dumps(res)
                    else:
                        Asset.objects.create(hostname=hostname,ip=ip,cip=cip,vip=vip,mem=mem, cpu=cpu, os=os, disk=disk,mac=mac,hosttype=hosttype,env=env,statu=statu,platform=platform,exist=exist,manufacture=manufacture,server_model=server_model,sn=sn,out_use=out_use,idc=idc,cabinet_no=cabinet_no,cabinet_pos=cabinet_pos,business=business,sub_business=subbusiness,nic=nic,purpose=purpose,raidcard=raidcard,raidtype=raidtype)
                        res['code'] = 0
                        res['errmsg'] = "添加资产 {} 成功".format(hostname)
                        res = json.dumps(res)
                        LogInfo("{} {} 添加资产: {} ".format(request.user.username, request.user.last_name, hostname))
                        return redirect(reverse('bumblebee:assetlist'), locals())
                if hosttype == 'VM':
                    if exist == '':
                        res['code'] = 1
                        res['errmsg'] = "当资产类型为虚拟机时，宿主机不能为空"
                        res = json.dumps(res)
                        return render(request, 'assetadd.html', locals())
                    else:
                        Asset.objects.create(hostname=hostname, ip=ip, cip=cip, vip=vip, mem=mem, cpu=cpu, os=os, disk=disk, mac=mac, hosttype=hosttype, env=env, statu=statu, platform=platform, exist=exist, idc=idc, business=business, sub_business=subbusiness, nic=nic, purpose=purpose, raidcard=raidcard, raidtype=raidtype)
                        res['code'] = 0
                        res['errmsg'] = "添加资产 {} 成功".format(hostname)
                        res = json.dumps(res)
                        LogInfo("{} {} 添加资产: {} ".format(request.user.username, request.user.last_name, hostname))
                        return redirect(reverse('bumblebee:assetlist'), locals())
            else:
                Asset.objects.create(hostname=hostname, ip=ip, cip=cip,
                                     vip=vip,
                                     disk=disk, mac=mac,
                                     hosttype=hosttype, env=env,
                                     statu=statu, platform=platform,
                                     exist=exist,
                                     manufacture=manufacture,
                                     server_model=server_model, sn=sn,
                                     out_use=out_use, idc=idc,
                                     cabinet_no=cabinet_no,
                                     cabinet_pos=cabinet_pos,
                                     business=business,
                                     sub_business=subbusiness, nic=nic,
                                     purpose=purpose, raidcard=raidcard,
                                     raidtype=raidtype)
                LogInfo("{} {} 添加资产: {} ".format(request.user.username,request.user.last_name,hostname))
                res['code'] = 0
                res['errmsg'] = "添加资产 {} 成功".format(hostname)
                res = json.dumps(res)
                return redirect(reverse('bumblebee:assetlist'), locals())
    else:
        form = AssetForm
    return render(request, 'assetadd.html', locals())

@login_required
@permission_required('bumblebee.delete_asset')
def AssetsDelete(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    LogInfo("{} {} 删除资产: {} ".format(request.user.username, request.user.last_name,asset))
    asset.delete()
    return HttpResponseRedirect(reverse('bumblebee:assetlist'))

@login_required
def DomainList(request):
    domains = Domain.objects.all()
    return render(request, '../templates/domainlist.html', {'domains': domains})

@login_required
@permission_required('bumblebee.add_domain', login_url='/asset/domainlist/')
def DomainAdd(request):
    if request.method == 'POST':
        res = {'code': 0}
        form = DomainForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'].strip()
            ip = form.cleaned_data['ip']
            oip = form.cleaned_data['oip']
            inner_outner = form.cleaned_data['inner_outner']
            use_for = form.cleaned_data['use_for']
            person_duty = form.cleaned_data['person_duty']
            project = form.cleaned_data['project']
            env = form.cleaned_data['env']
            business = form.cleaned_data['business']
            subbusiness = form.cleaned_data['subbusiness']
            check_domain = Domain.objects.filter(name=name).first()
            if check_domain != None:
                print(check_domain)
                res['code'] = 1
                res['errmsg'] = '域名 {} 已存在'.format(name)
                res = json.dumps(res)
                return render(request, 'domainadd.html', locals())
            else:
                print(name,ip,oip,inner_outner,use_for,person_duty,project,env,business,subbusiness)
                Domain.objects.create(name=name, ip=ip, oip=oip, inner_outner=inner_outner,use_for=use_for,person_duty=person_duty,project=project,env=env,business=business,subbusiness=subbusiness)
                res['errmsg'] = '添加域名 {} 成功'.format(name)
                res = json.dumps(res)
                return redirect(reverse('bumblebee:domainlist'), locals())
    else:
        form = DomainForm
    return render(request, 'domainadd.html', locals())

@login_required
@permission_required('bumblebee.delete_domain', login_url='/asset/domainlist/')
def DomainDelete(request, domain_id):
    domain = get_object_or_404(Domain, id=domain_id)
    domain.delete()
    return HttpResponseRedirect(reverse('bumblebee:domainlist'))

@login_required
@permission_required('bumblebee.change_domain', login_url='/asset/domainlist/')
def DomainEdit(request, domain_id):
    envs = Domain.ENV_CHOICES
    subbusinesses = SubBusiness.objects.all()
    domain_ret = Domain.objects.filter(id=domain_id)
    if request.method == 'POST':
        domain = request.POST.get('domain', 'N')
        ip = request.POST.get('ip', 'N')
        oip = request.POST.get('oip', 'N')
        inner_outner = request.POST.get('inner_outer', 'N')
        use_for = request.POST.get('used_for', 'N')
        person = request.POST.get('person', 'N')
        env = request.POST.get('env', 'N')
        subbusiness = request.POST.get('subbusiness', 'N')
        domain_ret.update(name=domain, ip=ip, oip=oip, inner_outner=inner_outner, person_duty=person, use_for=use_for, env=env, subbusiness=subbusiness)
        return redirect(reverse('bumblebee:domainlist'))
    return render(request, 'domainedit.html', locals())

@login_required
def IdcList(request):
    idcs = IDC.objects.all()
    print(idcs)
    return render(request, '../templates/idclist.html', {'idcs': idcs})

@login_required
def IdcDatail(request, idc_id):
    idc_ret = IDC.objects.filter(id=idc_id)
    return render(request, '../templates/idcdatail.html', locals())

@login_required
@permission_required('bumblebee.change_idc', login_url='/asset/idclist/')
def IdcEdit(request, idc_id):
    idc_ret = IDC.objects.filter(id=idc_id)
    if request.method == 'POST':
        idc_name = request.POST.get('name', '')
        idc_bandwidth = request.POST.get('bandwidth', '')
        idc_contactor = request.POST.get('contactor', '')
        idc_phone = request.POST.get('phone', '')
        idc_address = request.POST.get('address', '')
        idc_ret.update(name=idc_name, bandwidth=idc_bandwidth, contactor=idc_contactor, phone=idc_phone, addres=idc_address)
        return redirect(reverse('bumblebee:idclist'))
    return render(request, '../templates/idcedit.html', locals())

@login_required
@permission_required('bumblebee.add_idc', login_url='/asset/idclist/')
def IdcAdd(request):
    if request.method == 'POST':
        idcname = request.POST['idcname']
        bandwidth = request.POST['bandwidth']
        contactor = request.POST['contactor']
        phone = request.POST['phone']
        address = request.POST['address']

        name_find = IDC.objects.filter(name=idcname).first()
        if name_find == None:
            idc = IDC(name=idcname, contactor=contactor, phone=phone, address=address)
            idc.save()
            return redirect(reverse('bumblebee:idclist'))
        else:
            print("{}机房已存在".format(idcname))
            return redirect(reverse('bumblebee:idclist'))
    return  render(request, '../templates/idcadd.html')

@login_required
@permission_required('bumblebee.delete_idc')
def IdcDelete(request, idc_id):
    idc = get_object_or_404(Asset, id=idc_id)
    idc.delete()
    return HttpResponseRedirect(reverse('bumblebee:idclist'))

@login_required
def BusinessDatail(request):
    businesses = Business.objects.all()
    idcs = IDC.objects.all()
    return render(request, '../templates/businessdatail.html', {'businesses':businesses})

@login_required
@permission_required('bumblebee.add_business', login_url='/asset/businessdatail/')
def BusinessAdd(request):
    if request.method == 'POST':
        businessname = request.POST['businessname']
        person = request.POST['person_duty']
        businessname_find = IDC.objects.filter(name=businessname).first()
        if businessname_find == None:
            business = Business(name=businessname, person_duty=person)
            business.save()
        return redirect(reverse('bumblebee:businessdatail'))
    return render(request,'../templates/businessadd.html')

@login_required
@permission_required('bumblebee.change_business', login_url='/asset/businessdatail/')
def BusinessEdit(request, business_id):
    business_ret = Business.objects.filter(id=business_id)
    allsre = User.objects.filter(group=83)
    if request.method == 'POST':
        name = request.POST.get('businessname', 'N')
        name_english = request.POST.get('name_english', 'N')
        person_duty = request.POST.get('person_duty', 'N')
        sre = request.POST.getlist("sre", "None")
        endsre = ','.join(sre)
        business_ret.update(name=name, name_english=name_english, person_duty=person_duty, sre=endsre)
        return redirect(reverse('bumblebee:businessdatail'))
    return render(request, 'businesedit.html', locals())

@login_required
def SubBiseDatail(request):
    sub_busis = SubBusiness.objects.all()
    return render(request, '../templates/sub_busi_datail.html', {'sub_busis':sub_busis})

@login_required
@permission_required('bumblebee.add_subbusiness', login_url='/asset/subbisedatail/')
def SubBiseAdd(request):
    business = Business.objects.all()
    if request.method == 'POST':
        sub_name = request.POST['subname']
        business = Business.objects.get(name=request.POST['business'])
        person_duty = request.POST['person_duty']
        sub_find = SubBusiness.objects.filter(name=sub_name).first()
        if sub_find == None:
            sub = SubBusiness(name=sub_name, business=business, person=person_duty)
            sub.save()
            Config.fort_data["name"] = business
            FD = requests.post("{}{}".format(Config.FortBASE_URL,Config.FortDepartQuery), data=Config.fort_data)
            ParentID = json.loads(str(FD.content,  'utf-8'))['data'][0]['id']
            Config.fort_data["name"] = sub_name
            Config.fort_data["parent"] = ParentID
            FDADD = requests.post("{}{}".format(Config.FortBASE_URL, Config.FortDepartAdd), data=Config.fort_data)
            logger.info(json.loads(str(FDADD.content, 'utf-8')))
            return redirect(reverse('bumblebee:subbisedatail'))
        else:
            print("{}已存在".format(sub_name))
            return render(request, '../templates/sub_busi_datail.html')
    return render(request, '../templates/sub_busi_add.html', {'business':business})

@login_required
@permission_required('bumblebee.change_subbusiness', login_url='/asset/subbisedatail/')
def SubBusibessEdit(request,subbusiness_id):
    subbusiness_ret = SubBusiness.objects.filter(id=subbusiness_id)
    allbusiness = Business.objects.all()
    allsre = User.objects.filter(group=83)
    if request.method == "POST":
        subbusibess = request.POST.get("subbusinessname")
        ename = request.POST.get("ename")
        business = request.POST.get("business")
        person = request.POST.get("person")
        sre = request.POST.getlist("sre", "None")
        endsre = ','.join(sre)
        subbusiness_ret.update(name=subbusibess, name_english=ename,business=business,person=person, sre=endsre)
        return redirect(reverse('bumblebee:subbisedatail'))
    return render(request,'../templates/subbusinessedit.html', locals())

@login_required
@permission_required('bumblebee.delete_asset')
def SubBusibessDelete(request, subbusiness_id):
    subbusiness = get_object_or_404(SubBusiness, id=subbusiness_id)
    subbusiness.delete()
    return HttpResponseRedirect(reverse('bumblebee:subbisedatail'))

"""
Get Business and SubBusiness
"""
@login_required
def BusiInfo(request):
    busi = Business.objects.all()
    subbusi = SubBusiness.objects.all()
    qs1 = SubBusiness.objects.values('business').annotate(count=Count('business')).order_by()
    qs2 = SubBusiness.objects.values('business','name','id','person', 'sre')
    return render(request, '../templates/business_subbusiness.html', locals())

@login_required
def NicList(request):
    nics = Nic.objects.all()
    return render(request,'../templates/niclist.html',{'nics':nics})

@login_required
def NicAdd(request):
    if request.method == 'POST':
        nicname = request.POST['nicname']
        nic_find = Nic.objects.filter(name=nicname).first()
        if nic_find == None:
            nic = Nic(name=nicname)
            nic.save()
            return redirect(reverse('bumblebee:niclist'))
        else:
            print("{}已存在".format(nicname))
    return  render(request, '../templates/nicadd.html')

@login_required
def PurposeList(request):
    purposes = Purpose.objects.all()
    return render(request, '../templates/purposelist.html',{'purposes':purposes})

@login_required
def PurposeAdd(request):
    if request.method == 'POST':
        purpose_name = request.POST['purposename']
        pur_find = Purpose.objects.filter(name=purpose_name).first()
        if pur_find == None:
            purpose = Purpose(name=purpose_name)
            purpose.save()
            return redirect(reverse('bumblebee:purposelist'))
        else:
            print("{}已存在".format(purpose_name))
    return render(request, '../templates/purposeadd.html')

@login_required
def ProjectList(request):
    projects = Project.objects.all()
    return render(request, '../templates/projectlist.html', locals())

@login_required
@permission_required('bumblebee.add_project', login_url='/asset/projectlist/')
def ProjectAdd(request):
    return render(request, '../templates/projectadd.html')

@login_required
def ProjectDatail(request, project_id):
    project_ret = Project.objects.filter(id=project_id)
    return render(request, '../templates/projectdatail.html', locals())

@login_required
@permission_required('bumblebee.change_project', login_url='/asset/projectlist/')
def ProjectEdit(request, project_id):
    project_ret = Project.objects.filter(id=project_id)
    monitor_choices = Project.MONITOR_CHOICES
    monitor_envs = Project.MONITOR_STATUS
    res = {'code': 0}
    if request.method == "POST":
        choice = request.POST.get("choice", 'N')
        env = request.POST.get("env", 'N')
        uri = request.POST.get("uri", 'N')

        if choice == 'Yes':
            if env == 'Null':
                res['code'] = 1
                res['errmsg'] = '当需要监控时，环境不能为空'
                res = json.dumps(res)
            elif uri == '':
                res['code'] = 1
                res['errmsg'] = '当需要监控时，uri不能为空'
                res = json.dumps(res)
            else:
                project_ret.update(monitorchoice=choice, monitorenv=env, monitor_url=uri)
                return redirect(reverse('bumblebee:projectlist'))
        else:
            if env != 'Null':
                res['code'] = 1
                res['errmsg'] = '当环境不为空时，必须为监控状态'
                res = json.dumps(res)
            elif uri != '':
                res['code'] = 1
                res['errmsg'] = 'uri不能为空时，必须为监控状态'
                res = json.dumps(res)
            else:
                res['code'] = 0
                res['errmsg'] = '修改成功'
                res = json.dumps(res)
                project_ret.update(monitorchoice=choice, monitorenv=env, monitor_url=uri)
                return redirect(reverse('bumblebee:projectlist'), locals())
    return render(request, '../templates/projectedit.html', locals())

@login_required
def RaidCardList(request):
    RaidCardRet = RaidCard.objects.all()
    return render(request, 'raidcardlist.html', locals())

@login_required
@permission_required('bumblebee.add_raidcard', login_url='/asset/raidcardlist/')
def RaidCardAdd(request):
    if request.method == 'POST':
        raidcard_name = request.POST.get('raidcardname', 'N')
        raidcard_cache = request.POST.get('cache', 'N')
        raidcard_check = RaidCard.objects.filter(name=raidcard_name).first()
        creat_user = request.user.name
        if raidcard_check is None:
            NewRaidCard = RaidCard.objects.create(name=raidcard_name, cache=raidcard_cache, created_by=creat_user)
            NewRaidCard.save()
            return HttpResponseRedirect(reverse('bumblebee:raidcardlist'))
        else:
            print('已存在')
            return HttpResponseRedirect(reverse('bumblebee:raidcardlist'))
    return render(request, 'raidcardadd.html')

@login_required
@permission_required('bumblebee.delete_raidcard', login_url='/asset/raidcardlist/')
def RaidCardDelete(request, raidcard_id):
    raidcard = get_object_or_404(RaidCard, id=raidcard_id)
    raidcard.delete()
    return HttpResponseRedirect(reverse('bumblebee:raidcardlist'))

@login_required
@permission_required('bumblebee.change_raidcard', login_url='/asset/raidcardlist/')
def RaidCardEdit(request, raidcard_id):
    raidcard_ret = RaidCard.objects.filter(id=raidcard_id)
    if request.method == 'POST':
        raidcard_name = request.POST.get('raidcardname', 'N')
        raidcard_cache = request.POST.get('cache', 'N')
        change_user = request.user.name
        raidcard_ret.update(name=raidcard_name,cache=raidcard_cache, last_oper=change_user)
        return HttpResponseRedirect(reverse('bumblebee:raidcardlist'))
    return render(request, 'raidcardedit.html', locals())

@login_required
def RaidTypeList(request):
    RaidTypeRet = RaidType.objects.all()
    return render(request, 'raidtypelist.html', locals())

@login_required
@permission_required('bumblebee.add_raidtype', login_url='/asset/raidtypelist/')
def RaidTypeAdd(request):
    if request.method == 'POST':
        raidtype = request.POST.get('raidtypename', 'N')
        raidtype_check = RaidType.objects.filter(name=raidtype).first()
        if raidtype_check is None:
            NewRaidType = RaidType.objects.create(name=raidtype)
            NewRaidType.save()
            return HttpResponseRedirect(reverse('bumblebee:raidtypelist'))
        else:
            print('已存在')
            return HttpResponseRedirect(reverse('bumblebee:raidtypeadd'))
    return render(request, 'raidtypeadd.html')

@login_required
@permission_required('bumblebee.delete_raidtype', login_url='/asset/raidtypelist/')
def RaidTypeDelete(request, raidtype_id):
    raidtype = get_object_or_404(RaidType, id=raidtype_id)
    raidtype.delete()
    return HttpResponseRedirect(reverse('bumblebee:raidtypelist'))

"""
database function views
"""
@login_required
def DBList(request):
    dbs = DBA.objects.all()
    return render(request, '../templates/dblist.html', locals())

@login_required
@permission_required('bumblebee.add_dba', login_url='/asset/dbalist/')
def DBAdd(request):
    if request.method == 'POST':
        res = {'code': 0}
        form = DBAForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            instance = form.cleaned_data['instance']
            db_name = form.cleaned_data['instance']
            db_type = form.cleaned_data['db_type']
            db_port = form.cleaned_data['db_port']
            db_statu = form.cleaned_data['db_statu']
            business = form.cleaned_data['business']
            subbusiness = form.cleaned_data['subbusiness']
            check_name = DBA.objects.filter(name=name).first()

            if check_name != None:
                if db_type == check_name.db_type:
                    res['code'] = 1
                    res['errmsg'] = '数据库类型为 {} 的集群 {} 已存在'.format(db_type, name)
                    res = json.dumps(res)
                    return render(request, 'dbaadd.html', locals())
            else:
                dbid = DBA.objects.all().count() + 1
                dba = DBA.objects.create(dbid=dbid,name=name,instance=instance,db_name=db_name, db_type=db_type,db_statu=db_statu,db_port=db_port, business=business,subbusiness=subbusiness)
                res['errmsg'] = '添加数据库类型为{}的集群{}成功'.format(db_port, name)
                res = json.dumps(res)
                return redirect(reverse('bumblebee:dblist'), locals())
    else:
        form = DBAForm
    return render(request, 'dbaadd.html', locals())

class AppsList(ListView):
    model = Apps

class AppsAdd(View):
    form_class = AppAddForm
    template_name = 'apps_add.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        res = {'code': 0}
        appadd_form = self.form_class(request.POST)
        if appadd_form.is_valid():
            host = request.POST.get('host', None).strip()
            port = request.POST.get('port', None).strip()
            uri = request.POST.get('uri', 'metrics')
            check_host = Apps.objects.filter(host=host,port=port).first()

            if host is not None and port is not None and uri == 'metrics':
                HostLen = len(host.split('-') or host.split(','))
                if check_host != None:
                    res['code'] = 1
                    res['errmsg'] = "主机{} 端口{} 监控已存在".format(host, port)
                    res = json.dumps(res)
                    return render(request, 'apps_add.html', locals())
                if HostLen == 4:
                    appadd_form.save()
                    return HttpResponseRedirect(reverse('bumblebee:appslist'))
                else:
                    res['code'] = 1
                    res['errmsg'] = "请在主机选项不要填写多个主机"
                    res = json.dumps(res)
        else:
            res['code'] = 1
            res['errmsg'] = "主机、监控端口、监控uri不能为空"
            res = json.dumps(res)
        return render(request, 'apps_add.html', locals())

@login_required
@permission_required('bumblebee.delete_apps')
def AppsDelete(request, app_id):
    app = get_object_or_404(Apps, id=app_id)
    app.delete()
    return HttpResponseRedirect(reverse('bumblebee:appslist'))

@login_required
def Fort(request):
    return render(request, 'fort.html')

@login_required
def ActiveFort(request):
    res = {'code': 0}
    user = "{}@xxx.com".format(request.user.name)
    Ret = ActiveUser(user)
    if Ret['code'] != 0:
        res['code'] = 1
        res['errmsg'] = Ret['message']
        ret = json.dumps(res)

    else:
        res['errmsg'] = Ret['message']
        ret = json.dumps(res)
    return render(request, 'fort.html', locals())

from lib.orgphone import getphone
from lib.sms import sendmsm, getphonecode
@login_required
def GetCheckNum(request):
    res = {'code': 0}
    if request.method == 'POST':
        user = request.user.name
        phone = getphone(user)
        checknum = request.POST.get("checknum", None)
        checkcode = getphonecode(phone)
        if checknum is not None:
            if checknum == checkcode:
                Ret = UpdateFortUser(user)
                if Ret['code'] != 2000:
                    res['code'] = 1
                    res['errmsg'] = Ret['msg']
                    ret = json.dumps(res)
                    LogInfo("{} {} 重新绑定手机失败 {}".format(request.user.username, request.user.last_name, Ret['msg']))
                else:
                    res['code'] = 0
                    res['errmsg'] = "重新绑定手机成功"
                    ret = json.dumps(res)
                    LogInfo("{} {}重新绑定手机成功".format(request.user.username, request.user.last_name))
                    return render(request, 'fort.html', locals())
            else:
                res['code'] = 1
                res['errmsg'] = "手机验证码不正确"
                ret = json.dumps(res)
                LogInfo("{} {}重新绑定手机失败 手机验证码不正确".format(request.user.username, request.user.last_name))
                return render(request, 'update_fort.html', locals())
        else:
            res['code'] = 1
            res['errmsg'] = "手机验证码不能为空"
    return render(request, 'update_fort.html', locals())

@login_required
def UpFortUser(request):
    res = {'code': 0}
    user = request.user.name
    phone = getphone(user)
    ret = sendmsm(phone)
    if ret['code'] != 0:
        res['code'] = 1
        res['errmsg'] = ret['message']
        return render(request, 'fort.html', locals())
    else:
        res['code'] = 0
        res['errmsg'] = "验证码已发送至手机"
        return HttpResponseRedirect(reverse('bumblebee:changephone'))

class OutIPList(ListView):
    model = OutIPS

@login_required
@permission_required('bumblebee.add_outip', login_url='/asset/outiplist/')
def OutIPAdd(request):
    if request.method == 'POST':
        res = {'code': 0}
        form = OutIPForm(request.POST)
        if form.is_valid():
            ipaddress = form.cleaned_data['ipaddress']
            innerip = form.cleaned_data['innerip']
            business = form.cleaned_data['business']
            subbusiness = form.cleaned_data['subbusiness']
            domain = form.cleaned_data['domain']
            check_ipaddress = OutIPS.objects.filter(ipaddress=ipaddress).first()
            if check_ipaddress != None:
                res['code'] = 1
                res['errmsg'] = '外网IP {} 已存在'.format(ipaddress)
                res = json.dumps(res)
                print(res)
                return render(request, 'outipadd.html', locals())
            else:
                OutIPS.objects.create(ipaddress=ipaddress, innerip=innerip, business=business, subbusiness=subbusiness, domain=domain)
                res['errmsg'] = '添加外网IP {} 成功'.format(ipaddress)
                res = json.dumps(res)
                return redirect(reverse('bumblebee:outiplist'), locals())
    else:
        form = OutIPForm
    return render(request, 'outipadd.html', locals())