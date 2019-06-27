# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: reg_case_test.py
@time: 2019/06/10 9:03
"""

from appium import webdriver
import ddt
import os
import time
import unittest
from utils.Parmeris import Parmer
from utils.log import LOG
from utils.init_app_params import make_dis
from utils.obtain_test_data import obtain_test_data
from funtions.regpub import RegFun
from utils.obtain_performance import caijicpu,getnencun
from utils.recording_txt import write_recording
from config.config import AppPackage, base_dir, app_path

from utils.save_result import save_result


data_test = obtain_test_data(os.path.join(base_dir, 'data/testcase_data.xlsx'), index=1)


@ddt.ddt
class Regtest(Parmer):

    def __init__(self, parm, methodName='runTest'):
        super(Regtest, self).__init__(methodName)
        self.port = parm['port']  # appium连接端口
        self.udid = parm["udid"]  # appium连接设备
        self.parm = parm

    # 这是reg测试用例
    def setUp(self):
        """
        setup

        """
        LOG.info("setUp....")
        self.dis_app = make_dis(self.parm)
        LOG.info('http://127.0.0.1:{}/wd/hub'.format(self.port))
        self.driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(self.port), self.dis_app)
        if not self.driver.is_app_installed(AppPackage):
            self.driver.install_app(app_path)

        LOG.info(self.driver)
        LOG.info('reg测试用例开始执行')

    def tearDown(self):
        """
            tearDown
        """
        LOG.info("tearDown....")
        if self.driver.is_app_installed(AppPackage):
            self.driver.remove_app(AppPackage)
        LOG.info('测试用例执行完毕，测试环境正在还原！')
        time.sleep(5)
        self.driver.quit()

    def test_swipe(self):
        # 打印屏幕高和宽
        window_size = self.driver.get_window_size()
        x = window_size["width"]
        y = window_size["height"]
        LOG.info("印屏幕大小 window={}".format(window_size))

        self.driver.swipe(6/7*x, 1/2*y, 1/7*x, 1/2*y, 100)

    @unittest.skip("先跳过注册实例")
    @ddt.data(*data_test)
    def test_reg(self, data_test):
        """
        reg测试
        """
        regfun = RegFun(driver=self.driver)
        self.assertuen = regfun.reg(**data_test)

        cpu = caijicpu(
            packagename = AppPackage,
            devices = self.parm['deviceName']
        )
        neicun = getnencun(
            packagename = AppPackage,
            devices=self.parm['deviceName']
        )
        write_recording(
            cpu=cpu,
            neicun=neicun,
            devices=str(self.parm['deviceName'])
        )
        if data_test['assert'] == self.assertuen:
            device = self.parm['udid']
            data = "&".join([device, "pass", str(data_test)]) #shebei+'&'+'pass'+'&'+str(data_test)
            save_result(data)
        else:
            # shebei = self.parm['udid']
            data = "&".join([self.parm['udid'], "fail"]) #shebei + '&' + 'fail'
            save_result(data)