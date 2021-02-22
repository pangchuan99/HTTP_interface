
import pytest
import requests
import json
from common.url import host  #地址


#盾构课堂用户操作 - 模拟考试-获取题目列表
class shieldClassList:

    def shieldClassList1(s):
        '''
        盾构课堂用户操作
        模拟考试-获取题目列表
        '''
        url= host+"/api/v1/shieldClassList"
        r=s.get(url)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        # print(a1)
        return r

