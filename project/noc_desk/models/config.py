# -*- coding: UTF-8 -*-



class BaseCongfig():
    NOC_URL = 'https://noc.guazi-cloud.com'
    SSO_URL = 'https://sso.guazi-cloud.com'
    LOGIN_RETURN_URL = '/account/login?returnUrl='
    LOGOUT_RETURN_URL = '/account/logOut?returnUrl='
    SSO_LOGIN_API = '/account/logInApi'
    SSO_LOGOUT_API = '/account/logOutApi'
    GET_USERINFO_API = '/account/identity'


config = {
    'base': BaseCongfig
}