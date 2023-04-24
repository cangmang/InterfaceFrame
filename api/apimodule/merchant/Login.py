# -*- coding: utf-8 -*-
import requests

__author__ = 'Administrator'
__date__ = '2018/8/24'
"""
"""
from api.apipub.HttpRequest import SendHttpRequest


class Login:
    def __init__(self):
        self.url = "http://192.168.31.233:8010/noauth/merchant/v2/login"
        self.userAccount = "ssssddfffff"
        self.pwd = "ca6b6a18e116a4a30f9ba52d4e2c0c2c"
        value = {
            "userAccount": self.userAccount,
            "pwd": self.pwd
        }
        header = {
            "Accept": "application/json",
            "appID": "android_m_1_0_3"
        }

        self.response = SendHttpRequest().postByJson(self.url, value=value,headers=header)

    def login(self):
        return self.response

    def getToken(self):
        return self.response.get("response").get("token")

    def getUserId(self):
        return self.response.get("response").get("userId")

    def getShopId(self):
        return self.response.get("response").get("shopId")


# if __name__ == "__main__":
#     Login().login()