# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: AppiumServer.py
@time: 2019/06/10 9:03
"""

import os
import urllib.request
from multiprocessing import Process
import threading
import time
import platform
import subprocess
from utils.log import LOG,logger
from utils.py_kill_process import AppiumProcess
"""
启动appium服务
"""

class RunServer(threading.Thread):#启动服务的线程
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        os.system(self.cmd)

class AppiumServer(object):

    def __init__(self,kwargs):
        self.kwargs=kwargs

    def run(self, url):
        time.sleep(5)
        response = urllib.request.urlopen(url, timeout=5)
        if str(response.getcode()).startswith("2"):
            return True

    def start_server(self): #开启服务
        for item in self.kwargs:
            cmd = "appium --session-override  -p %s  -U %s" % (item["port"],  item["devices"])
            LOG.info(platform.system())
            if platform.system() == "Windows":  # windows下启动server
                t1 = RunServer(cmd)
                p = Process(target = t1.start())
                p.start()
                while True:
                    time.sleep(4)
                    if self.run("http://127.0.0.1:{}/wd/hub/status".format(item["port"])):
                        LOG.info("-------win_server_ 成功--------------")
                        break
            else:
                process_cmd = "lsof -i:{0}".format(item["port"])
                ap = AppiumProcess(process_cmd)
                if ap.is_node_process:
                    ap.kill_process()

                appium = subprocess.Popen(
                    cmd,
                    shell = True,
                    stdout = subprocess.PIPE,
                    stderr = subprocess.PIPE,
                    bufsize = 1,
                    close_fds = True
                )
                while True:
                    appium_line = appium.stdout.readline().strip().decode()
                    LOG.info("---------start_server----------")
                    time.sleep(2)
                    if 'listener started' in appium_line:
                        print(appium_line)
                        LOG.info("----server启动成功---")
                        break

    def stop_server(self, devices):
        LOG.info(devices)
        platform_sys = platform.system()
        if platform_sys == 'Windows':
            os.popen("taskkill /f /im node.exe")
        else:
            for device in devices:
                cmd = "lsof -i:{0}".format(device["port"])
                ap = AppiumProcess(cmd)
                if ap.is_node_process:
                    ap.kill_process()

                # plist = os.popen(cmd).readlines()
                # if plist:
                #     plists = plist[1].split()
                #     os.popen("kill -9 {0}".format(plists[0]))