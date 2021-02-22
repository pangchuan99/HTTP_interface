import allure
from  TestDatas.dg_011_sjgl_sppx_hieldClassVideoField import shieldClassVideoField
import json


#盾构课堂数据管理 - 视频培训-增加视频

class Test_finishShieldClassVideo:

    @allure.story("盾构课堂数据管理 - 视频培训-增加视频")
    @allure.description("盾构课堂数据管理 - 视频培训-增加视频")
    def test_shieldClassVideoField(self,login_fixture1):

        '''
        盾构课堂数据管理 - 视频培训-增加视频
        :return:s
        '''

        s=login_fixture1
        r1=shieldClassVideoField.shieldClassVideoField1(s)
        print(r1.json())
        a1=(json.dumps(r1.json(),indent=4,ensure_ascii=False))
        print(a1)

        assert r1.json()["success"] ==True
        assert r1.json()["msg"] == ""

