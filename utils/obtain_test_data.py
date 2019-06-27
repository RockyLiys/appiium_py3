# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: obtain_test_data.py
@time: 2019/06/10 9:03
"""
'''从Excel获取测试用例相关数据'''
import xlrd
from utils.log import logger,LOG

@logger('获取测试用例所需要的参数')
def obtain_test_data(file_path, index=1):
    try:
        file = xlrd.open_workbook(file_path)
        me = file.sheets()[index]
        nrows = me.nrows
        listdata = []
        for i in range(1, nrows):
            dict_canshu = {
                'id': me.cell(i, 0).value,
                'model': me.cell(i, 0).value,
                'logout': (me.cell(i, 2).value)
            }
            dict_canshu.update(eval(me.cell(i,3).value))
            dict_canshu.update(eval(me.cell(i,4).value))
            listdata.append(dict_canshu)
        return listdata
    except Exception as e:
        LOG.info('获取测试用例参数失败！失败原因：%s'%e)
        return e