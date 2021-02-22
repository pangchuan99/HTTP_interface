from common.url import host  #地址


#盾构课堂用户操作 - 获取盾构课堂首页用户进度信息


class shieldClassHomeSchedule:

    def shieldClassHomeSchedule1(s):
        '''
        盾构课堂用户操作
        获取盾构课堂首页用户进度信息

        '''
        url= host+"/api/v1/shieldClassHomeSchedule"
        r=s.get(url)
        # a1 = (json.dumps(r.json(), indent=4, ensure_ascii=False))
        # print(r.json())
        return r

