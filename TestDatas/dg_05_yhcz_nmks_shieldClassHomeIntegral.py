from common.url import host  #地址


#盾构课堂用户操作 - 获取所有人的积分情况

class shieldClassHomeIntegral:

    def shieldClassHomeIntegral1(s):
        '''
        盾构课堂用户操作
        获取所有人的积分情况
        '''
        url= host+"/api/v1/shieldClassHomeIntegral"
        r=s.get(url)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r

