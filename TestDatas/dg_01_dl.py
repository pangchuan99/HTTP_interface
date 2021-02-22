
import pytest
import requests
import json
from common.url import host  #地址



#登录接口
class Login_interface:

    def __init__(self,s):
        self.s = s

    def Login(self):
        '''
        正确登录账号
        :return: 返回所有
        '''

        url= host+"/api/v1/session"
        body={
            "telephone":"13547324646",
            "type":"password",
            "code":"e10adc3949ba59abbe56e057f20f883e"
        }

        r=self.s.post(url,data=body)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        print(r.json())
        # s.headers.update(r)

        return r


    def Login_error(self):
        '''
        错误登录
        :return: 返回所有
        '''
        url= host+"/api/v1/session"
        body={
            "telephone":"13547324646",
            "type":"password",
            "code":"e10adc3949ba59abbe56e057f20f8831"
        }

        r=self.s.post(url,data=body)
        return r

    def Login_fixture0(self):
        '''
        登录之后进行把token  放在headers里面 在conftest.py文件 设置为前置操作(session)
        :return: 返回所有
        '''

        url = host + "/api/v1/session"
        body = {
            "telephone": "13547324646",
            "type": "password",
            "code": "e10adc3949ba59abbe56e057f20f883e"
        }
        r = self.s.post(url, data=body)
        token = r.json()["data"]["token"]

        h = {
            "Content - Type": "application / x - www - form - urlencoded",
            "Authorization": "Bearer {}".format(token)
        }
        self.s.headers.update(h)
        return self.s


if __name__ == '__main__':
    s=requests.session()
    r1=Login_interface(s)
    print(r1)
    r2=r1.Login_fixture0()
    print(r2)


    # print(r2.json()["data"]["name"])
    # r3=r1.Login_error()
    # print(r3)
    # print(type(r3))
    # print(r3.json())
