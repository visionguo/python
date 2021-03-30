#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2021/03/22
# Brief:
#    index
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import sys
from flask import jsonify, Flask, app, request, render_template, redirect, url_for, session, abort, jsonify, make_response, send_from_directory, make_response, jsonify, Response, flash
from gen_case_id import gen_case_id
from mysql import query_db, modify_db
from form import EditForm
import time
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
from models.sso import Sso
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from models.models import user_id_exists
from models.models import User, NocImprovement, NocAffected, NocNoc, NocPriority, NocReasons
from models.models import db
from models.identity import get_user_role
from models.identity import login_required, is_admin
from models.config import config
from models.identity import login_required, is_admin, get_user_role, insert_es
from noclist import finish_rate
import json

app = Flask(__name__)
app.config.from_object(config['base'])
app.secret_key = ''
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['TEMPLATES_AUTO_RELOAD'] = True

def object_as_dict(obj):
    """
    对象转字典
    """
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

@app.route('/')
    """
    登录
    """
def login():
    user_info = Sso.user_info_by_token()
    if Sso.valid_user_info(user_info):
        """
        通过sso鉴权该用户是否合法
        """
        user_id = user_info.get("user_id")
        user = user_info.get("fullname")
        email = user_info.get("email")
        name = email[:-10]
        role_id = 1
        current_user = User(user_id=user_id, name=name, email=email, role_id=role_id)
        session["user_id"] = user_id
        session["username"] = user
        session["role"] = get_user_role()

        if not user_id_exists(user_id):
            """
            通过userid判断用户是否存在
            """
            try:
                db.session.add(current_user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()

        return redirect(url_for('noclist'))
    return redirect(app.config['SSO_URL'] + app.config.get('LOGIN_RETURN_URL') + app.config.get('NOC_URL'))

@app.route("/logout/")
@login_required
def logout():
    """
    用户退出
    """
    logout_token_status = Sso.logout_token()
    if not logout_token_status:
        return
    session.pop("username", None)
    session.pop("role", None)
    return redirect(app.config['SSO_URL'] + app.config.get('LOGOUT_RETURN_URL') + app.config.get('NOC_URL'))

@app.route("/user/", methods=["GET", "POST"])
@login_required
@is_admin
def user():
    username = request.values.get("username")
    role_id = request.values.get("role_id")
    user_id = request.values.get("user_id")

    if username is not None:
        search_user = db.session.query(User).filter_by(name=username).first()
        if search_user is None:
            flash('Not Found!', 'info')
        else:
            data = {
                "name": search_user.name,
                "email": search_user.email,
                "user_id": search_user.user_id,
                "role_id": search_user.role.id,
                "role_name": search_user.role.name
            }
            db.session.close()
            return render_template('nocusers-list.html', **data)

    if request.method == 'POST' and user_id is not None:
        user = db.session.query(User).filter_by(user_id=user_id).first()
        user.role_id = int(role_id)
        db.session.add(user)
        db.session.commit()

    user = db.session.query(User).filter_by(user_id=session.get("user_id")).first()
    if user is not None:
        data = {
            "name": user.name,
            "email": user.email,
            "user_id": user.user_id,
            "role_id": user.role.id,
            "role_name": user.role.name
        }
        db.session.close()
    return render_template('nocusers-list.html', **data)

@app.route('/addnocid', methods=('GET', 'POST'))
@login_required
@is_admin
def addnocid():
    """
    增加nocid
    """
    if request.method == 'POST':
        postData = request.form
        t = request.form.getlist('imp_data')[0]
        dict_data = dict(map(lambda s: s.split('='), t.split('&')))
        add_dict = {'serial_number': dict_data["nocid"],'title': dict_data["noctitle"]}
        add_info = NocNoc(**add_dict)
        try:
            db.session.add(add_info)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            raise
        finally:
            db.session.close()

        d = {'res': 'success','nocid': dict_data["nocid"] }
    return jsonify(d)

@app.route('/Declare.html', methods=('GET', 'POST'))
@login_required
@is_admin
def pages():
    """
    page页
    """
        path = request.path
        forms = request.args.get('declare_form')
        print(forms)
        case_id = gen_case_id()
        print(case_id)
        if forms == '2':
            print(r)
        return render_template('Declare.html', **locals())

@app.route('/noclist.html')
@login_required
def noclist():
    """
    noc列表
    """
    path = request.path
    searchstr = request.args.get('search')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page',10))
    if searchstr is not None:
        noc_xxx = NocNoc.query.filter(or_(NocNoc.serial_number.like('%'+searchstr+'%'), NocNoc.title.like('%'+searchstr+'%'), NocNoc.priority_id.like('%'+searchstr+'%'),NocNoc.responsible_team.like('%'+searchstr+'%'),NocPriority.name.like('%'+searchstr+'%'),NocAffected.affected_team.like('%'+searchstr+'%') )).join(  NocPriority, NocNoc.priority_id==NocPriority.id).join(  NocAffected, NocNoc.id==NocAffected.nid).order_by(NocNoc.id.desc()).paginate(page, per_page, error_out=False)
        posts = noc_xxx.items
    else:
        noc_xxx = NocNoc.query.order_by(NocNoc.id.desc()).paginate(page, per_page, error_out=False)
        posts = noc_xxx.items

    finish_rate_list={}
    for i in posts:
        finish_rate_list[i.serial_number]=finish_rate(i.serial_number)
    return render_template('noclist.html', **locals())

@app.route('/inseartes')
def inseartes():
    """
    写入es
    """
    case_id = request.args.get('sn')
    noc_json = {
            "@timestamp": "2018-11-17T10:18:00.305430",
            "start_time": "2018-11-17T23:08:00.305430",
            "found_time": "2018-11-17T23:21:00.305430",
            "fixed_time": "2018-11-17T23:38:00.305430",
            "noc_time": "2018-11-17T23:26:00.305430",
            "interval_discover": 13,
            "interval_report": 5,
            "interval_recover": 17,
            "topic": "hive metastore 连接数被打爆，导致presto bi集群查询超时",
            "case_level": 2,
            "accident_source": [
                "大数据"
            ],
            "accident_reason": [
                "线上机器管理不善"
            ],
            "affected": [
                "xinche交易"
            ],
            "noc_url": "http://wiki.xxx.com"
    }
    try:
        noc_info = db.session.query(NocNoc).filter(NocNoc.serial_number == case_id ).first()
        affected_info = db.session.query(NocAffected).filter(NocAffected.nid == noc_info.id).all()
        imp_info = db.session.query(NocImprovement).filter(NocImprovement.nid == noc_info.id).all()
    except Exception as e:
        db.session.rollback()
        print(e)
        raise
    finally:
        db.session.close()

    if noc_info.found_time:
        """
        noc信息查询时间
        """
        try:
            noc_json["found_time"] = datetime.strftime(noc_info.found_time, "%Y-%m-%dT%H:%M:%S")
        except:
            noc_json["found_time"] = noc_info.found_time

    if noc_info.start_time:
        """
        开始时间
        """
        try:
            noc_json["start_time"] = datetime.strftime(noc_info.start_time, "%Y-%m-%dT%H:%M:%S")
            noc_json["@timestamp"] = noc_json["start_time"]
        except:
            noc_json["start_time"] = noc_info.start_time

    if noc_info.fixed_time:
        """
        修复时间
        """
        try:
            noc_json["fixed_time"] = datetime.strftime(noc_info.fixed_time, "%Y-%m-%dT%H:%M:%S")    # strftime: time结构格式化为字符串
        except:
            noc_json["fixed_time"] = noc_info.fixed_time

    if noc_info.noc_time:
        """
        noc time
        """
        try:
            noc_json["noc_time"] = datetime.strftime(noc_info.noc_time, "%Y-%m-%dT%H:%M:%S")
        except:
            noc_json["noc_time"] = noc_info.noc_time
            noc_json["interval_discover"] = (noc_info.found_time - noc_info.start_time).total_seconds() / 60    # 发现间隔
            noc_json["interval_report"] = (noc_info.noc_time - noc_info.found_time).total_seconds() / 60    # 报告间隔
            noc_json["interval_recover"] = (noc_info.fixed_time - noc_info.start_time).total_seconds() / 60    # 恢复间隔
            noc_json["topic"] = noc_info.title    # noc 主题
            noc_json["case_level"] = noc_info.priority_id    # 故障级别
            noc_json["noc_url"] = "http://xxx.xxx-int.com/nocdoc.html?id=" + case_id    # noc url
            noc_json["accident_source"] = str(noc_info.responsible_dept) + "/" + str(noc_info.responsible_team)    # 事故来源
            noc_json["affected"]=[]    # 故障影响

    for i in affected_info:
        """
        故障影响信息
        """
        noc_json["affected"].append(str(i.affected_dept)+"/"+str(i.affected_team))
    insert_es("doc", "noc_new", noc_json)
    return redirect(url_for('noclist'))

@app.route('/inseartjira')
def inseartjira():
    """
    插入到jira信息
    """
    case_id = request.args.get('sn')
    url = 'http://project.xxx-int.com/rest/api/2/issue/'
    headers = { 'Content-Type': 'application/json'}
    jiradata = {
    "fields": {
        "project": {
            "key": "NOC"
        },
        "summary": "summary",
        "description": "Creating of an issue using project keys and issue type names using the REST API",
        "issuetype": {
            "id": "11101"
        },
        "customfield_12407": {
            "key": "ZNKFE"
        },
        "customfield_12835": "2018-12-03",
        "assignee": {
            "name": "rd1"
        }
    }
    }

    try:
        noc_info = db.session.query(NocNoc).filter(NocNoc.serial_number == case_id).first()
        imp_info = db.session.query(NocImprovement).filter(NocImprovement.nid == noc_info.id ).first()
    except Exception as e:
        db.session.rollback()
        print(e)
        raise
    finally:
        db.session.close()

    if imp_info.completion_time:
        """
        完成时间
        """
        try:
            jiradata["fields"]["customfield_12835"] = datetime.strftime(imp_info.completion_time, "%Y-%m-%d")
            print(jiradata["fields"]["customfield_12835"])
        except:
            jiradata["fields"]["customfield_12835"] = imp_info.completion_time
    jiradata["fields"]["summary"] = imp_info.title
    print(jiradata)

    r = requests.post(url, data= json.dumps(jiradata), headers=headers, auth=('noc1','Gnnoocc@)!('))
    print(r.text)
    return redirect(url_for('noclist'))

@app.route('/header.html')
def header():
    """
    头部界面
    """
    return render_template('header.html')

@app.route('/nocdoc.html')
def nocdoc():
    """
    noc 文档
    """
    path =  request.path
    business = requests.get("http://cmdb.xxx-int.com/api/v1/business/")
    subbusiness = requests.get("http://cmdb.xxx-int.com/api/v1/subbusiness/")
    b = business.json()
    sb = subbusiness.json()
    case_id = request.args.get('sn')
    try:
        db.session.commit()
        noc_info = db.session.query(NocNoc).filter(NocNoc.serial_number == case_id).first()
        print(noc_info.id)
        priority_info = db.session.query(NocPriority).all()
        reasons_info = db.session.query(NocReasons).filter(NocReasons.parent_id == 0).all()
        sub_reasons_info = db.session.query(NocReasons).filter(NocReasons.parent_id != 0).all()

        affected_info = db.session.query(NocAffected).filter(NocAffected.nid == noc_info.id).all()
        imp_info = db.session.query(NocImprovement).filter(NocImprovement.nid == noc_info.id).all()
    except Exception as e:
        db.session.rollback()
        print(e)
        raise
    finally:
        db.session.close()

    if noc_info.found_time:
        """
        noc报告感知时间
        """
        try:
            found_time = datetime.strftime(noc_info.found_time, "%Y-%m-%dT%H:%M:%S")
        except:
            found_time = noc_info.found_time

    if noc_info.start_time:
        """
        noc报告开始时间
        """
        try:
            start_time = datetime.strftime(noc_info.start_time, "%Y-%m-%dT%H:%M:%S")
        except:
            start_time = noc_info.start_time

    if noc_info.fixed_time:
        """
        修复时间
        """
        try:
            fixed_time = datetime.strftime(noc_info.fixed_time, "%Y-%m-%dT%H:%M:%S")
        except:
            fixed_time = noc_info.fixed_time

    if noc_info.noc_time:
        """
        noc时间
        """
        try:
            noc_time = datetime.strftime(noc_info.noc_time, "%Y-%m-%dT%H:%M:%S")
        except:
            noc_time = noc_info.noc_time
    return render_template('nocdoc.html', **locals())    # 使用 render_template 模板进行渲染

@app.route('/detail.html', methods=('GET', 'POST'))
@login_required
def edit():
    """
    编辑
    """
    path = request.path
    business = requests.get("http://cmdb.xxx-int.com/api/v1/business/")
    subbusiness = requests.get("http://cmdb.xxx-int.com/api/v1/subbusiness/")
    b = business.json()
    sb = subbusiness.json()
    affected_customer_type = {u'内部':1, u'外部':2}
    case_sn = request.args.get('sn')
    try:
        db.session.commit()
        noc_info = db.session.query(NocNoc).filter(NocNoc.serial_number == case_sn).first()
        reasons_info = db.session.query(NocReasons).filter(NocReasons.parent_id == 0).all()
        sub_reasons_info = db.session.query(NocReasons).filter(NocReasons.parent_id != 0).all()

        priority_info = db.session.query(NocPriority).all()
        affected_info = db.session.query(NocAffected).filter(NocAffected.nid == noc_info.id).all()
        imp_info = db.session.query(NocImprovement).filter(NocImprovement.nid == noc_info.id).all()
    except Exception as e:
        db.session.rollback()
        print(e)
        raise
    finally:
        db.session.close()

    if noc_info.found_time:
        try:
            found_time = datetime.strftime(noc_info.found_time, "%Y-%m-%dT%H:%M:%S")
        except:
            found_time = noc_info.found_time

    if noc_info.start_time:
        try:
            start_time = datetime.strftime(noc_info.start_time, "%Y-%m-%dT%H:%M:%S")
        except:
            start_time = noc_info.start_time

    if noc_info.fixed_time:
        try:
            fixed_time = datetime.strftime(noc_info.fixed_time, "%Y-%m-%dT%H:%M:%S")
        except:
            fixed_time = noc_info.fixed_time
    return render_template('detail.html', **locals())

@app.route('/edit_effect_info', methods=["POST"])
@login_required
def edit_effect_info():
    """
    编辑影响
    """
    if request.method == 'POST':
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        serial_number = request.form.getlist('serial_number')[0]
        try:
            NocNoc.query.filter(NocNoc.serial_number == serial_number).update(data)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            raise
        finally:
            db.session.close()

        d = {'res': 'success'}
    return jsonify(d)

@app.route('/edit_action', methods=('GET', 'POST'))
@login_required
def edit_action():
    """
    编辑动作
    """
    if request.method == "POST":
        postData = request.form
        act = request.form.getlist('act')
        if act[0] == 'del':
            id = request.form.getlist('id')[0]
            try:
                NocAffected.query.filter(NocAffected.id == id).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()
            d = {'res': 'success'}
        elif act[0] == 'get':
            id = request.form.getlist('affected_id')
            try:
                db.session.commit()
                d = db.session.query(NocAffected).filter(NocAffected.id == id).first().as_dict()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()
            d['act'] = 'edit'
        elif act[0] == 'edit':
            t = request.form.getlist('form_data')[0]
            dict_data=dict(map(lambda s: s.split('='), t.split('&')))
            edit_dict = {'affected_dept': dict_data['affected_dept'],
                        'affected_team': dict_data['affected_team'],
                        'affected_customer_type': dict_data['affected_customer_type'],
                        'affected_scope': dict_data['affected_scope'], 'affected_money': dict_data['affected_money'],
                        'detail': dict_data['detail']}
            try:
                NocAffected.query.filter(NocAffected.id == dict_data['affected_id']).update(edit_dict)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()
            d = {'res': 'success'}
        else:
            t = request.form.getlist('form_data')[0]
            dict_data=dict(map(lambda s: s.split('='), t.split('&')))
            try:
                db.session.commit()
                noc_info = db.session.query(NocNoc).filter(NocNoc.serial_number == dict_data['case_sn']).first()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()
            add_dict = {'nid': noc_info.id,
                        'affected_dept': dict_data['affected_dept'],
                        'affected_team': dict_data['affected_team'],
                        'affected_customer_type': dict_data['affected_customer_type'],
                        'affected_scope': dict_data['affected_scope'], 'affected_money': dict_data['affected_money'],
                        'detail': dict_data['detail']}
            add_info = NocAffected(**add_dict)

            try:
                db.session.add(add_info)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()
            d = {'res': 'success'}
    return jsonify(d)

@app.route('/imp_action', methods=('GET', 'POST'))
@login_required
def imp_action():
    """
    imp动作
    """
    if request.method == "POST":
        impData = request.form
        imp_act = request.form.getlist('imp_act')
        if imp_act[0] == 'del':
            id = request.form.getlist('id')[0]
            try:
                NocImprovement.query.filter(NocImprovement.id == id).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()
            d = {'res': 'success'}
        elif imp_act[0] == 'get':
            id = request.form.getlist('imp_id')
            try:
                db.session.commit()
                d = db.session.query(NocImprovement).filter(NocImprovement.id == id).first().as_dict()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()
            d['imp_act'] = 'edit'
        elif imp_act[0] == 'edit':
            t = request.form.getlist('imp_data')[0]
            dict_data=dict(map(lambda s: s.split('='), t.split('&')))
            edit_dict = {'title': dict_data['imp_title'],
                        'completion_time': dict_data['imp_completion_time'],
                        'jira_link': dict_data['imp_jira_link'],
                        'improve_team': dict_data['imp_team'],
                        'improve_dept': dict_data['imp_dept'],
                        'assignee': dict_data['imp_username'],
                        'status': dict_data['imp_status']}
            try:
                NocImprovement.query.filter(NocImprovement.id == dict_data['imp_id']).update(edit_dict)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()
            d = {'res': 'success'}
        else:
            t = request.form.getlist('imp_data')[0]
            dict_data=dict(map(lambda s: s.split('='), t.split('&')))
            print(dict_data)
            try:
                db.session.commit()
                noc_info = db.session.query(NocNoc).filter(NocNoc.serial_number == dict_data['case_sn']).first()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()
            add_dict = {'nid': noc_info.id,
                        'title': dict_data['imp_title'],
                        'improve_team': dict_data['imp_team'],
                        'improve_dept': dict_data['imp_dept'],
                        'assignee': dict_data['imp_username'],
                        'completion_time': dict_data['imp_completion_time'],
                        'jira_link': dict_data['imp_jira_link'],
                        'status': dict_data['imp_status']}
            add_info = NocImprovement(**add_dict)
            try:
                db.session.add(add_info)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                raise
            finally:
                db.session.close()
            d = {'res': 'success'}
    return jsonify(d)

@app.route('/edit_actiontest', methods=('GET', 'POST'))
def edit_action_test():
    """
    测试
    """
    case_id = request.form.get('id')
    textdesc = request.form.get('textdesc')
    act = request.form.get('act')
    if act == 'delete':
        try:
            NocNoc.query.filter( NocNoc.serial_number == case_id ).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            raise
        finally:
            db.session.close()
        d = {'res': 'success'}
    return jsonify(d)

@app.route('/reason', methods=('GET', 'POST'))
def reason():
    """
    结果
    """
    path = request.path
    business = requests.get("http://cmdb.xxx-int.com/api/v1/business/")
    subbusiness = requests.get("http://cmdb.xxx-int.com/api/v1/subbusiness/")
    b = business.json()
    sb = subbusiness.json()
    affected_customer_type = {u'内部':1, u'外部':2}
    case_sn = request.args.get('sn')
    try:
        db.session.commit()
        noc_info = db.session.query(NocNoc).filter(NocNoc.serial_number == case_sn).first()
        reasons_info = db.session.query(NocReasons).filter(NocReasons.parent_id == 0).all()
        sub_reasons_info = db.session.query(NocReasons).filter(NocReasons.parent_id != 0).all()
        print(reasons_info[0].name)

        priority_info = db.session.query(NocPriority).all()
        affected_info = db.session.query(NocAffected).filter(NocAffected.nid == noc_info.id).all()
        imp_info = db.session.query(NocImprovement).filter(NocImprovement.nid == noc_info.id).all()
    except Exception as e:
        db.session.rollback()
        print(e)
        raise
    finally:
        db.session.close()

    if noc_info.found_time:
        try:
            found_time = datetime.strftime(noc_info.found_time, "%Y-%m-%dT%H:%M:%S")
        except:
            found_time = noc_info.found_time

    if noc_info.start_time:
        try:
            start_time = datetime.strftime(noc_info.start_time, "%Y-%m-%dT%H:%M:%S")
        except:
            start_time = noc_info.start_time

    if noc_info.fixed_time:
        try:
            fixed_time = datetime.strftime(noc_info.fixed_time, "%Y-%m-%dT%H:%M:%S")
        except:
            fixed_time = noc_info.fixed_time
    return render_template('reason.html', **locals())

@app.route('/sub_reason', methods=('GET', 'POST'))
def noc_reason():
    """
    noc reason
    """
    if request.method == "POST":
        postData = request.form
        parentId = request.form.getlist('parentId')
        noc_reasons = db.session.query(NocReasons).filter(NocReasons.parent_id == parentId).all()
        d = []
        for u in noc_reasons:
            d.append({x.name: getattr(u, x.name) for x in u.__table__.columns})
    return jsonify(d)

@app.route('/sub_business', methods=('GET', 'POST'))
def sub_business():
    if request.method == "POST":
        postData = request.form
        sbid = request.form.getlist('sbid')
        business = requests.get("http://cmdb.xxx-int.com/api/v1/business/")
        b = business.json()
        for i in b:
            if str(i['id']) == sbid[0]:
                sapi = "http://cmdb.xxx-int.com/api/v1/business/allsub/" + i['name']
                subbusiness = requests.get(sapi)
        sb = subbusiness.json()
    return jsonify(sb['data']['sub'])

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.debug = True
    app.run()
