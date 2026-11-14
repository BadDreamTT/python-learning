# HTTP 笔记

> 记录 HTTP 原理、抓包分析和疑问。参考：小林 coding 图解网络。

## 1. 基本概念
- HTTP 是应用层协议，基于 TCP，默认端口 80（HTTPS 443）
- 一次请求的结构：请求行 + 请求头 + 空行 + 请求体

## 2. 请求方法与状态码

| 方法 | 用途 | 幂等 |
|---|---|---|
| GET | 获取资源 | ✅ |
| POST | 提交数据 | ❌ |
| PUT | 更新资源 | ✅ |
| DELETE | 删除资源 | ✅ |

| 状态码段 | 含义 |
|---|---|
| 2xx | 成功 |
| 3xx | 重定向 |
| 4xx | 客户端错误（401 未认证、403 无权限、404 找不到） |
| 5xx | 服务端错误 |

## 3. Cookie 与 Session
- Cookie：存在浏览器，每次请求自动带上
- Session：存在服务端，靠 Cookie 里的 sessionId 关联
- 登录流程：POST 登录 → 服务端 `Set-Cookie` → 后续请求带 `Cookie`

## 4. 抓包实战：GitHub 登录

**抓包步骤**：Chrome `F12` → Network → 勾上 `Preserve log` → 输入账号密码点 Sign in → 在列表里找 `POST` 请求。

**1）定位到的请求**

| 项 | 值 |
|---|---|
| 方法 | `POST` |
| URL | `https://github.com/session` |
| 状态码 | `302`（登录成功后重定向） |
| 类型 | `document`（表单提交，整页跳转） |

**2）请求体（Payload）的关键字段**

| 字段 | 含义 |
|---|---|
| `login` | 账号 |
| `password` | 密码（明文放在请求体里，靠 HTTPS 加密链路保护） |
| `authenticity_token` | CSRF 防护令牌，防止跨站伪造提交 |

**3）响应头关键字段**

| 字段 | 含义 |
|---|---|
| `Set-Cookie: user_session=***` | 登录态凭证，服务端下发给浏览器 |
| `Location: /` | 302 跳转的目标地址（登录成功回首页） |

**4）观察与结论**

- 登录用 **POST + 302 跳转**，不是 200 —— 这叫 **PRG 模式**（Post-Redirect-Get）：提交完马上跳转，避免用户刷新时重复提交表单；
- 密码放在**请求体**里（不是 URL），所以不会出现在浏览器历史、代理日志里；真正的保护来自 **HTTPS 加密链路**；
- 登录成功后浏览器会自动保存 Cookie，**后续每个请求都会带上** `Cookie: user_session=***`，服务端靠它识别"已登录"；
- 因此 **Cookie 泄露 ≈ 账号被盗**，所以抓包记录里绝不能贴真实 Cookie 值。

**5）顺带学到的**

- `ping` / `collect` 类型的 204 请求是埋点统计，测试时直接过滤；
- 有验证码的站点（如极验），登录前会先发 `gt`（验证码初始化）、`powGetP` 等请求，**验证通过后**才发真正的登录 POST。

## 5. 用 Python 复现请求

```python
import requests

resp = requests.get("https://api.github.com", timeout=10)
print(resp.status_code)
print(resp.headers["content-type"])