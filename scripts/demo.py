"""演示用法"""

from api_client import ApiClient


def main() -> None:
    client = ApiClient()

    resp = client.get("/get", params={"q": "hello"})
    print("GET:", resp.status_code, resp.json()["args"])     # GET: 200 {'q': 'hello'}

    resp = client.post("/post", json={"user": "demo"})
    print("POST:", resp.status_code, resp.json()["json"])    # POST: 200 {'user': 'demo'}


if __name__ == "__main__":
    main()