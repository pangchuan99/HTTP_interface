from common.url import host  #地址
from requests_toolbelt import MultipartEncoder  #这个是用来上传下载用的
from TestDatas.dg_04_yhcz_mnks_shieldClassList import shieldClassList


#盾构课堂数据管理 - 视频培训-增加视频

class shieldClassVideoField:

    #盾构课堂数据管理 - 视频培训-增加视频

    def shieldClassVideoField1(s):
        '''
        盾构课堂数据管理 -
        视频培训-增加视频

        :return:
        '''
        r1 = shieldClassList.shieldClassList1(s)
        print(r1.json())
        id = r1.json()["data"][0]["_id"]
        print(id)
        url= host+"/api/v1/shieldClassVideoField"
        M=MultipartEncoder(
            fields=[
            ("shieldClass_id",id),
            ("topic","万老板添加视频"),
            ("video",("m1.mp4",open("D:\PYcharm\pyjk\common\m1.mp4","rb"),"mp4"))
            ]
        )
        r=s.put(url,data=M,headers={"content-Type":M.content_type})
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r



