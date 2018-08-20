# -*- coding: utf-8 -*-
__author__ = 'xujianbo'
__data__ = '2018-08-19'

import os

from api.apipub.Config import Config

"""
获取配置文件的值
@:param path 配置文件（ini）绝对路径
"""


class apiset:
    def __init__(self, path=None):
        if path == None:
            path = os.path.dirname(__file__)
            scene = Config().getScene()
            if scene == 'test':
                self.config_path = os.path.join(os.path.abspath(path) + "\\test\\config.ini")
            elif scene == 'online':
                self.config_path = os.path.join(os.path.abspath(path) + "\\online\\config.ini")
            else:
                assert "请指定运行环境：test or online"
        else:
            self.config_path = path
        self.config = Config().getConfig(self.config_path)

    def getConfigValues(self, section, option):
        """
        根据传入的section获取对应的value
        :param section: ini配置文件中用[]标识的内容
        :return:
        """
        return self.config.get(section=section, option=option)

    def getConfigItems(self, section):
        """
        根据传入的section获取对应的value
        :param section: ini配置文件中用[]标识的内容
        :return:
        """
        return self.config.items(section=section)


        # if __name__ == "__main__":
        # print apiset().getConfigItems("mysql_db")