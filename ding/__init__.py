# encoding: utf-8
"""
@author: monitor1379
@contact: yy4f5da2@hotmail.com

@version: 1.0
@file: __init__.py.py
@time: 18-7-24 下午8:26

这一行开始写关于本文件的说明与解释
"""


import logging

def setup_ding_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    logger.propagate = False

    # 控制台logger：默认level=INFO
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    fmt = '[%(asctime)s] [PID:%(process)d] [%(filename)s:#%(lineno)d] [%(levelname)s]: %(message)s'
    formatter = logging.Formatter(fmt)
    console.setFormatter(formatter)
    logger.addHandler(console)
    return logger

setup_ding_logger()



from .basic import GroupRobot, Dingtalk, App


