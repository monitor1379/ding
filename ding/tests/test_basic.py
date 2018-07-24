# encoding: utf-8
"""
@author: monitor1379
@contact: yy4f5da2@hotmail.com

@version: 1.0
@file: test_basic.py
@time: 18-7-24 下午9:01

这一行开始写关于本文件的说明与解释
"""

from ding import GroupRobot, App, Dingtalk


def run():
    # test_group_robot()
    test_app()


def test_group_robot():
    with open('../../experiments/robot_access_token', 'r') as fp:
        robot_access_token = fp.read().strip()
    robot = GroupRobot(robot_access_token=robot_access_token)
    robot.send_text('Hello World')


def test_app():
    with open('../../experiments/corp_id', 'r') as fp:
        corp_id = fp.read().strip()

    with open('../../experiments/corp_secret', 'r') as fp:
        corp_secret = fp.read().strip()

    agent_id = 184751749
    userid_list = 'manager9478'

    access_token = Dingtalk.get_corp_access_token(corp_id=corp_id, corp_secret=corp_secret)
    app = App(agent_id=agent_id)
    app.send_text(access_token=access_token, userid_list=userid_list, text='DedSec')


if __name__ == '__main__':
    run()
