import allure
from  TestDatas.dg_06_yhcz_mnks_shieldClassHomeSchedule import shieldClassHomeSchedule


class Test_shieldClassHomeSchedule:


    @allure.story("盾构课堂用户操作 - 获取盾构课堂首页用户进度信息")
    @allure.description("盾构课堂用户操作 - 获取盾构课堂首页用户进度信息  接口返回 data分别为试卷总题数,试卷总完成数,视频总数,观看视频总数")
    def test_shieldClassHomeSchedule(self,login_fixture1):
        '''
        盾构课堂用户操作
        获取盾构课堂首页用户进度信息
        :return:s
        '''
        s=login_fixture1
        r1=shieldClassHomeSchedule.shieldClassHomeSchedule1(s)
        print(r1.json())
        assert r1.json()["success"] ==True
        assert r1.json()["msg"] == ""
