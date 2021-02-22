from common.url import host  #地址
from TestDatas.dg_04_yhcz_mnks_shieldClassList import shieldClassList

#盾构课堂用户操作 - 模拟考试-获取历史记录
class shieldClassFieldHistory:

    #盾构课堂用户操作 - 模拟考试-获取历史记录
    def shieldClassFieldHistory1(s):
        '''
        盾构课堂用户操作
       模拟考试-获取历史记录
       这个需要调用到shieldClass_id 他需要从 from TestDatas.dg_02_shieldClassList import shieldClassList  shieldClassList.shieldClassList1(s) 里面获取他的id 进行调用
        '''

        r1=shieldClassList.shieldClassList1(s)
        id=r1.json()["data"][-1]["_id"]

        url= host+"/api/v1/shieldClassFieldHistory"
        body={
            "shieldClass_id":"{}".format(id)
        }
        r=s.get(url,params=body)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r
