# encoding: utf-8
"""
@author: rocky
@software: PyCharm
@file: subprocess_popen.py
@time: 2019/06/10 9:03
"""

import subprocess
def subprocess_popen(cmd):
    return subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).stdout.readlines()