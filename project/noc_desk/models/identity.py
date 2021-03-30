# coding:utf-8

from flask import g, abort, redirect, current_app
from models.sso import Sso
from models.models import User, Administrator, db
from functools import wraps
from elasticsearch import Elasticsearch

def get_user_info():
    if "user_info" in g:
        return g.user_info

    user_info = Sso.user_info_by_token()
    if Sso.valid_user_info(user_info):
        g.user_info = user_info

    return g.get("user_info")


def get_user_id():
    user_info = get_user_info()
    if user_info:
        return user_info.get("user_id")
    return

def get_user_role():
    user_id = get_user_id()
    try:
        #user = User.query.filter_by(user_id=user_id).first()
        user = db.session.query(User).filter_by(user_id=user_id).first()
        if not user:
            return "get user role fail!"
        return user.role.name
    except Exception as e:
        db.session.rollback()
        print(e)
        raise
    finally:
        db.session.close()


def login_required(func):
    @wraps(func)
    def auth(*args, **kwargs):
        if get_user_info():
            return func(*args, **kwargs)
        else:
            return redirect(current_app.config['SSO_URL'] + current_app.config.get('LOGIN_RETURN_URL') + current_app.config.get('NOC_URL'))
    return auth


def is_admin(func):
    @wraps(func)
    def admin(*args, **kwargs):
        user_id = get_user_id()
        if not user_id:
            return abort(401)

        if Administrator(user_id):
            return func(*args, **kwargs)
        else:
            return abort(403)
    return admin

def insert_es(doc_type,index,json):
    es    = Elasticsearch([{"host":"es-log.dns.guazi.com","port":9200,"timeout":150}])
    res = es.index(
                doc_type=doc_type,
                index=index,
                body=json,
            )
    return res