# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: Parmeris.py
@time: 2019/06/10 9:03
"""
'''uittest的再次封装'''

import unittest

class Parmer(unittest.TestCase):

    def __init__(self, methodName='runTest', parme=None):
        super(Parmer, self).__init__(methodName)
        self.parme = parme

    def parametrize(testcase_klass, param=None):
        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(testcase_klass(methodName=name, parm=param))
        return suite