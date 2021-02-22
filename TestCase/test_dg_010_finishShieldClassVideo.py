import allure
from  TestDatas.dg_010_finishShieldClassVideo import finishShieldClassVideo
import json


#盾构课堂用户操作 -  视频培训-完成视频
class Test_finishShieldClassVideo:

    @allure.story("盾构课堂用户操作 -  视频培训-完成视频")
    @allure.description("盾构课堂用户操作 -  视频培训-完成视频")
    def test_finishShieldClassVideo(self,login_fixture1):

        '''
        :return:s
        '''

        s=login_fixture1
        r1=finishShieldClassVideo.finishShieldClassVideo1(s)
        print(r1.json())
        # a1=(json.dumps(r1.json(),indent=4,ensure_ascii=False))
        # print(a1)

        assert r1.json()["success"] ==True
        assert r1.json()["msg"] == "观看成功"

