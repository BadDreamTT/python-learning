import requests

Base_URL = 'http://httpbin.org/'


#--------用例:每条返回(通过/不通过,说明)---------
def case_post_json_ok():
    """用例1:POST JSON应原样回显"""
    resp = requests.post(f"{Base_URL}/post",json={"user":"abc123"},timeout=10)
    assert resp.status_code == 200
    assert resp.json()["json"] == {"user":"abc123"}
    return "POST /post 回显正确"

def case_post_empty_body():
    """空请求体也应有响应"""
    resp = requests.post(f"{Base_URL}/post", json={}, timeout=10)
    assert resp.status_code == 200
    assert resp.json()["json"] == {}
    return "空JSON处理正确"

def case_status_404():
    """错误状态码是否如实返回"""
    resp = requests.get(f"{Base_URL}/status", timeout=10)
    assert resp.status_code == 404
    assert "JSON" not in resp.headers.get("Content-Type")
    return "404 状态码正确"

def case_timeout():
    """ 超时用例：依赖 httpbin 的 3 秒延迟。
    注意：曾出现"未超时即返回"的偶发情况（代理/连接复用导致），
    属不稳定用例，W7 将改为本地 socket 构造以保证可复现。
    """
    try:
        requests.get(f"{Base_URL}/delay/3", timeout=1)
    except requests.exceptions.Timeout:
        return "超时被捕获正确"
    raise AssertionError("应超时但没有")

def case_bad_host():
    """域名不存在时抛异常连接"""
    try:
        requests.get("https://nonexistent.invalid/x", timeout=5)
    except requests.exceptions.ConnectionError:
        return "连接异常被正确捕获"
    raise AssertionError("应该抛ConnectionError")

#---------执行器----------
def run_all():
    cases = [
        ("TC-001", "POST JSON 回显", case_post_json_ok),
        ("TC-002", "POST 空请求体", case_post_empty_body),
        ("TC-003", "404 状态码", case_status_404),
        ("TC-004", "超时异常", case_timeout),
        ("TC-005", "域名不存在", case_bad_host),
    ]
    passed, failed = 0, 0
    for case_id, title, func in cases:
        try:
            msg = func()
            print(f"√ {case_id} {title}---{msg}")
            passed = passed + 1
        except AssertionError as exc:
            print(f"❌ {case_id} {title}---{exc}")
            failed = failed + 1
        except Exception as exc:
            print(f"boom {case_id} {title}---异常:{type(exc).__name__}:{exc}")
            failed = failed + 1
    print(f"\n合计 {passed+failed}条:通过{passed},失败{failed}")

if __name__ == "__main__":
    run_all()