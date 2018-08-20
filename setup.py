# -*- coding: utf-8 -*-
"""
运行自动安装Python框架所需要的库
"""
import os

if __name__ == '__main__':
    installFile = os.path.join(os.path.dirname(__file__), 'requirements')
    os.system('pip install -r ' + installFile)
