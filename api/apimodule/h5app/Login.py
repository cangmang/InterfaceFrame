# -*- coding: utf-8 -*-
from api.apipub import Database

__author__ = 'xujianbo'
from api.apipub.HttpRequest import SendHttpRequest


class Login:
    def __init__(self, userName, password):
        value = {
            "name": userName,
            "clientId": "c977c4f7929803a01215fcc845672505",
            "password": password
        }

        url = ""
        self.response = SendHttpRequest().postByData(url=url, value=value)

    # 登录获取token
    def getToken(self):
        try:
            return self.response.get("response").get("token")
        except Exception as e:
            return e.message + self.response.get("msg")

    # 获取shopId
    def getShopId(self):
        try:
            return self.response.get("response").get("shopId")
<<<<<<< HEAD
        except Exception as e:
            return e.message + self.response.get("msg")
=======
        except Exception, e:
            return e.message + self.response.get("msg")
>>>>>>> a29f1cf8174034e04410b6becdb8d006f509f84d
