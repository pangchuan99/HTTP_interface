import json
import os
import time
from threading import Timer, Event, Thread
import websocket


class HeartbeatThread(Thread):
    """心跳"""

    def __init__(self, event, ws):
        super(HeartbeatThread, self).__init__()
        self.event = event
        self.ws = ws

    def run(self):
        while 1:
            self.event.wait(timeout=2)


def on_message(ws, message):
    """接收信息"""
    try:
        print("正在获取token")
        print(message)
        if "token" in message:
            message=message.replace("\\","")
            msg_list=message.split(",")
            file=open("../data/token.ini","w",encoding="utf8")
            print(msg_list[13][8::])
            file.write(msg_list[13][8::].replace('"',''))
            print("token获取成功")
            file.close()
            os._exit(0)
    except:
        pass



def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    """请求连接"""
    ws.send("5probe")

def data(userName):
    content = {
        "code": "user.login",
        "body": {
            "userName": userName,
            "password": "278a97d3b74b6ff8da2c66d33842c210"
        },
            "token": "",
        "timestamp": time.time(),
        "sign": "aDlPwGnEeYR0uLGOMsfjWBbmeum_MjZ2",
        "nonestr": "8f88c6a0-99f4-42f9-ae99-c40e4d7efeeb",
        "extra": "null"
    }
    return content


def on_emit(ws):
    # 创建心跳线程
    event = Event()
    heartbeat = HeartbeatThread(event, ws)
    heartbeat.start()
    data = {
        "code": "item.select",
        "body": {
            "isPaging": 1,
            "page": 1
        },
        "timestamp": 1595813452,
        "nonestr": "696247",
        "token": "f2784009e0514b82996f019215344fdf"
    }
    content={"code": "user.login","body": {"userName": "18780887831","password": "278a97d3b74b6ff8da2c66d33842c210"},"token": "","timestamp": time.time(),"sign": "aDlPwGnEeYR0uLGOMsfjWBbmeum_MjZ2","nonestr": "8f88c6a0-99f4-42f9-ae99-c40e4d7efeeb","extra": "null"}
    while 1:
        # ws.send('42[\"request\",\"{0}\"]'.format(data))
        ws.send('42[\"request\","{0}"]'.format(content))
        time.sleep(2)

hosts="wss://gsm.jdjinsui.com/wss/?EIO=3&transport=websocket"
if __name__ == '__main__':
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        url=hosts,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    t = Timer(3, on_emit, args=(ws,))
    t.start()
    ws.run_forever()





