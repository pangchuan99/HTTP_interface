
import pytest
import requests
import json
from common.url import host  #地址
from TestDatas.dg_04_yhcz_mnks_shieldClassList import shieldClassList

#盾构课堂数据管理 - 模拟考试-获取所有题目

class shieldClassFieldAll:

    def shieldClassFieldAll1(s):
        '''
        盾构课堂数据管理 -
         模拟考试-获取所有题目

        '''
        r1=shieldClassList.shieldClassList1(s)
        id= r1.json()['data'][-1]["_id"]
        # print("我是03获取的ID{}".format(id))
        url= host+"/api/v1/shieldClassFieldAll"
        body={
            "shieldClass_id":id

        }
        r=s.get(url,params=body)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r

