import websocket
import json
import time


def send(url, data):
    '''websocket建立连接接收消息'''
    ws = websocket.create_connection(url)              # 创建连接
    ws.send(json.loads(data))   # json转化为字符串，必须转化
    results = []
    while True:
        receive = ws.recv()    # 服务器响应数据
        results.append(json.loads(receive))

    ws.close()
    return results

if __name__ == '__main__':
    url = "wss://gsm.jdjinsui.com/wss/?EIO=3&transport=websocket"
    data = {
        "code": "user.login",
        "body": {
            "userName": "13547324646",
            "password": "278a97d3b74b6ff8da2c66d33842c210"
        },
        "token": "",
        "timestamp": time.time(),
        "sign": "aDlPwGnEeYR0uLGOMsfjWBbmeum_MjZ2",
        "nonestr": "8f88c6a0-99f4-42f9-ae99-c40e4d7efeeb",
        "extra": "null"
    }
    send(url, data)
