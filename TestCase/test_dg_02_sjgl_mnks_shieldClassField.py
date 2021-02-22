

import allure
from  TestDatas.dg_02_sjgl_mnks_shieldClassField import shieldClassField
from  TestDatas.dg_04_yhcz_mnks_shieldClassList import shieldClassList

#盾构课堂数据管理 - 模拟考试-编辑试卷

class Test_shieldClassField:


    @allure.story("盾构课堂数据管理 - 模拟考试-编辑试卷")
    @allure.description("盾构课堂数据管理 - 模拟考试-编辑试卷")
    def test_shieldClassField1(self,login_fixture1):
        '''
         盾构课堂用户操作
        模拟考试-获取题目列表
        shieldClassField2是进行添加
        :return:s
        '''
        s=login_fixture1
        r1=shieldClassField.shieldClassField1(s)
        print(r1.json())

        assert r1.json()["success"] ==True
        assert r1.json()["msg"] == ""
        #然后验证是否添加成功，查询
        r2=shieldClassList.shieldClassList1(s)
        print(r2.json())
        # assert r1.json()['data'][-1]['_id'] ==""
        assert r2.json()['data'][-1]['name'] == "庞川添加的题库"
        assert r2.json()['data'][-1]['description'] == "我添加的题库我最帅"





    @allure.story("盾构课堂用户操作 - 模拟考试-获取题目列表")
    @allure.description("正盾构课堂用户操作 - 模拟考试-获取题目列表")
    def test_shieldClassField2(self,login_fixture1):
        '''
         盾构课堂用户操作
        模拟考试-获取题目列表
        shieldClassField2是进行修改

        :return:s
        '''
        s = login_fixture1
        #操作步骤1. 进行查询获取到 添加的最后一个
        r1=shieldClassList.shieldClassList1(s)
        print(r1.json())
        id= r1.json()['data'][-1]["_id"]
        #操作步骤2  进行修改
        r2=shieldClassField.shieldClassField2(s,id)
        print(r2.json())
        assert r2.json()["success"] ==True
        assert r2.json()["msg"] == ""

        #操作步骤2  查询验证
        r3= shieldClassList.shieldClassList1(s)
        print(r3.json())
        assert r3.json()['data'][-1]["name"]=="庞川修改的试卷"
        assert r3.json()['data'][-1]["description"] == "庞川修改的试卷简介"

