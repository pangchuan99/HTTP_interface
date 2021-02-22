from common.url import host  #地址



#盾构课堂用户操作 -  视频培训-获取题目列表
class shieldClassVideoList:

    #盾构课堂用户操作 -  视频培训-获取题目列表
    def shieldClassVideoList1(s):
        '''
        盾构课堂用户操作 -
        视频培训-获取题目列表
        '''
        url= host+"/api/v1/shieldClassVideoList"

        r=s.get(url)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r



