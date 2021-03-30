# coding:utf-8
from flask import request, session, current_app
import requests




class Sso:
    @staticmethod
    def user_info_by_token():
        session["token"] = request.cookies.get("GUAZISSO", None)
        print(session.get("token"))

        if not session.get("token"):
            return "Get token fail !"

        url = current_app.config.get('SSO_URL') + current_app.config.get('GET_USERINFO_API')
        post_data = {"token": session.get("token")}
        re = requests.post(url, post_data)
        data = re.json()

        if data.get("status") is False:
            return
        return data.get("userInfo", None)


    @staticmethod
    def valid_user_info(user_info):
        require_item = ["user_id", "fullname", "email"]
        for item in require_item:
            if item not in user_info:
                return False
        return True


    @staticmethod
    def logout_token():
        url = current_app.config.get('SSO_URL') + current_app.config.get('GET_USERINFO_API')
        post_data = {"token": session.get("token")}
        re = requests.post(url, post_data)
        data = re.json()
        return data.get("status", None)


