# 登录接口测试用例设计

## 一、接口说明

- 路径：`POST /api/login`
- 请求体：`{"account": "4~16位字母数字", "password": "6~20位"}`
- 成功响应：`200 {"code":0,"data":{"token":"..."}}`
- 失败响应：`{"code":1001,"msg":"账号或密码错误"}` / `{"code":1002,"msg":"参数不合法"}`

## 二、用例表

| 编号 | 标题 | 请求数据 | 预期结果 | 优先级 |
|---|---|---|---|---|
| TC-001 | 账号密码均正确 | account=abc123, password=123456 | 200；code=0；token 非空 | P0 |
| TC-002 | 账号不存在 | account=zzz999, password=123456 | code=1001；不返回 token | P1 |
| TC-003 | 密码错误 | account=abc123, password=wrong123 | code=1001；不返回 token | P1 |
| TC-004 | 账号为空 | account="", password=123456 | code=1002；提示不能为空 | P2 |
| TC-005 | 密码为空 | account=abc123, password="" | code=1002；提示不能为空 | P2 |
| TC-006 | 账号 3 位（下边界外） | account=abc, password=123456 | code=1002；长度不合法 | P2 |
| TC-007 | 账号 4 位（下边界） | account=abcd, password=123456 | 200；code=0 | P1 |
| TC-008 | 账号 16 位（上边界） | account=abcdefgh12345678, password=123456 | 200；code=0 | P1 |
| TC-009 | 账号 17 位（上边界外） | account=abcdefgh123456789, password=123456 | code=1002；长度不合法 | P2 |
| TC-010 | 账号含特殊字符 | account=abc@123, password=123456 | code=1002；格式不合法 | P2 |
| TC-011 | 账号含中文 | account=张三abc, password=123456 | code=1002；格式不合法 | P2 |
| TC-012 | 密码 5 位（下边界外） | account=abc123, password=12345 | code=1002；长度不合法 | P2 |
| TC-013 | 密码 21 位（上边界外） | account=abc123, password=123456789012345678901 | code=1002；长度不合法 | P2 |
| TC-014 | SQL 注入串 | account=' OR 1=1 --, password=123456 | code=1001 或 1002；**不登录成功** | P1 |
| TC-015 | XSS 脚本串 | account=abc123, password=<script>alert(1)</script> | code=1001；响应中**不回显**该脚本 | P1 |
| TC-016 | 连续错误 3 次后 | 前 3 次密码错，第 4 次密码对 | 第 4 次返回 code=1003（锁定） | P1 |
| TC-017 | 登录后校验 token | 用 TC-001 的 token 调 /api/user/info | 200；返回用户信息 | P0 |
| TC-018 | 伪造 token | Authorization: Bearer fake123 | 401；不返回业务数据 | P1 |


## 三、设计说明

- **等价类**：账号/密码各划分有效与无效类，每类挑代表值
- **边界值**：长度取下边界、上边界及其两侧（3/4/16/17、5/6/20/21）
- **安全类**：SQL 注入、XSS 尽量不让请求"成功"
- **流程类**：覆盖锁定策略与 token 有效性