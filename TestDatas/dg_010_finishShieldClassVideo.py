from common.url import host  #地址
from TestDatas.dg_013_shieldClassVideoField import shieldClassVideoField

#盾构课堂用户操作 - 视频培训-完成视频

class finishShieldClassVideo:

    #盾构课堂用户操作 -  视频培训-完成视频
    def finishShieldClassVideo1(s):
        '''
        盾构课堂用户操作 -
        视频培训-完成视频
        :return:
        '''
        r1=shieldClassVideoField.shieldClassVideoField1(s)
        id=(r1.json()["data"][-1]["topic_id"])
        print(id)

        url= host+"/api/v1/finishShieldClassVideo"
        body = {
            "topic_id": "{}".format(id)
        }
        r=s.post(url,data=body)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r



