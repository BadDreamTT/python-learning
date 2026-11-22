"""HTTP 客户端封装：统一超时、会话复用、错误处理"""
import logging
import requests

from config import BASE_URL, TIMEOUT

logger = logging.getLogger(__name__)

class ApiClient:
    def __init__(self, base_url: str = BASE_URL, timeout: int = TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()      # 复用连接、自动保持 Cookie

    def get(self, path: str, retries: int = 3,**kwargs) -> requests.Response:
        url = self._url(path)
        logger.debug("GET %s", url)
        last_error = None
        for attempt in range(1,retries+1):
            try:
                logger.debug("GET %s (第%d次)", self._url(path), attempt)
                resp = self.session.get(url, timeout=self.timeout, **kwargs)
                logger.info("GET %s -> %s", url, resp.status_code)
                return resp
            except requests.exceptions.Timeout as exc:
                last_error = exc
                logger.error("GET %s timed out (%ss)", url,self.timeout)
                logger.warning("第 %d 次超时,准备重试", attempt)
            except requests.exceptions.ConnectionError:
                logger.error("GET %s connection failed", url)
                raise
        logger.error("重试 %d 次仍失败", retries)
        raise last_error
    def post(self, path: str, **kwargs) -> requests.Response:
        return self.session.post(self.base_url + path, timeout=self.timeout, **kwargs)

    def _url(self, path: str) -> str:
        if not path.startswith("/"):
            path = "/" + path
        return self.base_url + path
    def close(self) -> None:
        """关闭会话,释放连接池"""
        self.session.close()

if __name__ == "__main__":
    # 模块自测：直接运行本文件时执行，被 import 时不执行
    client = ApiClient()
    resp = client.get("/get")
    assert resp.status_code == 200, resp.status_code
    print("self test passed, status =", resp.status_code)