import allure
from  TestDatas.dg_013_shieldClassVideoField import shieldClassVideoField
import json


#盾构课堂用户操作 - 视频培训-获取视频

class Test_shieldClassVideoField:

    @allure.story("盾构课堂用户操作 - 视频培训-获取视频")
    @allure.description("盾构课堂用户操作 - 视频培训-获取视频")
    def test_shieldClassVideoField(self,login_fixture1):

        '''
        :return:s
        '''

        s=login_fixture1
        r1=shieldClassVideoField.shieldClassVideoField1(s)
        print(r1.json())
        print(r1.json()["data"][-1]["topic_id"])
        a1=(json.dumps(r1.json(),indent=4,ensure_ascii=False))
        print(a1)

        assert r1.json()["success"] ==True
        assert r1.json()["msg"] == ""

