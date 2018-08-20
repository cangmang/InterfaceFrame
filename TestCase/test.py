# -*- coding: utf-8 -*-

__author__ = 'xujianbo'
__date__ = '2018-08-17'
"""
"""
import unittest
from api.apidata.apiset import apiset

from api.apimodule.h5app.Login import Login
from api.apipub.HttpRequest import SendHttpRequest


class testClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login = Login("18280372006", "e4c0884a449ef1bdc50c69a42b173779")
        cls.token = cls.login.getToken()
        cls.shopId = cls.login.getShopId()
        cls.version_name = apiset().getConfigValues("version", "version_name")

    @classmethod
    def tearDownClass(cls):
        pass

    def testGetShopInfo(self):
        headers = {
            "versionName": self.version_name,
            "token": self.token,
            "shopId": "shopId"
        }
        response = SendHttpRequest().get("http://h5app.wx.pxsj.com/api/shop/getShopInfo", headers=headers)
        self.assertEqual(response.get("code"), "20000000", response.get("msg"))


if __name__ == '__main__':
    unittest.main()
