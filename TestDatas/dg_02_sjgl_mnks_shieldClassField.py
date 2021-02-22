
import pytest
import requests
import json
from common.url import host  #地址


#盾构课堂数据管理 - 模拟考试-编辑试卷
class shieldClassField:
    def shieldClassField1(s):
        '''
       盾构课堂数据管理 -
       模拟考试-编辑试卷----进行添加
        '''
        url = host + "/api/v1/shieldClassField"
        body = {
            # "shieldClass_id":"5fb09ebdb912222db0837bf5",
            "type": "exam",
            "name": "庞川添加的题库",
            "description": "我添加的题库我最帅",
            "data":
                [
                    {

                        "topic": "我是单选",
                        "options": [
                            {
                                "key": "A",
                                "value": "正确"
                            },
                            {
                                "key": "B",
                                "value": "错误"
                            }
                        ],
                        "result": [
                            "A"
                        ],
                        "reason": "我是详情"
                    }
                ]
        }
        he = {"content-type": "application/json"}

        r = s.post(url, json=body, headers=he)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r


    def shieldClassField2(s,id):
        '''
       盾构课堂数据管理 -
       模拟考试-编辑试卷---进行修改
        '''
        url = host + "/api/v1/shieldClassField"
        body = {
            "shieldClass_id": id,
            "type": "exam",
            "name": "庞川修改的试卷",
            "description": "庞川修改的试卷简介",
            "data":
                [
                    {

                        "topic": "我是单选我是单选答案",
                        "options": [
                            {
                                "key": "A",
                                "value": "正确"
                            },
                            {
                                "key": "B",
                                "value": "错误"
                            }
                        ],
                        "result": [
                            "A"
                        ],
                        "reason": "我是详情"
                    }
                ]
        }
        he = {"content-type": "application/json"}
        r = s.post(url, json=body, headers=he)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r



