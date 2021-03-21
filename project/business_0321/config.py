# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    config
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

cache_config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': 'ip',
    'CACHE_REDIS_PORT': port,
    'CACHE_REDIS_DB': '1',
    'CACHE_REDIS_PASSWORD': 'password'
}

class BaseConfig:
    """
    基本配置类
    """
    SECRET_KEY = 'Sre'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(BaseConfig):
    """
    测试环境
    """
    PRESTO_DOMAIN = "presto.xxx-apps.com"
    PRESTO_PORT = 9400
    PRESTO_USER = "Visionguo"
    PRESTO_GROUP = "presto-sre"
    PRESTO_PASSWORD = "passport"
    PRESTO_CATALOG = "hive"
    PRESTO_SCHEMA = "sre"
    TESTING = True

    CMDB_DOMAIN = "http://cmdb.xxx-int.com"
    CMDB_DATABASE_URI = "mysql+pymysql://prime_w:password@ip:port/cmdb?charset=utf8"
    EARTHWORM_DATABASE_URI = "mysql+pymysql://eathworm_r:passwordd@ip:port/eathworm"
    MEDUSA_DATABASE_URI = "mysql+pymysql://eathworm_r:password@ip:port/saber"

    CACHE_HOST = "ip"
    CACHE_PORT = "80"
    CACHE_PASSWORD = "password"
    NOC_DATABASE_URL = "mysql+pymysql://noc:password@ip/noc?charset=utf8"
    BIGDATA_DATABASE_URL = "mysql+pymysql://root:root@hostname/sre?charset=utf8"
    CACHE_DOMAIN = "http://127.0.0.1:5000/"

class ProductionConfig(BaseConfig):
    """
    生产环境
    """
    TESTING = True
    PRESTO_DOMAIN = "presto.xxx-apps.com"
    PRESTO_PORT = 9400
    PRESTO_USER = "Visionguo"
    PRESTO_GROUP = "presto-sre"
    PRESTO_PASSWORD = "password"
    PRESTO_CATALOG = "hive"
    PRESTO_SCHEMA = "sre"

    CMDB_DOMAIN = "http://cmdb.xxx-int.com"
    CMDB_DATABASE_URI = "mysql+pymysql://xxx_cmdb_r:password@hostname:3405/xxx_cmdb?charset=utf8"
    EARTHWORM_DATABASE_URI = "mysql+pymysql://saber_earth_r:password@hostname:3405/earthworm"
    MEDUSA_DATABASE_URI = "mysql+pymysql://saber_earth_r:password@hostname:3405/saber"

    CACHE_HOST = "ip"
    CACHE_PORT = "6379"
    CACHE_PASSWORD = "password"
    CACHE_DOMAIN = "http://business.xxx-int.com/"

config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': TestingConfig
}
