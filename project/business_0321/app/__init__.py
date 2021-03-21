# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    _init_
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config
from .urls import init_urls
from .db import db

def create_app(config_name):
    """
    创建app对象
    """
    app = Flask(__name__,
                template_folder='../dist/templates',
                static_folder='../dist/static')
    app.debug = app.config['DEBUG']    #配置为Debug模式，这样修改文件后，会自动重启服务
    app.config['JSON_AS_ASCII'] = False

    app.config.from_object(config[config_name])

    db.init_app(app)
    init_urls(app)
    return app

