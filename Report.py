# -*- coding: utf-8 -*-

__author__ = 'xujianbo'
__data__ = '2015-03-20'
"""
生成测试报告存放在项目report文件夹下
"""
import unittest
import time
import os
import sys
from api.apipub.Config import Config
from api.apiconfig.apiset import apiset

from api.apipub import HTMLTestRunner



class Report:
    def startAllCase(self):
        """
        使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
        @:param filename 报告存放路径
        @:param Report_title 报告标题
        @:param Report_description 报告描述信息
        """
        Report_title = apiset().getConfigValues("report", "title")
        Report_description = apiset().getConfigValues("report", "description")
        discover = unittest.defaultTestLoader.discover(Config().case_path, pattern='test*.py',
                                                       top_level_dir=None)
        file_path = Config().report_path
        try:
            os.mkdir(file_path)
        except:
            pass
        finally:
            filename = os.path.join(file_path,
                                    (time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time())) + '.html'))

        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=Report_title,
                                               description=Report_description
                                               )
        try:
            runner.run(discover)
        except Exception as e:
            raise Exception(e.message)
        finally:
            fp.close()
            # os.system("adb emu kill")


if __name__ == "__main__":
    try:
        tag = sys.argv[1]
        if tag == "test" or tag == "online":
            Config().setScene(tag)
            Report().startAllCase()
        else:
            print (u"请指定正确的运行环境：test or online")
    except:
        # 没指定任何环境时默认在测试环境执行
        tag = "test"
        Config().setScene(tag)
        Report().startAllCase()
