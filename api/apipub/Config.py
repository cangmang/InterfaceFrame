# -*- coding: utf-8 -*-
__author__ = 'xujianbo'
__data__ = '2018-08-19'

import os
import configparser



class Config:
    def __init__(self):
        pass

    def getConfig(self, config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        return config

    def setScene(self, scene):
        """
        Jenkins持续集成时设置运行的环境
        @:param scene 运行的环境
        """
        path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(os.path.dirname(path) + "\\apidata\\evm.ini")
        config = self.getConfig(config_path)
        config.set("environment", "scene", scene)
        config.write(open(config_path, "r+"))

    def getScene(self):
        """
        Jenkins持续集成时获取运行的环境
        @:param scene 运行的环境
        """
        path = os.path.dirname(os.path.abspath(__file__))
        config = self.getConfig(os.path.join(os.path.dirname(path) + "\\apidata\\evm.ini"))
        return config.get("environment", "scene")

# if __name__ == "__main__":
        # Config().setScene("1211")