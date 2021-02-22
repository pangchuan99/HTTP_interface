from common.url import host  #地址
from TestDatas.dg_07_yhcz_mnks_shieldClassField import shieldClassField
#盾构课堂用户操作 - 模拟考试-下一题


class shieldClassFieldSubmit:

    #盾构课堂用户操作 - 模拟考试-获取用户剩下的题
    def shieldClassFieldSubmit1(s):
        '''
        盾构课堂用户操作
       模拟考试-获取用户剩下的题
       首先你得需要调用到 from TestDatas.dg_05_shieldClassField import shieldClassField          r1=shieldClassField.shieldClassField2(s) 里面获取他的data里面的 id 进行调用
       然后调用的了from TestDatas.dg_05_shieldClassField import shieldClassField这个文件 ，这个文件又去调用了  from TestDatas.dg_02_shieldClassList import shieldClassList文件
       意思就是  需要（盾构课堂用户操作 - 模拟考试-获取题目列表   这个shieldClass_id ），在然后（盾构课堂用户操作 - 模拟考试-获取用户剩下的题  获取上一个shieldClass_id  进行查看data里面的id ），
        '''

        r1=shieldClassField.shieldClassField2(s)
        id=r1.json()["data"]["data"][-1]["_id"]

        url= host+"/api/v1/shieldClassFieldSubmit"
        body={
            "topic_id":"{}".format(id),
            "answer":["A","B","C"]
        }

        r=s.post(url,data=body)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r



