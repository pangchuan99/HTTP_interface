import pytest
import requests
import json
from TestDatas.dg_01_dl import Login_interface

# sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "D:\PYcharm\python16")))



@pytest.fixture(scope="session")
def login_fixture1():
    '''登录 前置操作'''
    s=requests.session()
    Login_interface(s).Login_fixture0()
    yield s
    print("后置操作")
    # s.close()





