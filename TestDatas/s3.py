import websocket
import time
import re

import json
try:
    import thread
except ImportError:
    import _thread as thread
import time


url = "wss://gsm.jdjinsui.com/wss/?EIO=3&transport=websocket"

#是用来接受消息的，server发送的所有消息都可以用on_message这个方法来收取。
def on_message(ws, message):
    '''

    :param ws:
    :param message:
    :return:
    '''
    print("####### on_message #######")
    print(ws)
    print(message)
    '''
    :param ws:
    :param message: 接收返回的值
    :return: r1
    '''
    print("我是来接受消息的{}".format(message))
    #
    message1=message.replace("\\","")
    msg_list = message1.split("'")
    # print("我是分割的结果",type(msg_list))
    # print("我是进行分割好后的结果{}".format(msg_list))
    # print("我是获取列表值",msg_list[0][320:352])
    #
    # print("我是获取列表值",msg_list[0][15:-2])
    # print("打印下他的类型",type(msg_list[0][15:-2]))

    r1=(json.loads(msg_list[0][15:-2]))


    print(type(r1))
    print(r1)
    print(r1["body"]["token"])
    print(message)
#这个方法是用来处理错误异常的，如果一旦socket的程序出现了通信的问题，就可以被这个方法捕捉到。
def on_error(ws, error):
    print("####### on_error #######")
    print(ws)
    print(error)


#主要就是关闭socket连接的。

def on_close(ws):
    print("####### on_close #######")
    print(ws)
    print("####### closed #######")


content = {
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
data = {
    "code": "item.select",
    "body": {
        "isPaging": 1,
        "page": 1
    },
    "timestamp": 1595813452,
    "nonestr": "8f88c6a0-99f4-42f9-ae99-c40e4d7efeeb",
    "token": "16c3c366e87f654cdbde5e95721a8f9e"
}
#方法是用来保持连接的，上面这样的一个例子，就是保持连接的一个过程，每隔一段时间就会来做一件事,他会在30s内一直发送hello。最后停止
def on_open(ws):
    print("####### on_open #######")
    def run(*args):
        for i in range(1):
            time.sleep(1)
            ws.send('42["request","{}"]'.format(content))
        time.sleep(1)
        ws.close()
        print("thread terminating...")


    thread.start_new_thread(run, ())


if __name__ == '__main__':
    ws = websocket.WebSocketApp(url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    # ws.run_forever(http_proxy_host="172.16.102.71", http_proxy_port=4229)
    ws.run_forever()

"""
####### on_open #######
####### on_message #######
<websocket._app.WebSocketApp object at 0x7f8ffe73eb38>
Hello 0
####### on_message #######
<websocket._app.WebSocketApp object at 0x7f8ffe73eb38>
Hello 1
####### on_message #######
<websocket._app.WebSocketApp object at 0x7f8ffe73eb38>
Hello 2
####### on_close #######
<websocket._app.WebSocketApp object at 0x7f8ffe73eb38>
thread terminating...
####### closed #######
"""