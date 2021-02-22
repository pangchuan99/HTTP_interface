import allure
from  TestDatas.dg_05_yhcz_nmks_shieldClassHomeIntegral import shieldClassHomeIntegral


class Test_shieldClassHomeIntegral:


    @allure.story("盾构课堂用户操作 - 获取所有人的积分情况")
    @allure.description("盾构课堂用户操作 - 获取所有人的积分情况")
    def test_shieldClassHomeIntegral(self,login_fixture1):
        '''
         盾构课堂用户操作
        获取所有人的积分情况
        :return:s
        '''
        s=login_fixture1
        r1=shieldClassHomeIntegral.shieldClassHomeIntegral1(s)
        print(r1.json())
        assert r1.json()["success"] ==True
        # assert r1.json()['data'][0]['name'] =="庞川"
        assert r1.json()["msg"] == ""
