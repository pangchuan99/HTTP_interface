
import requests
import allure
from  TestDatas.dg_03_sjgl_mnks_shieldClassFieldAll import shieldClassFieldAll


class Test_shieldClassFieldAll:


    @allure.story("盾构课堂用户操作 - 模拟考试-获取题目列表")
    @allure.description("正盾构课堂用户操作 - 模拟考试-获取题目列表")
    def test_shieldClassFieldAll(self,login_fixture1):
        '''
         盾构课堂用户操作
        模拟考试-获取题目列表
        :return:s
        '''
        s=login_fixture1
        r1=shieldClassFieldAll.shieldClassFieldAll1(s)
        print(r1.json())
        assert r1.json()["success"] ==True
