"""
@author: rocky
@file: test_fun.py
@time: 2019/06/10 10:05
"""

import time
from utils.load_yaml import open_da
from utils.log import  logger,LOG
from  utils.py_app import driver_fengzhuang as feng

"""
 解析测试步骤，按照需求进行测试用例
 默认的定位的最后的一组为断言
"""

@logger('解析测试步骤')
class MakeAppCase(object):

    def __init__(self,driver, path):
        self.driver = driver
        self.path = path

    def open_file(self):
        return open_da(path=self.path)

    def exce_case(self,**kwargs):

        data = self.open_file()['data']
        case_der = feng(driver=self.driver)

        for json_data in data:
            LOG.info(json_data)
            f = case_der.find_elemens(lujing=json_data['element_info'], fangfa=json_data['find_type'])
            if json_data['operate_type'] =='click':
                f[int(json_data['index'])].click()
            elif json_data['operate_type'] =='text':
                f[int(json_data['index'])].text
            elif json_data['operate_type'] =='send_key':
                f[int(json_data['index'])].clear()
                f[int(json_data['index'])].set_value(kwargs.get(json_data['key']))
            else:
                LOG.info('请检查您的测试步骤')
            time.sleep(5)
        f = case_der.find_elemens(lujing=json_data['element_info'], fangfa=json_data['find_type'])

        if json_data['operate_type'] == 'text':
            duanyan = {'code':0,'data':f[int(json_data['index'])].text}
        else:
            duanyan = {'code': 1, 'data':"请检查您的测试步骤最后一步为断言用的"}
            LOG.info('请检查您的测试步骤最后一步为断言用的')
        return duanyan



