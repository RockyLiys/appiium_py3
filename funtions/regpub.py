# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: regpub.py
@time: 2019/06/10 9:03
"""
'''
注册测试
'''
from utils.log import LOG,logger
from exce_test_funs.test_fun import MakeAppCase
import os
from config.config import base_dir

path_yongli = os.path.join(base_dir, 'data/dingwei/reg.yaml')

@logger('注册测试')
class RegFun:
    def __init__(self,driver):
        self.driver = driver
        self.path = path_yongli
        self.open = MakeAppCase(self.driver, path=self.path)

    def reg(self,**kwargs):
        f = self.open.exce_case(**kwargs)
        if f['code']==1:
            LOG.info('无法获取断言')
            return
        else:
            beijing = f['data']
            return beijing