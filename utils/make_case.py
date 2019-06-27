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

def  read_header():
    path_new = os.path.join(base_dir, 'template/case.txt')
    return open(path_new,encoding='utf-8').read()

def reader_conntent():
    path_new = os.path.join(base_dir, "template/content.txt")
    conet = open(path_new, encoding='utf-8').read()
    return conet

def  make_case_files(case_name, desc, funtion_name):

    LOG.info("开始生成测试用例文件")
    file_path = os.path.join(base_dir, 'cases/{}_case_test.py'.format(case_name))
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(read_header().format(case_name, case_name))
            file.write(reader_conntent().format(funtion_name, desc))
    else:
        pass