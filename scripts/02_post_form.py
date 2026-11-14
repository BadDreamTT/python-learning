"""POST 表单提交：观察请求体怎么带数据"""
import requests

url = "https://httpbin.org/post"          # 一个专门回显请求的测试站
data = {"username": "test", "password": "123456"}

#resp = requests.post(url, data=data, timeout=10)
resp = requests.post(url, json=data, timeout=10)     # data → json
print("状态码:", resp.status_code)

# httpbin 会把收到的内容原样返回
body = resp.json()
print("表单数据:", body["form"])
print("Content-Type:", resp.json()["headers"].get("Content-Type"))
print("JSON 数据:", body["json"])