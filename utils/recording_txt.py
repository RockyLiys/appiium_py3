# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: recording_txt.py
@time: 2019/06/10 9:03
"""
'''采集的性能测试数据存放在txt文档中'''
import  os
import  time
from utils.log import LOG, logger
from config.config import base_dir

now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
recording=os.path.join(base_dir, 'reports/{}-xing.txt'.format(now))
@logger('记录当前的cpu占有率，内存')
def write_recording(cpu, neicun, devices):
    try:
        with open(recording,'a',encoding='utf-8') as f:
            m='%s：cpu:%s,内存：%s'%(devices,cpu,neicun)
            f.write(m+'\n')
            f.close()
    except Exception as e:
        LOG.info('写入性能数据失败！失败原因：%s'%e)