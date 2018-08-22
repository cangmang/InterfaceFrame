# -*- coding: utf-8 -*-
__author__ = 'xujianbo'
__data__ = '2018-03-20'
"""
实现json字符串的转换和比较
"""
import json

import xmltodict

from api.apipub.PyApiLog import log


# 解析json字符串
class jsonprase(object):
    def __init__(self, json_value):
        try:
            self.json_value = json.loads(json_value)
        except ValueError, e:
            log().error(e)

    def find_json_node_by_xpath(self, xpath):
        elem = self.json_value
        nodes = xpath.strip("/").split("/")
        for x in range(len(nodes)):
            try:
                elem = elem.get(nodes[x])
            except AttributeError:
                elem = [y.get(nodes[x]) for y in elem]
        return elem

    def datalength(self, xpath="/"):
        return len(self.find_json_node_by_xpath(xpath))

    @property
    def json_to_xml(self):
        try:
            root = {"root": self.json_value}
            xml = xmltodict.unparse(root, pretty=True)
        except ArithmeticError, e:
            log().error(e)
        return xml


# 解析xml字符串
class xmlprase(object):
    def __init__(self, xml_value):
        self.xml_str = xml_value

    @property
    def xml_to_json(self):
        try:
            xml_dic = xmltodict.parse(self.xml_str,
                                      encoding="utf-8",
                                      process_namespaces=True,
                                      )
            json_str = json.dumps(xml_dic)
        except Exception, e:
            print e
        return json_str


class jsonAssert:
    # 对json字符串深度断言----比较两个json字符串是否完全相同，并返回不相同的部分
    def compareJsonData(self, json1, json2, L=[], xpath='json1'):
        if xpath == "json1":
            self.standard = "json1"
            self.standard1 = "json2"
        elif xpath == "json2":
            self.standard = "json2"
            self.standard1 = "json1"
        if isinstance(json1, list) and isinstance(json2, list):
            for i in range(len(json1)):
                try:
                    self.compareJsonData(json1[i], json2[i], L, xpath + '[%s]' % str(i))
                except:
                    L.append('%s中%s[%s]的值:%s未在%s中对应位置找到\n' % (self.standard, xpath, i, json1[i], self.standard1))
        if isinstance(json1, dict) and isinstance(json2, dict):
            for i in json1:
                try:
                    json2[i]
                except:
                    print json1
                    L.append('%s中%s的key：%s未在%s中对应位置找到\n' % (self.standard, xpath, i, self.standard1))
                    continue
                if not (isinstance(json1.get(i), (list, dict)) or isinstance(json2.get(i), (list, dict))):
                    if type(json1.get(i)) != type(json2.get(i)):
                        if self.standard == "json1":
                            L.append('json1、json2中存在类型不同的参数:  %s["%s"]  ===> %s is %s, %s is %s \n' % (
                            xpath, i, self.standard, type(json1.get(i)), self.standard1, type(json2.get(i))))
                    elif json1.get(i) != json2.get(i):
                        if self.standard == "json1":
                            L.append(
                            'json1、json2中存在内容不同的参数:  %s["%s"]  ===> %s is %s, %s is %s \n' % (
                                xpath, i, self.standard, json1.get(i), self.standard1, json2.get(i)))
                    continue
                self.compareJsonData(json1.get(i), json2.get(i), L, xpath + '["%s"]' % str(i))
            return
        if type(json1) != type(json2):
            if self.standard == "json1":
                L.append('json1、json2中存在类型不同的参数:  %s  ===> %s is %s, %s is %s \n' % (
                xpath, self.standard, type(json1), self.standard1, type(json2)))
        elif json1 != json2 and type(json1) is not list:
            if self.standard == "json1":
                L.append('json1、json2中存在内容不同的参数:  %s  ===> %s is %s, %s is %s \n' % (
                xpath, self.standard, json1, self.standard1, json2))
        return L

    def equal(self, json1, json2):
        C = []
        self.compareJsonData(json1, json2, C)
        self.compareJsonData(json2, json1, C, xpath="json2")
        assert len(C) == 0, "\n" + "".join(C)


# if __name__ == '__main__':
#     dict1 = {"name": "zhangsan", "fridents": [{"name": [2, 2, 3]}, {"name": "wangwu"}], "sex": 1}
#     dict2 = {"name": "zhangsan", "fridents": [{"name": [2, 2, 3]}, {"name": "wangwu"}, 12]}
#     d1 = [1, 2, 3]
#     d2 = [1, 1, 3]
#     jsonAssert().equal(dict1, dict2)
    # jsonAssert().equal(d1, d2)