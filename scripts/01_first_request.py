"""第一个 HTTP 请求：GET 请求 + 看响应"""
import requests

resp = requests.get("https://api.github.com", timeout=10)

print("状态码:", resp.status_code)
print("Content-Type:", resp.headers.get("content-type"))
print("响应长度:", len(resp.text))
print("前 200 字符:")
print(resp.text[:200])