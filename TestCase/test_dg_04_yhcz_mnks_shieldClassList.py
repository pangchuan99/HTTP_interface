
import requests
import allure
from  TestDatas.dg_04_yhcz_mnks_shieldClassList import shieldClassList


class Test_shieldClassList:


    @allure.story("盾构课堂用户操作 - 模拟考试-获取题目列表")
    @allure.description("正盾构课堂用户操作 - 模拟考试-获取题目列表")
    def test_shieldClassList(self,login_fixture1):
        '''
         盾构课堂用户操作
        模拟考试-获取题目列表
        :return:s
        '''
        s=login_fixture1
        r1=shieldClassList.shieldClassList1(s)
        print(r1.json())
        print(r1.json()['data'][-1])
        print(r1.json()['data'][-1]['_id'])
        print(r1.json()['data'][-1]['name'])
        assert r1.json()["success"] ==True
        # assert r1.json()['data'][0]['_id']== "5fb09ebdb912222db0837bf5"
        # assert r1.json()['data'][0]['name'] =="盾构基础类"
        # assert r1.json()["msg"] == ""
