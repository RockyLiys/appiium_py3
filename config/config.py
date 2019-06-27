"""
@author: rocky
@file: config.py
@time: 2019/06/10 10:05
"""
'''
配置app以及测试设备的相关信息
'''

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 项目首路径

AppPackage = 'com.aixuetang.online'#被测应用名称
TestandroidDeviceReadyTimeout = 30    #超时时间
TestunicodeKeyboard = True
TestresetKeyboard = True

Dingtalk_access_token =''#钉钉的token
Test_Project_name = ''
TiTestuser = ''
Test_user="自动化"
app_path = os.path.join(base_dir, "data/packages/com.aixuetang.online.apk")


