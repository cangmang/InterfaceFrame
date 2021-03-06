# -*- coding: utf-8 -*-
import urllib
import sys
from api.apiconfig.apiset import apiset

__author__ = 'xujianbo'
__data__ = '2018-03-20'
"""
"""
from api.apipub.PyApiLog import log
import requests


class SendHttpRequest:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.version_name = apiset().getConfigValues("version", "version_name")
        self.header = {
            "Accept": "application/json",
            "versionName": self.version_name
        }


    def postByparam(self, url, value, headers=None, timeout=3):
        if headers == None:
            headers = self.header
        params = urllib.urlencode(value)
        try:
            req = requests.post(url + "?%s" % params, headers=headers, timeout=timeout)
        except Exception, err:
            log().error("接口" + url + "请求失败：" + err.message)
            print err.message
        if req.status_code == 200:
            log().info(u"发送post请求: %s  服务器返回:  %s" % (req.url, req.status_code))
        else:
            log().error(u"发送post请求: %s   服务器返回:  %s\n error info: %s " % (req.url, req.status_code, req.text))
        return req.json()

    def postByJson(self, url, value=None, headers=None, timeout=3):
        if headers == None:
            headers = self.header
        try:
            req = requests.post(url, json=value, headers=headers, timeout=timeout)
            print req.url
        except Exception, err:
            log().error("接口" + url + "请求失败：" + err.message)
            print err.message
        if req.status_code == 200:
            log().info(u"发送post请求: %s  服务器返回:  %s" % (req.url, req.status_code))
            return req.json()
        else:
            log().error(u"发送post请求: %s   服务器返回:  %s\n error info: %s " % (req.url, req.status_code, req.text))
            print req.text

    def postByData(self, url, value=None, headers=None, timeout=3):
        if headers == None:
            headers = self.header
        try:
            req = requests.post(url, data=value, headers=headers, timeout=timeout)
            print req.url
        except Exception, err:
            log().error("接口" + url + "请求失败：" + err.message)
            print err.message
        if req.status_code == 200:
            log().info(u"发送post请求: %s  服务器返回:  %s" % (req.url, req.status_code))
            return req.json()
        else:
            log().error(u"发送post请求: %s   服务器返回:  %s\n error info: %s " % (req.url, req.status_code, req.text))
            print req.text

    def get(self, url, value=None, headers=None, timeout=3):
        if headers == None:
            headers = self.header
        try:
            req = requests.get(url, params=value, headers=headers, timeout=timeout)
        except Exception, err:
            log().error("接口" + url + "请求失败：" + err.message)
            print err.message
        if req.status_code == 200:
            log().info(u"发送get请求: %s   服务器返回:  %s" % (req.url, req.status_code))
        else:
            log().error(u"发送get请求: %s   服务器返回:  %s\n error info: %s " % (req.url, req.status_code, req.text))
            print req.text
        return req.json()