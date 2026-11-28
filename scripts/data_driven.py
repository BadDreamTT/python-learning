import requests

BASE_URL = 'http://httpbin.org/'

CASES =[
 # (用例编号, 路径, 期望状态码, 说明)
    ("TC-001", "/status/200", 200, "正常返回"),
    ("TC-002", "/status/404", 404, "资源不存在"),
    ("TC-003", "/status/500", 500, "服务器错误"),
    ("TC-004", "/status/301", 301, "重定向"),
    ("TC-005", "/get", 200, "GET 正常"),
    ("TC-006", "/status/418", 418, "我是茶壶（彩蛋状态码）"),
    ("TC-007", "/status/204", 204, "无内容"),
    ("TC-008", "/status/503", 503, "服务不可用"),
]

def test_status(path:str,expect:int):
    """一个通用用例,验证状态码"""
    resp = requests.get(BASE_URL+path,timeout=10, allow_redirects=False)
    assert resp.status_code == expect,f"期望{expect},实际{resp.status_code}"

def run_all():
    passed = failed = 0
    for case_id,path,expect,desc in CASES:
        try:
            test_status(path,expect)
            print(f"✔{case_id} {path} {expect} {desc}")
            passed = passed + 1
        except AssertionError as es:
            print(f"❌{case_id} {desc}{path}->{expect}")
            failed = failed + 1
    print(f"\n合计 {passed +failed}条:通过{passed}失败{failed}")

if __name__ == "__main__":
    run_all()
