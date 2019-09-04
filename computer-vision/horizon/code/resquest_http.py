import sys
import websocket
import json
import urllib.request
import urllib.parse
import _thread as thread
import time
from sign_up import sign

ak = "BYbVOsYWcwQIRk4H0AsKQEDp"
sk = "dT4LCHVfYGcRqOQDhhncWhwLhYuDf7rK"
http_host = "api-aiot.horizon.ai"
ws_host = "xpushservice-aiot.horizon.ai"


def http_get(path,method,params=None):
    path = path
    method = method
    dic = params or {}

    headers = {"host": http_host,"Content-Type":"application/json"}
    authorization = sign(ak, sk, method, path, dic, headers)
    # authorization = "horizon-auth-v1/BYbVOsYWcwQIRk4H0AsKQEDp/1566359821/f9b99e5e4517e4cb202f18a16e41a0e2211f50c23c2f5852be5cd59a6dc36253"

    headers["authorization"] = authorization
    headers["Method"] = method
    # url = "http://" + http_host + path
    # url = "http://" + http_host + path + '?%s'%params

    params = urllib.parse.urlencode(dic)
    url = "http://" + http_host + path + '?%s' % params
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).read()
    # print("respone: ", response)
    return response


def http_post(path,method,body=None):
    path = path
    method = method
    dic = body or {}
    data = json.dumps(dic)
    headers = {"host": http_host,"Content-Type":"application/json"}
    authorization = sign(ak, sk, method, path, None ,headers)
    headers["authorization"] = authorization
    headers["Method"] = method
    url = "http://" + http_host + path
    data = bytes(data,'utf-8')
    request = urllib.request.Request(url,headers=headers,method=method)
    response = urllib.request.urlopen(request,data).read()
    # print("respone: ", response)
    response = response.decode('utf-8')
    return response


def http_put(path,method,body=None):
    path = path
    method = method
    dic = body or {}
    data = json.dumps(dic)
    headers = {"host": http_host,"Content-Type":"application/json"}
    authorization = sign(ak, sk, method, path, None ,headers)
    # print(authorization)
    headers["authorization"] = authorization
    headers["Method"] = method
    url = "http://" + http_host + path
    data = bytes(data, 'utf8')
    request = urllib.request.Request(url,headers=headers,method=method)
    response = urllib.request.urlopen(request,data).read()
    # print("respone: ", response)
    return response


def http_delete(path, method):
    path = path
    method = method
    headers = {"host": http_host,"Content-Type":"application/json"}
    authorization = sign(ak, sk, method, path, None ,headers)
    headers["authorization"] = authorization
    headers["Method"] = method
    url = "http://" + http_host + path
    request = urllib.request.Request(url,headers=headers,method=method)
    response = urllib.request.urlopen(request).read()
    # print("respone: ", response)
    return response


def ws_sample(client_id):
        method = "GET"
        path = "/ws"
        sign_headers = {"host": ws_host}
        authorization = sign(ak, sk, method, path, None, sign_headers)
        headers = {"hobot_xpush_client_id": client_id,
                   "authorization": authorization}
        print("ws://"+ws_host+path)
        ws = websocket.WebSocketApp("ws://"+ws_host+path,header=headers,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
        ws.on_open = ws_on_open
        ws.run_forever()


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def ws_on_open(ws):
    def run(*args):
        for i in range(30000):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())



if __name__ == '__main__':
    ws_sample("cig123")
    # http_post('/openapi/v1/device_spaces', 'POST', {"name": "test3","description": "测试1","extra": "描述信息"})
    # http_get('/openapi/v1/device_spaces', 'GET')
    # http_put('/openapi/v1/device_spaces/747e1a255d0dcf8e2e2a2a74_XnKqMUDb', 'PUT', {"name": "test3", "description": "测试2", "extra": "描述信息"})
    # http_delete('/openapi/v1/device_spaces/747e1a255d0dcf8e2e2a2a74_XnKqMUDb', 'DELETE')