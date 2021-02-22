from common.url import host  #地址
from TestDatas.dg_04_yhcz_mnks_shieldClassList import shieldClassList
from TestDatas.dg_012_shieldClassVideoList import shieldClassVideoList

#盾构课堂用户操作 - 视频培训-获取视频

class shieldClassVideoField:

    #盾构课堂用户操作 - 视频培训-获取视频

    def shieldClassVideoField1(s):
        '''
        盾构课堂用户操作 -
         视频培训-获取题目列表
        :return:
        '''

        # r1=shieldClassList.shieldClassList1(s)
        r1=shieldClassVideoField.shieldClassVideoField1(s)
        print(r1.json())
        id=r1.json()["data"][0]["_id"]
        url= host+"/api/v1/shieldClassVideoField"
        body = {
            "shieldClass_id": "{}".format(id)
        }
        r=s.get(url,params=body)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r



