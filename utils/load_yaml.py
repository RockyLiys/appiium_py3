# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: load_yaml.py
@time: 2019/06/10 9:03
"""
import yaml
from  utils.log import LOG,logger

@logger('解析yaml文件')
def open_da(path):
    try:
        with open('{}'.format(path),'r',encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return {'code':0,'data':data}
    except Exception as e:
        LOG.info('yaml文档解析失败！原因：{}'.format(e))
        return {'code':1,'data':e}