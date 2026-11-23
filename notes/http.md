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
```

##HTTP 与 TLS

**对称加密**：加密和解密用同一把密钥（如 AES）。速度快、强度高，
难点在于"密钥怎么安全地交给对方"——如果密钥在网络上明文传输，等于没有加密。

**非对称加密**：一对密钥，公钥加密、私钥解密（也可私钥签名、公钥验签）。
公钥可以公开，私钥必须自己保管。速度慢，所以只用来"协商密钥"，不用于传大量数据。

**HTTPS 的做法**：
1. 先通过非对称加密（或密钥交换算法）安全地协商出一把"对称密钥"；
2. 之后全程用对称加密传输数据（又快又安全）。

**为什么光有加密还不够（中间人攻击）**：
如果服务端只是把自己的公钥发过来，中间人可以劫持并替换成**自己的公钥**。
浏览器用假公钥加密的密钥，中间人用自己的私钥就能解开 → 拿到对称密钥 → 之后全程解密。

**证书的作用**：
证书由 CA（证书颁发机构）用自己的私钥对"域名 + 公钥 + 有效期"签名。
浏览器内置了各大 CA 的公钥，收到证书后验签：
- 签名对不上 → 证书是伪造的，警告；
- 域名不匹配 → 证明不了这个公钥属于该网站，警告。
这样中间人既不能伪造签名，也不能把别人的证书拿来冒充自己。

**一句话**：非对称加密解决"密钥分发"，对称加密解决"传输性能"，证书解决"我怎么确定对面是谁"。

---

## HTTPS 与 TLS

> 一句话：**HTTPS = HTTP + TLS**。HTTP 负责"说什么"，TLS 负责"别人听不懂、也改不了"。

### 1. HTTP 与 HTTPS 的区别

| 项目 | HTTP | HTTPS |
|---|---|---|
| 端口 | 80 | 443 |
| 传输内容 | 明文 | TLS 加密后的密文 |
| 能否被窃听/篡改 | 能 | 不能（没有会话密钥解不开） |
| 身份验证 | 无 | 证书验证"对面是谁" |
| 抓包 | 直接看到请求 | 只能看到密文（除非有密钥） |

### 2. 两把钥匙：对称 vs 非对称

| | 对称加密 | 非对称加密 |
|---|---|---|
| 密钥 | 加密解密同一把 | 公钥加密、私钥解密 |
| 速度 | 快（AES） | 慢（RSA/ECDHE） |
| 难题/特点 | **密钥怎么安全地交给对方** | 公钥可公开，私钥自己留着 |
| 在 HTTPS 中的角色 | **传数据** | **协商密钥 + 身份验证** |

**HTTPS 的经典思路**：用非对称（或 ECDHE）安全地协商出一把对称密钥 → 之后全程用对称密钥加密。

### 3. 为什么还要证书（中间人攻击）

如果服务端只是"把自己的公钥发给你"：

```
你 ←── 公钥 ── 中间人 ←── 真公钥 ── 服务器
      （替换成自己的公钥）
```

中间人用自己的私钥就能解开你发的密钥，之后全程解密。

**证书的作用**：由 CA（证书颁发机构）用**它的私钥**对"域名 + 公钥 + 有效期"签名；浏览器内置 CA 公钥，收到证书后**验签**：

- 签名对不上 → 证书是伪造的
- 域名不匹配 → 无法证明这个公钥属于该网站
- 过期 → 同样拒绝

**所以证书解决的是"你是谁"，加密解决的是"别人看不懂"，两者不能互相替代。**

### 4. TLS 握手

```
客户端                                     服务端
  |  ClientHello（支持的算法 + 随机数）  →
  |                                        |  ServerHello（选定算法 + 随机数）
  |  ←  Certificate（服务器证书，含公钥）  
  |  ←  ServerHelloDone                    |
  |  验证证书（CA 链、域名、有效期）          
  |  交换密钥材料（ECDHE）→                
  |                                        |  双方各自算出相同的"对称密钥"
  |  Finished（用会话密钥加密）→            
  |  ←  Finished                            |
  ============ 之后全部用对称密钥加密 ============
```

**TLS 1.3 的改进**：
- 握手从 2-RTT 降到 **1-RTT**（甚至 0-RTT 恢复）
- 用 **ECDHE** 做密钥交换，支持**前向保密**（私钥将来泄露也解不开历史流量）
- 取消了重协商（这也是"R 键报错"的原因）

### 5. 实测：openssl s_client

工具说明：Windows 上 `openssl` 可能是 PyCharm 自带的老版本（1.1.1h，无 CA 路径），
改用 Git 自带的 3.5.9：

```powershell
& "D:\Git\ucrt64\bin\openssl.exe" s_client `
  -proxy 127.0.0.1:7892 `
  -connect github.com:443 `
  -servername github.com `
  -CAfile "D:\Git\ucrt64\etc\ssl\certs\ca-bundle.crt"
