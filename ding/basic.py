# encoding: utf-8
"""
@author: monitor1379
@contact: yy4f5da2@hotmail.com

@version: 1.0
@file: basic.py
@time: 18-7-24 下午8:27

钉钉工具类
官方开发者平台：https://open-doc.dingtalk.com/microapp/serverapi2/ye8tup
"""

import json
import logging
from typing import Dict

import requests

logger = logging.getLogger(__name__)

HEADERS = {'Content-Type': 'application/json'}

# 企业内部开发APIs
URL_ROOT = 'https://oapi.dingtalk.com/'
URL_GROUP_ROBOT_SEND_MESSAGE = URL_ROOT + 'robot/send?access_token={access_token}'
URL_CORP_GET_TOKEN = URL_ROOT + 'gettoken?corpid={corp_id}&corpsecret={corp_secret}'
URL_CORP_CONVERSATION_ASYN_SEND_MESSAGE = URL_ROOT + 'topapi/message/corpconversation/asyncsend_v2?access_token={access_token}'


class GroupRobot(object):

    def __init__(self, robot_access_token):
        self.robot_access_token = robot_access_token
        self.url = URL_GROUP_ROBOT_SEND_MESSAGE.format(access_token=robot_access_token)

    def send(self, payload: Dict):
        return requests.post(url=self.url, data=json.dumps(payload), headers=HEADERS)

    def send_text(self, text):
        payload = {'msgtype': 'text', 'text': {'content': text}}
        response = self.send(payload)
        return response


class App(object):

    def __init__(self, agent_id: int):
        self.agent_id = agent_id

    def send(self, url: str, payload: Dict):
        return requests.post(url=url, data=json.dumps(payload), headers=HEADERS)

    def send_text(self, access_token, userid_list, text):
        url = URL_CORP_CONVERSATION_ASYN_SEND_MESSAGE.format(access_token=access_token)
        payload = {
            'agent_id': self.agent_id,
            'userid_list': userid_list,
            'msg': {
                'msgtype': 'text',
                'text': {
                    'content': text
                }
            }
        }
        return self.send(url, payload)


class Dingtalk(object):

    @staticmethod
    def get_corp_access_token(corp_id, corp_secret):
        url = URL_CORP_GET_TOKEN.format(corp_id=corp_id, corp_secret=corp_secret)
        response = requests.get(url)
        data = response.json()
        access_token = data['access_token']
        return access_token
