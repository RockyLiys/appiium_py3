# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: make_case.py
@time: 2019/06/10 9:03
"""

import  os
from utils.log import  LOG
from config.config import base_dir

def  readheader():
    path_new = os.path.join(base_dir, 'template/case.txt')
    return open(path_new,encoding='utf-8').read()

def readerconet():
    path_new = os.path.join(base_dir, "template/content.txt")
    conet = open(path_new, encoding='utf-8').read()
    return conet

def  makecasefile(casename, desc, funtionname):

    LOG.info("开始生成测试用例文件")
    filepath = os.path.join(base_dir, 'cases/{}casetest.py'.format(casename))
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(readheader().format(casename, casename))
            file.write(readerconet().format(funtionname, desc))
    else:
        pass