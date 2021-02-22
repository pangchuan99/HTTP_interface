from common.url import host  #地址
from TestDatas.dg_04_yhcz_mnks_shieldClassList import shieldClassList

#盾构课堂用户操作 - 模拟考试-获取用户剩下的题
class shieldClassField:

    #盾构课堂用户操作 - 模拟考试-获取用户剩下的题 type字段填写  "carryOn"      carryOn为继续做题,reStart为重新开始
    def shieldClassField1(s):
        '''
        盾构课堂用户操作
       模拟考试-获取用户剩下的题

       这个需要调用到shieldClass_id 他需要从 from TestDatas.dg_02_shieldClassList import shieldClassList  shieldClassList.shieldClassList1(s) 里面获取他的id 进行调用
        '''

        r1=shieldClassList.shieldClassList1(s)
        id=r1.json()["data"][-1]["_id"]

        url= host+"/api/v1/shieldClassField"

        body={
            "shieldClass_id":"{}".format(id),
            "type":"carryOn"
        }

        r=s.get(url,params=body)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r


    #盾构课堂用户操作 - 模拟考试-获取用户剩下的题 type字段填写  "reStart"      carryOn为继续做题,reStart为重新开始
    def shieldClassField2(s):

        '''
        盾构课堂用户操作
       模拟考试-获取用户剩下的题
       这个需要调用到shieldClass_id 他需要从 from TestDatas.dg_02_shieldClassList import shieldClassList  shieldClassList.shieldClassList1(s) 里面获取他的id 进行调用
        '''
        r1=shieldClassList.shieldClassList1(s)
        id=r1.json()["data"][-1]["_id"]

        url= host+"/api/v1/shieldClassField"
        body={
            "shieldClass_id":"{}".format(id),
            "type":"reStart"
        }

        r=s.get(url,params=body)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r
