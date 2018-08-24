# -*- coding: utf-8 -*-
__author__ = 'xujianbo'
__data__ = '2018-08-19'

import os
import configparser


class Config:
    def __init__(self):
        self.root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.log_path = os.path.join(self.root_path, "logs")
        self.report_path = os.path.join(self.root_path, "TestReport")
        self.evm_path = os.path.join(self.root_path, "api\\apiconfig\\evm.ini")
        self.t_config_path = os.path.join(self.root_path, "api\\apiconfig\\test\\config.ini")
        self.o_config_path = os.path.join(self.root_path, "api\\apiconfig\\test\\config.ini")
        self.case_path = os.path.join(self.root_path, "TestCase")

    def getConfig(self, config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        return config

    def setScene(self, scene):
        """
        Jenkins持续集成时设置运行的环境
        @:param scene 运行的环境
        """
        config_path = os.path.join(self.evm_path)
        config = self.getConfig(config_path)
        config.set("environment", "scene", scene)
        config.write(open(config_path, "r+"))

    def getScene(self):
        """
        Jenkins持续集成时获取运行的环境
        @:param scene 运行的环境
        """
        config = self.getConfig(self.evm_path)
        return config.get("environment", "scene")


# if __name__ == "__main__":
#     print Config().o_config_path