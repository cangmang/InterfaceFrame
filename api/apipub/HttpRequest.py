# -*- coding: utf-8 -*-
import urllib
import sys, importlib

from api.apiconfig.apiset import apiset

__author__ = 'xujianbo'
__data__ = '2018-03-20'
"""
"""
from api.apipub.PyApiLog import log
import requests


class SendHttpRequest:
    def __init__(self, url, username, password):
        self.req_url = url
        self.username = username
        self.password = password
        self.token = self._get_token("/token")

    def _get_token(self, path):
        try:
            res = requests.post(
                self.req_url + path,
                params={
                    'username': self.username,
                    'password': self.password,
                },
                verify=False,
                )
            res_dict = res.json()
            if 'access_token' in res_dict:
                return res_dict['access_token']
            else:
                raise Exception('未获取到访问token!')

        except Exception as e:
            raise Exception(e)

    def get(self, path, **kwargs):
        """封装get方法"""
        # 获取请求参数
        params = kwargs.get("params", {})
        headers = kwargs.get("headers", {})
        headers['Authorization'] = "Bearer {}".format(self.token)
        try:
            result = requests.get(self.req_url + path,
                                  params=params,
                                  headers=headers,
                                  verify=False)
            return result
        except Exception as e:
            raise Exception("get请求错误: %s" % e)

    def post(self, path, **kwargs):
        """封装post方法"""
        # 获取请求参数
        params = kwargs.get("params", {})
        data = kwargs.get("data", {})
        jn = kwargs.get("json", {})
        headers = dict()
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer {}'.format(self.token)
        try:
            result = requests.post(self.req_url + path,
                                   params=params,
                                   data=data,
                                   json=jn,
                                   headers=headers,
                                   verify=False)
            return result
        except Exception as e:
            raise Exception("post请求错误: %s" % e)