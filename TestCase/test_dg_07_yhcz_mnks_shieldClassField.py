import allure
from  TestDatas.dg_07_yhcz_mnks_shieldClassField import shieldClassField
import json
#盾构课堂用户操作 - 模拟考试-获取用户剩下的题
class Test_shieldClassHomeSchedule:


    @allure.story("盾构课堂用户操作 - 获取盾构课堂首页用户进度信息---carryOn为继续做题")
    @allure.description("盾构课堂用户操作 - 获取盾构课堂首页用户进度信息---carryOn为继续做题")
    def test_shieldClassHomeSchedule1(self,login_fixture1):
        '''
        盾构课堂用户操作
        获取盾构课堂首页用户进度信息
        :return:s
        '''
        s=login_fixture1
        r1=shieldClassField.shieldClassField1(s)
        print(r1.json())
        assert r1.json()["success"] ==True
        assert r1.json()["msg"] == ""



    @allure.story("盾构课堂用户操作 - 获取盾构课堂首页用户进度信息---reStart为重新开始")
    @allure.description("盾构课堂用户操作 - 获取盾构课堂首页用户进度信息---reStart为重新开始")
    def test_shieldClassHomeSchedule2(self,login_fixture1):
        '''
        盾构课堂用户操作
        获取盾构课堂首页用户进度信息
        :return:s
        '''

        s=login_fixture1
        r1=shieldClassField.shieldClassField2(s)
        # a1=(json.dumps(r1.json(),indent=4,ensure_ascii=False))
        # print(a1)
        print(r1.json())
        assert r1.json()["success"] ==True
        assert r1.json()["msg"] == ""
