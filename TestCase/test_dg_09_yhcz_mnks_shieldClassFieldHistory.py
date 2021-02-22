import allure
from  TestDatas.dg_09_yhcz_mnks_shieldClassFieldHistory import shieldClassFieldHistory

import json
#盾构课堂用户操作 - 模拟考试-获取历史记录
class Test_shieldClassFieldHistory:


    @allure.story("盾构课堂用户操作 - 模拟考试-获取历史记录")
    @allure.description("盾构课堂用户操作 - 模拟考试-获取历史记录s")
    def test_shieldClassFieldHistory(self,login_fixture1):
        '''
        盾构课堂用户操作
        获取盾构课堂首页用户进度信息
        :return:s
        '''
        s=login_fixture1
        r1=shieldClassFieldHistory.shieldClassFieldHistory1(s)
        print(r1.json())

        a1=(json.dumps(r1.json(),indent=4,ensure_ascii=False))
        print(a1)
        assert r1.json()["success"] ==True
        assert r1.json()["msg"] == ""

