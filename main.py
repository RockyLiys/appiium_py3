# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: main.py
@time: 2019/06/10 9:03
"""
"""
主运行文件

"""
from utils.read_excel import create
from utils.log import LOG,logger
from  utils.make_case import makecasefile
from multiprocessing import Pool
from  cases.reg_case_test import Regtest
from  utils.Parmeris import Parmer
from utils.AppiumServer import AppiumServer
from  utils.base_apk import getPhoneInfo,AndroidDebugBridge
import os
import unittest
import random
import datetime

from config.config import  base_dir

l_devices=[]

@logger('生成设备配置链接的进程池')
def runner_pool(getDevices):
    """
       根据链接的设备生成不同的dict
       然后放到设备的list里面
       设备list的长度产生进程池大小
    """
    devices_Pool = []
    for device in getDevices:
        _pool = []
        _initApp = {
            "udid": device["devices"],
            "port": device["port"],

            "deviceName": device["devices"],
            "platformVersion": getPhoneInfo(devices=device["devices"])["release"],
            "platformName": "android",
            "appPackage": 'com.aixuetang.online',
            "appActivity": 'com.aixuetang.mobile.activities.LaunchActivity'
        }
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pools = Pool(processes=1)   # 定义CPU核数量为3
    res = pools.map(runner_case_app, devices_Pool)  # 把测试用例放到设置到进程池
    LOG.info(res)
    pools.close()
    pools.join()

@logger('组织测试用例')
def runner_case_app(devices):
    """
        利用unittest的testsuite来组织测试用例
    """
    LOG.info(devices)
    test_suit = unittest.TestSuite()

    test_suit.addTest(Parmer.parametrize(Regtest, param=devices)) #扩展的其他的测试用例均这样添加

    unittest.TextTestRunner(verbosity=2).run(test_suit)


if __name__=="__main__":
    LOG.info("测试开始执行")
    start_time = datetime.datetime.now()
    devices = AndroidDebugBridge().attached_devices()
    LOG.info(devices)
    # makecasefile('reg','reg','reg') #没有的时候才会生成，一般都会有这个文件   暂时关掉
    if len(devices) > 0:
        for dev in devices:
            app = {
                "devices": dev,
                "port": "4723"  #str(random.randint(4700, 4723))
            }
            l_devices.append(app)

        # appium开始
        appium_server = AppiumServer(l_devices)
        appium_server.start_server() #启动服务
        runner_pool(l_devices)

        try:
            appium_server.stop_server(l_devices)
        except Exception as e:
            LOG.info("关闭服务失败，原因：{}".format(e))


        end_time = datetime.datetime.now()
        hour = end_time - start_time
        # 生成测试报告
        filenm = os.path.join(base_dir, 'reports/result.xls')
        create(filename=filenm, devices_list=devices, Test_version='2.0.1', testtime=str(hour))
        LOG.info("测试执行完毕，耗时：{}".format(hour))
    else:
        LOG.info("没有可用的安卓设备")
        # print("没有可用的安卓设备")