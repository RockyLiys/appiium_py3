# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: init_app_params.py
@time: 2019/06/10 9:03
"""
'''
从配置文件获取相关的app测试配置信息
'''
from  config.config import *
from  utils.log import logger

@logger('开始从配置文件中获取测试相关的配置')
def make_dis(params):
    return {
        'platformName': params['platformName'],
        'platformVersion': params['platformVersion'],
        'deviceName': params['deviceName'],
        'appPackage': params['appPackage'],
        'appActivity': params['appActivity'],
        'app': app_path,

        'androidDeviceReadyTimeout': TestandroidDeviceReadyTimeout,
        'unicodeKeyboard': TestunicodeKeyboard,
        'resetKeyboard': TestresetKeyboard
    }