```

| 参数 | 作用 |
|---|---|
| `-connect host:port` | 连接目标 |
| `-servername 域名` | SNI，告诉服务器要哪个站点的证书（一个 IP 上可能有很多网站） |
| `-proxy host:port` | 让 openssl 走 HTTP 代理（openssl 不读系统代理） |
| `-CAfile 路径` | 指定 CA 根证书包，否则报 `Verify return code: 20` |
| `-quiet` | 少打印握手日志 |

**观察到的结果**：

⬜ 成功时：
```
Protocol    : TLSv1.3
Cipher      : TLS_AES_128_GCM_SHA256
subject=CN = github.com
Verify return code: 0 (ok)
```

⬜ 失败时（代理关闭）：
```
BIO_connect: connect error
→ 连 TCP 都没通，还没开始 TLS 握手
```

⬜ 异常现象：证书链的签发者是 **Sectigo**（GitHub 正常应为 DigiCert）
→ 说明代理在**中间人解密**。这就是"MITM"的真实样子。

**在 TLS 通道里发 HTTP 请求**（连接成功后输入，最后空行结束）：

```
HEAD / HTTP/1.1
Host: github.com
User-Agent: curl/8.0

```

⬜ 响应：`HTTP/1.1 301 Moved Permanently` —— 证明 HTTP 跑在 TLS 之上

### 6. 踩坑记录

| 现象 | 原因 | 解决 |
|---|---|---|
| `Verify return code: 20 (unable to get local issuer certificate)` | openssl 找不到 CA 根证书 | 加 `-CAfile` 指向 ca-bundle.crt |
| `BIO_connect: connect error` | 代理没开 / 端口不对 | 确认代理在运行、端口是 7892 |
| 卡在 `CONNECTED` 不动 | openssl 不读系统代理 | 加 `-proxy 127.0.0.1:7892` |
| 敲 `R` 后 `can_renegotiate: wrong ssl version` | `R` 是 s_client 的"重协商"快捷键，TLS1.3 不支持 | 别敲单字母，直接敲 HTTP 请求 |
| `User-Agent: ...` 报"无法识别" | 敲在 PowerShell 里而不是 s_client 里 | 先连上再输请求头 |
| `HTTP/1.1 403 Forbidden` | GitHub 拒绝没有 User-Agent 的请求 | 加 `User-Agent: curl/8.0` |

### 7. 面试问答

**Q：抓包为什么看不到 HTTPS 内容？**
> 因为 TLS 加密，没有会话密钥只能看到密文。DevTools 能看到是因为浏览器持有密钥；Wireshark 要解密需要配置 `SSLKEYLOGFILE`。

**Q：证书能防住什么？**
> 防中间人冒充。中间人可以转发流量，但无法伪造 CA 的签名；伪造证书浏览器会报警。

**Q：为什么 HTTPS 用两种加密？**
> 对称加密快，适合传数据；非对称（ECDHE）能安全协商密钥。组合起来既安全又高效。

**Q：HTTP/2、HTTP/3 和 HTTPS 什么关系？**
> HTTP/2 通常跑在 TLS 上（浏览器强制），HTTP/3 基于 QUIC（UDP + TLS 1.3），都是"协议版本"，加密是 TLS 提供的。


## 缓存与 CDN 实测（2026-11-23）

### 结论一：动态接口不缓存
httpbin.org/get 的响应头只有：
  Content-Type、Content-Length、Date、CORS 相关、X-Content-Type-Options
→ 没有 Cache-Control / ETag / Last-Modified
→ 因为动态数据每次可能不同，缓存会拿到脏数据

### 结论二：静态资源长缓存
bilibili 的 JS（xxx.min.js）响应头：
  Cache-Control: max-age=600      → 10 分钟强缓存
  Age: 250                        → 已在 CDN 缓存 250 秒
                                    剩余有效期 = 600 - 250 = 350 秒
  ETag: 4938e9a7...               → 内容指纹
  Content-Encoding: br            → Brotli 压缩
  Accept-Ranges: bytes            → 支持断点续传

### 结论三：三种缓存表现
  强缓存未过期  → 不发请求，200 + (disk cache)
  强缓存过期且未变 → 304 Not Modified（无响应体）
  内容变化/强制刷新 → 200 重新下载

### 结论四：怎么判断走了代理/CDN
  DevTools → Remote Address: 127.0.0.1:7892  → 说明走了本地代理
  响应头有 Age / X-Cache / Server → 说明前面有 CDN 或反向代理
