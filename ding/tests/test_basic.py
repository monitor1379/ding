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

    msg = {
        "msgtype": "action_card",
        "action_card": {
            "title": "是透出到会话列表和通知的文案",
            "markdown": "支持markdown格式的正文内容",
            "btn_orientation": "0",
            "btn_json_list": [
                {
                    "title": "一个按钮",
                    "action_url": "https://www.taobao.com"
                },
                {
                    "title": "两个按钮",
                    "action_url": "https://www.tmall.com"
                }
            ]
        }
    }

    msg = {
        "msgtype": "action_card",
        "action_card": {
            "title": "是透出到会话列表和通知的文案",
            "markdown": "支持markdown格式的正文内容",
            "single_title": "查看详情",
            "single_url": "https://open.dingtalk.com"
        }
    }

    msg = {
        "msgtype": "oa",
        "oa": {
            "head": {
                "bgcolor": "FFBBBBBB",
                "text": "头部标题"
            },
            "body": {
                "title": "正文标题",
                "form": [
                    {
                        "key": "姓名:",
                        "value": "张三"
                    },
                    {
                        "key": "年龄:",
                        "value": "20"
                    },
                    {
                        "key": "身高:",
                        "value": "1.8米"
                    },
                    {
                        "key": "体重:",
                        "value": "130斤"
                    },
                    {
                        "key": "学历:",
                        "value": "本科"
                    },
                    {
                        "key": "爱好:",
                        "value": "打球、听音乐"
                    }
                ],
                "rich": {
                    "num": "15.6",
                    "unit": "元"
                },
                "content": "大段文本大段文本大段文本大段文本大段文本大段文本大段文本大段文本大段文本大段文本大段文本大段文本",
                "image": "@lADOADmaWMzazQKA",
                "file_count": "3",
                "author": "张三"
            }
        }
    }
    app.send(access_token, userid_list, msg=msg)


if __name__ == '__main__':
    run()
