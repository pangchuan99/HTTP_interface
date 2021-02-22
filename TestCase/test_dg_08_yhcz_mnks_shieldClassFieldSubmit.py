import allure
from  TestDatas.dg_08_yhcz_mnks_shieldClassFieldSubmit import shieldClassFieldSubmit

#盾构课堂用户操作 - 模拟考试-获取用户剩下的题
class Test_shieldClassFieldSubmit:


    @allure.story("盾构课堂用户操作 -  模拟考试-获取用户剩下的题")
    @allure.description("盾构课堂用户操作 -  模拟考试-获取用户剩下的题")
    def test_shieldClassFieldSubmit(self,login_fixture1):

        '''
        盾构课堂用户操作
       模拟考试-获取用户剩下的题
       首先你得需要调用到 from TestDatas.dg_05_shieldClassField import shieldClassField          r1=shieldClassField.shieldClassField2(s) 里面获取他的data里面的 id 进行调用
       然后调用的了from TestDatas.dg_05_shieldClassField import shieldClassField这个文件 ，这个文件又去调用了  from TestDatas.dg_02_shieldClassList import shieldClassList文件
       意思就是  需要（盾构课堂用户操作 - 模拟考试-获取题目列表   这个shieldClass_id ），在然后（盾构课堂用户操作 - 模拟考试-获取用户剩下的题  获取上一个shieldClass_id  进行查看data里面的id
       获取到这个data里面的ID后 在dg_07_shieldClassFieldSubmit进行调用 ），
        :return:s
        '''

        s=login_fixture1
        r1=shieldClassFieldSubmit.shieldClassFieldSubmit1(s)
        print(r1.json())
        assert r1.json()["success"] ==True
        assert r1.json()["msg"] == "哈哈哈你个傻叉做错了"

