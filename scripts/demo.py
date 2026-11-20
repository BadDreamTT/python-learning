"""演示用法"""
import logging
import requests

from api_client import ApiClient

def set_logging() -> None:
    """日志配置:只在入口调用一次"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

#---------------------用例---------------------

def case_get_ok(client: ApiClient) -> None:
    resp = client.get("/get",params={"q":"hello"})
    assert resp.status_code == 200,f"状态码异常:{resp.status_code}"
    assert resp.json()["args"] == {"q":"hello"},resp.json()["args"]
    print("用例1通过:GET/get")

def case_post_json(client: ApiClient) -> None:
    """POST JSON :服务器收到的是json字段,不是form."""
    resp = client.post("/post",json={"user":"demo","pwd":"123"})
    assert resp.status_code == 200,resp.status_code
    body = resp.json()
    assert body["json"] == {"user":"demo","pwd":"123"}
    assert "application/json" in body["headers"]["Content-Type"]
    print("用例2通过:POST/post(JSON)")

def case_get_404(client: ApiClient) -> None:
    """错误状态码:接口返回404,request 不会抛异常,需要我们断言"""
    resp = client.get("/status/404")
    assert resp.status_code == 404,resp.status_code
    print("用例3通过:404状态码")

def case_timeout(client: ApiClient) -> None:
    """超时场景:故意用1秒超时去请求3秒接口,必须抛timeout"""
    slow_client = ApiClient(timeout=1)
    try:
        slow_client.get("/delay/3")
    except requests.exceptions.Timeout:
        print("用例4通过:超时被正确捕获")
    else:
        raise AssertionError("预期超时,但没发生")
    finally:
        slow_client.close()

#--------------------入口------------------------
def main():
    set_logging()
    client = ApiClient()

    try:
        case_get_ok(client)
        case_post_json(client)
        case_get_404(client)
        case_timeout(client)
    finally:
        client.close()
    print("\n 所有用例通过")


if __name__ == "__main__":
    main()