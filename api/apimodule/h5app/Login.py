# -*- coding: utf-8 -*-
from api.apipub import Database

__author__ = 'xujianbo'
from api.apipub.HttpRequest import SendHttpRequest


class Login:
    def __init__(self,userName, password):
        header = {
            "Accept": "application/json",
            "versionName": "1.0.1",
        }
        value = {
            "name": userName,
            "clientId": "c977c4f7929803a01215fcc845672505",
            "password": password
        }

        url = "http://h5app.wx.pxsj.com/api/shop/getToken"
        self.response = SendHttpRequest().postJsonValue(url=url, value=value)

    # 登录获取token
    def getToken(self):
        try:
            return self.response.get("response").get("token")
        except Exception,e:
            return e.message + self.response.get("msg")
    #获取shopId
    def getShopId(self):
        try:
            return self.response.get("response").get("shopId")
        except Exception,e:
            return e.message + self.response.get("msg")