
import requests
import allure
from  TestDatas.dg_01_dl import Login_interface

s=requests.session()
#登录接口
class Test_Login_interface:


    @allure.story("正常登录")
    @allure.description("正常登录.登录后进行判断他是否相等")
    def test_login(self):
        '''
        正常登录
        登录后进行判断他是否相等
        :return:
        '''
        r1=Login_interface(s).Login()

        assert r1.json()["success"] ==True
        assert r1.json()['data']['telephone']== 13547324646
        assert r1.json()['data']['name'] == "庞川"
        assert r1.json()["msg"] == "登录成功"
        return r1

    @allure.story("错误登录")
    @allure.description("错误登录.登录后进行判断他是否相等")
    def test_Login_error(self):
        '''

        :return:
        '''
        r1= Login_interface(s).Login_error()

        assert r1.json()["success"] ==False
        assert r1.json()["msg"] =="账号或密码错误"
