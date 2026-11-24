# Bandit 笔记

> OverTheWire Bandit 通关记录：每关写清「目标 / 命令 / 密码 / 学到什么」。

## Level 0 → 1
- **目标**：登录后找到密码文件
- **命令**：`cat readme`
- **密码**：`6y2kwnWK6grgwvpvlaa2T1cpFEKOhNR`
- **学到**：`cat` 用于查看文件内容

## Level 1 → 2
- **目标**：读取 `-` 开头的文件
- **命令**：`cat ./-`
- **密码**：`PK8fYLzg2hnHSz83plBL1iEpKDd3QTob`
- **学到**：文件名以 `-` 开头会被当成命令选项，用 `./` 让它被识别为路径

## Level 2 → 3
- **目标**：文件名带空格
- **命令**：`cat "spaces in this filename"`
- **密码**：`7ZzZ2LfrykP2zEyvB14m3c1c17tGYJPME`
- **学到**：文件名带空格时，用引号包起来，或用 `\ ` 转义

## Level 3 → 4
- **目标**：找隐藏目录里的文件
- **命令**：`ls -a` 找到 `inhere`，再 `cd inhere && ls -a`
- **密码**：`xzTXq1rDJQVVazdv5cHq1TQyTtwufAMq`
- **学到**：`ls -a` 显示以 `.` 开头的隐藏文件

## Level 4 → 5
- **目标**：目录里只有一个文件是人类可读的
- **命令**：`file ./*` 找出唯一 ASCII text，再 `cat ./-file07`
- **密码**：`6C7h9GD8M6a15nr7wo1RonzFjJ9ylrG`
- **学到**：`file` 可以判断文件类型；`cat` 到二进制文件会刷屏，用 `reset` 或 Ctrl+C` 恢复

## Level 5 → 6
- **目标**：按「大小 / 是否可执行」筛选出目标文件
- **命令**：`find . -type f -size 1033c ! -executable -exec cat {} \;`
- **密码**：`pxA26xhMWaC2SvDotA4r9EgZkulo6SBW`
- **学到**：`find` 的 `-type` / `-size` / `! -executable` 可以组合过滤；注意 `file` 不支持这些参数，筛选要用 `find`

- ## Level 6 → 7
- **目标**：按「user/group/ size」筛选出目标文件
- **命令**：`find / -user bandit7 -group bandit6 -size 33c 2>/dev/null;`
- **密码**：`Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3`
- **学到**：`find` 可以组合过滤；注意 `file` 不支持这些参数，筛选要用 `find`对于`2>dev/null`linux有三个默认流
- 0:标准输出stdin(键盘输入);1:标准输出stdout(正常结果).2:标准错误stderr(报错信息).`/dev/null`相当于linux的黑洞
- 写进的数据直接丢掉不保存不显示.所以整体就是把错误流>(定向)黑洞

- ## Level 7 → 8
- **目标**：找出存在某个固定单词旁的密码.
- **命令**：`grep millionth data.txt;`
- **密码**：`VR1ljMayciFxbnUokuQmJFw6QC9VKtub`
- **学到**：`grep`全局正则打印,在文本中找到关键词的行.去找关键词打印出来就行

- ## Level 8 → 9
- **目标**：密码存于data.txt并且是只出现一次的文本行
- **命令**：`sort data.txt | uniq -c;`
- **密码**：`EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl`
  - **学到**：`uniq`只能判断相邻重复所以必须要先`sort`按字母排序,然后再去识别.其次后面是 
  - `-u`就是打印出唯一出现的一行.
  - `d`只输出重复行
  - `c`统计每一行的重复次数,在前面打印出来+内容
  - `uniq`重复行只保留一份,全部打印出来

- ## Level 9 → 10
- **目标**：密码存在data.txt ,是少数几个人类可读的字符串之一,前面几个===字符.
- **命令**：`strings data.txt | grep === ;`
- **密码**：`B0s2khmbT9u0geKuOoVGW3JZKhndE3BG`
- **学到**：直接`cat`里面都是二进制乱码会崩溃,所以用`strings`提取里面人类可读的字符串.再由`|`管道传给下一个grep去找关键词.

- ## Level 10 → 11
- **目标**：密码所在文件包含base64编码数据.
- **命令**：`base64 -d data.txt;`
- **密码**：`pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro`
- **学到**：将`data.txt`文件解码用`base64 -d`,它会读取文件里的 base64 字符串，输出明文密码
- 更直观的写法应该是`cat data.txt | base64 -d`

## Level 11 → 12

- **目标**：文件内容是 A-Z 字母整体移位 13 位（ROT13），需要还原
- **命令**：`cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
- **密码**：`GROozWP08QyN0mGrjUkIDOWCYkZiQxrN`
- **学到**：
  - `tr` 是**字符逐一替换**：第一个集合的每个字符映射到第二个集合对应位置的字符
  - `'A-Za-z'` 是全部大小写字母，`'N-ZA-M'` 是"从 N 开始绕回"的映射
  - ROT13 移位 13 位，做两次会变回原文（13+13=26），所以加密解密是同一个命令

## Level 12 → 13

- **目标**：`data.txt` 被反复压缩了几十层，需要一层层解开
- **命令**：
  1. 先手动还原第一层二进制：`xxd -r data.txt > data.bin && mv data.bin data.txt`
  2. 再用循环自动解剩下的层：`while true; do ... case ... esac; done`
- **密码**：`qQYqihO8P8RzR6iqxYqX45quvihF2uzk`
- **学到**：

  **① 判断当前是哪一层**

  | 手段 | 用法 | 说明 |
  |---|---|---|
  | `file -b 文件` | `file -b data.txt` | 靠**文件头魔数**判断类型 |
  | 魔数 | `1f 8b`=gzip，`42 5a 68`=bzip2，`50 4b 03 04`=zip，`fd 37 7a 58 5a`=xz，`ustar`=tar | `xxd data.txt \| head -1` 就能看到 |

  **② 解压时统一输出到屏幕（配合 `>` 就不用反复改名）**

  | 类型 | 命令 |
  |---|---|
  | gzip | `gunzip -c f > next` |
  | bzip2 | `bunzip2 -c f > next` |
  | xz | `xz -dc f > next` |
  | zip | `unzip -p f > next` |
  | tar | `tar -xOf f > next` |
  | hexdump | `xxd -r f > next` |

  **③ 两个容易搞混的点**
  - `gunzip`/`bunzip2`/`unxz` 名字自带"解压"，只需 `-c`；`xz`/`gzip`/`bzip2` **默认压缩**，要 `-d` 才是解压
  - `tar` 的 `-c` 是 **create（创建归档）**，不是输出到屏幕；输出到屏幕是 `-O`（大写）

  **④ 为什么 `ASCII text` 不等于"到底了"**
  - hexdump 和 base64 的内容**本身就是 ASCII 文本**，`file` 会把它们识别成 `ASCII text`
  - 所以判断顺序应该是：先看内容特征（`^[0-9a-f]{8}:` 像 hexdump），再看 `file` 的压缩格式，最后才是"没有匹配 = 到底了"

- **顺带学到的命令**（不是这关核心）
  - `mkdir -p 目录`：`-p`（parent）父目录不存在时一起创建，且目录已存在不报错
  - `cp 源 目标`：`cp ~/data.txt .` 表示从家目录拷贝到当前目录（`.` = 当前目录）
  - `mktemp -d`：创建随机名的临时目录，返回完整路径

- ## Level 13 → 14
- **目标**：手上有一个叫 sshkey.private 的私钥，用它登录到下一个账号 bandit14.
- **命令**：
  1.  `cat sshkey.private`然后复制里面的所有信息
  2.   先到本地虚拟机上创建一个文件将所有东西粘贴进去然后.`chmod 600 sshkey.private`
  3.   然后用密钥登录.`ssh -i 密钥所在文件 用户名@主机 -p 端口`
  4.   最后`cat /etc/bandit_pass/bandit14`得到密码
- **密码**：`aaWecNkG4FhxJQxz07uiwzVP6bJiYS65`
- **学到**：服务器存公钥（authorized_keys），本地存私钥
- 登录时服务器发挑战，客户端用私钥签名回应
- 私钥从不离开本机 → 泄露私钥 = 身份被盗
- ② 为什么必须 chmod 600
- SSH 会主动检查：私钥若 group/other 可读，直接拒用并报 Permissions 0644 ... are too open
- 逻辑：别人能读 = 别人能复制 = 别人能冒充你

- ## Level 14 → 15
- **目标**：将当前关卡密码给localhost 30000获取下一层秘密.
- **命令**：`echo "这里粘贴你bandit14的密码" | nc localhost 30000;`
- **密码**：`pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7`
- **学到**：`nc`称之为网络瑞士军刀,作用就是建立 TCP 连接，往端口发文本.

## Level 15 → 16

- **目标**：把 bandit15 的密码发给本机 30001 端口，服务返回下一关密码
- **命令**：
  ```bash
  ssh bandit15@bandit.labs.overthewire.org -p 2220
  openssl s_client -connect localhost:30001
  # 连上后输入 bandit15 的密码，回车
  ```
- **密码**：`kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V`
- **学到**：

  **① 为什么 `nc` 不行**
  - 这个端口要求 **TLS 加密**连接，`nc` 发的是明文，直接被服务端拒绝/断开
  - 对比 14→15 那关的 30000 端口：**同样的操作，但一个要加密、一个不用**

  **② `openssl s_client` 是什么**
  - 一个**手动的 TLS 客户端**：连上后先做完整 TLS 握手，再让你像普通键盘一样发数据
  - 常用参数：
    | 参数 | 作用 |
    |---|---|
    | `-connect host:port` | 连接目标 |
    | `-servername 域名` | SNI，告诉服务器要哪个证书（HTTPS 用） |
    | `-quiet` | 减少握手日志的刷屏 |

  **③ 连接时你会看到什么**
  ```
  CONNECTED(00000003)
  ---
  Certificate chain
   i:...                      ← 服务器证书（自签的，所以会提示 verify error）
  ---
  SSL handshake has read ... bytes
  New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
  ```
  - 出现 `verify error: self signed certificate` **不用管**，这是自签证书，只影响身份验证、不影响加密
  - `Cipher is ...` 就是双方协商出来的加密算法

  **④ 判断"这关需要什么协议"**
  - 连不上 / 一进去就被断开 → 试 `openssl s_client`
  - `nc` 能连但没反应 → 可能要发特定格式
  - 这题的经验：**端口号不同，要求的协议可能不同**，安全题里很常见
## Level 16 → 17

- **目标**：题目提示 31000~32000 端口里有一个能直接给出密码，需要先找到它
- **命令**：
  ```bash
  # 1. 扫端口，找出 open 的
  nmap -p 31000-32000 localhost

  # 2. 对每个 open 的端口尝试 TLS 连接
  openssl s_client -connect localhost:<端口> -quiet
  # 连上后输入 bandit16 的密码，回车
  ```
- **密码**：`pWXMAZoxGC8JmDMfmT5MGEsobMM3vnj2`
- **学到**：

  **① `nmap` 的基本用法**

  | 参数 | 作用 |
  |---|---|
  | `-p 31000-32000` | 指定端口范围（`-p 80,443` 指定单个；`-p-` 全端口） |
  | `localhost` | 目标主机（这关是扫本机） |

  输出里 `open` 的才是能连的，`closed` / `filtered` 都试不了。

  **② 为什么要逐个试**

  - 扫出来可能是**好几个 open 端口**，但只有一个是"直接吐密码"的
  - 其他端口会要求你先发送当前密码做认证，或者干脆返回别的内容
  - 判断依据：连上后**输出里有 `bandit17` 的密码**就是它

  **③ `-quiet` 的好处**

  - 不加 `-quiet` 会打印一大堆握手日志（证书链、Session 等），把真正的输出淹没
  - 加了之后只显示服务端返回的内容，更适合"逮密码"

  **④ 端口扫描在安全里的位置**

  - 信息收集的第一步：**先知道目标开了哪些端口、跑什么服务**
  - 真实场景还要加 `-sV`（服务版本识别）、`-sC`（默认脚本）、`-T4`（提速）
  - ⚠️ 只在自己有权限的目标上扫——对公网主机扫端口可能违法

- **踩坑记录**：
  - `nmap` 没装 → `sudo apt install nmap`（Bandit 服务器已装好）
  - 用 `nc` 连 open 端口没反应 → 因为是 TLS 服务，必须用 `openssl s_client`
  - 试了 3~4 个端口才找到 → 正常，这关就是这么设计的

## Level 17 → 18

- **目标**：两个密码文件，只有一行不同，找出新文件里那一行
- **命令**：
  ```bash
  ssh bandit17@bandit.labs.overthewire.org -p 2220
  diff passwords.old passwords.new
  ```
- **密码**：`OQxXZjELndr90zuhOTDYBEomI0SZITXI`
- **学到**：

  **① `diff` 的输出怎么读**
  ```
  42c42
  < 旧文件这一行的内容
  ---
  > 新文件这一行的内容
  ```
  - `42c42` = 第 42 行有 change（旧第 42 行 → 新第 42 行）
  - `<` 表示**只存在于第一个文件**
  - `>` 表示**只存在于第二个文件** ← 这关要的就是它

  **② 其他"找差异"的写法**（都能解这题）
  ```bash
  # 只看新文件独有的行
  comm -13 passwords.old passwords.new     # 需要先排序

  # 反向过滤：去掉旧文件里出现过的行
  grep -vxF -f passwords.old passwords.new
  ```

  **③ 常见参数**
  | 参数 | 作用 |
  |---|---|
  | `diff -u a b` | 统一格式（unified diff，git 用的就是这种） |
  | `diff -y a b` | 左右并排显示 |
  | `diff -q a b` | 只说明"是否不同" |

  **④ 实际用途**
  - 比较两次配置文件改动（排查"谁改坏了"）
  - 对比两次接口响应（测试中验证变化）
  - `diff -u` 就是 Git 展示改动的基础格式

- **踩坑记录**：
  - 一开始看 `diff` 输出有点懵，因为默认会展示 `<` 和 `>` 两行；这关只需要 `>` 那一行

## Level 18 → 19

- **目标**：密码在 `readme` 文件里，但 `.bashrc` 被改成登录即退出，正常 SSH 进不去
- **命令**：
  ```bash
  ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
  ```
- **密码**：`KpsOfPkcP7i1FlIExk2QEjyt6dw8dxZI`
- **学到**：

  **① SSH 不只能开 shell，还能直接执行命令**

  ```bash
  ssh 用户@主机 命令            # 执行一条就断开
  ssh 用户@主机 "命令1 && 命令2"  # 多条用引号包起来
  ```

  **② 为什么这关这样能过**

  ```
  正常登录：连接 → 执行 .bashrc（被改成 exit）→ 立刻断开
  执行命令：连接 → 直接跑 "cat readme" → 不进入交互 shell → .bashrc 的影响被绕过
  ```

  非交互式执行**不会加载完整登录环境**，所以坏掉的启动脚本不起作用。

  **③ 实际用途**
  - 批量运维：`ssh host "df -h"`
  - 自动化脚本里远程执行
  - **服务器 shell 配置坏了时的救命手段**
  - 面试可答："SSH 除了登录还能做远程命令执行、端口转发（-L/-R）、传文件（scp/sftp）"

- **踩坑记录**：
  - 直接 `ssh bandit18@...` 登录 → 立刻断开，看起来像"密码错了"或"服务器拒绝"，实际是 `.bashrc` 在退出
  - 判断依据：出现 `Bye bye!` 之类提示 + 连接建立成功，说明是配置问题不是网络问题

## Level 19 → 20

- **目标**：`/etc/bandit_pass/bandit20` 只有 bandit20 能读，你是 bandit19，需要"借身份"读取
- **命令**：
  ```bash
  ssh bandit19@bandit.labs.overthewire.org -p 2220

  ls -l                                  # 找到 -rwsr-xr-x、属主 bandit20 的 bandit20-do
  ./bandit20-do                          # 先看它自己的用法提示（会给出示例 whoami）
  ./bandit20-do whoami                   # 验证身份切换：应输出 bandit20
  ./bandit20-do cat /etc/bandit_pass/bandit20   # 代读密码
  ```
- **密码**：`4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA`
- **学到**：

  **① SUID 是什么**
  ```
  -rwsr-xr-x  bandit20  bandit19  bandit20-do
    ↑             ↑          ↑
    s=SUID      文件属主    文件属组
  ```
  - 任何人执行这个程序时，进程的**有效用户 ID（euid）会临时变成文件属主**
  - 所以 `./bandit20-do cat xxx` 里的 `cat` 是**以 bandit20 身份**跑的
  - 这也是 Linux **提权的经典入口**（安全方向的必修内容）

  **② "代跑工具"的模式**
  ```
  ./bandit20-do <任意命令>
  ```
  - 它不关心你给什么命令，只是"用我的身份帮你执行"
  - 先跑 `./bandit20-do whoami` 验证身份，再跑真正要执行的命令——**先验证再使用**是好习惯

  **③ 必须写 `./` 的原因**
  - 当前目录不在 `PATH` 里，直接敲 `bandit20-do`

## Level 20 → 21

- **目标**：SUID 程序 `suconnect` 会连接指定端口，收到数据后把 `bandit21` 的密码发回；需要自己开监听端口，并用 bandit20 的密码"喂"给它
- **命令**：
  ```bash
  # 终端 A：监听 1234 端口，有客户端连上就发出 bandit20 的密码
  ssh bandit20@bandit.labs.overthewire.org -p 2220
  echo "bandit20的密码" | nc -l -p 1234

  # 终端 B：运行 SUID 程序，让它连接 A 的端口
  ssh bandit20@bandit.labs.overthewire.org -p 2220
  ./suconnect 1234
  ```
- **密码**：`bW9kBv5WC3P4yoDyf12LSdGuNz5ka6hY`
- **学到**：

  **① TCP 通信的两个角色**
  ```
  服务端：nc -l -p 1234        ← 监听（listen），等着别人来连
  客户端：./suconnect 1234      ← 主动连接（connect）
  ```
  - `nc` 不带 `-l` 是**客户端**（连别人），带 `-l` 是**服务端**（等别人）
  - `ss -tlnp` 里的 `l` 就是 listening，和这里的 `-l` 是同一个概念

  **② `nc` 参数**
  | 参数 | 含义 |
  |---|---|
  | `-l` | listen，监听模式 |
  | `-p 端口` | 指定端口（部分版本可省略 `-p`，写成 `nc -l 1234`） |

  **③ 端口怎么选**
  - **1~1023** 是特权端口，绑定需要 root
  - **1024~65535** 普通端口，1234 / 5555 / 8888 随便挑
  - 被占用会报 `Address already in use`，换一个；可用 `ss -tlnp | grep 端口` 检查

  **④ 管道把"数据"接到"网络"**
  ```bash
  echo "密码" | nc -l -p 1234
  #    ①          ②
  # ① 把密码写到标准输入
  # ② nc 把标准输入的内容，发送给连上来的客户端
  ```

  **⑤ SUID 在这里的作用**
  - `suconnect` 属主是 `bandit21`，带 `s` 位（`-rwsr-xr-x`）
  - 所以它能以 bandit21 的身份完成"验证密码 → 返回下一关密码"
  - 思路与 19→20 一致：**程序代你执行**

- **踩坑记录**：
  - 只开一个终端 → 无法同时"监听"和"连接"，**必须两个终端**
  - `nc -l -p 1234` 执行后光标卡住不动 → 这是**正常阻塞**（在等连接），不是卡死
  - 密码里的特殊字符没加引号 → 被 shell 解释；`echo "密码"` 一律加双引号
  - 忘了先启动监听就运行 `suconnect` → 报 `Connection refused`（对方端口没人听）

## Level 21 → 22

- **目标**：有一个 cron 定时任务以 bandit22 身份运行脚本，把 bandit22 的密码写到了 `/tmp` 下的文件，需要找到并读取它
- **命令**：
  ```bash
  ssh bandit21@bandit.labs.overthewire.org -p 2220

  ls /etc/cron.d/                       # 1. 看有哪些定时任务
  cat /etc/cron.d/cronjob_bandit22      # 2. 看这关的任务配置
  cat /usr/bin/cronjob_bandit22.sh      # 3. 看它执行的脚本内容
  cat /tmp/<脚本里那个文件名>            # 4. 直接读密码
  ```
- **密码**：`（填你拿到的 bandit22 密码）`
- **学到**：

  **① cron 配置的一行怎么读**
  ```
  * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
  ┬┬┬┬┬ ────┬─── ─────────────┬────────────
  │││││     │                 └─ 执行什么
  │││││     └─ 以谁的身份执行  ← 提权的关键
  ││││└─ 星期（0-7）
  │││└─ 月
  ││└─ 日
  │└─ 小时
  └─ 分钟
  ```
  - `* * * * *` = **每分钟**执行一次
  - 第 6 个字段是**执行身份**，这决定脚本"有多大权限"

  **② 脚本里的两行就是漏洞**
  ```bash
  chmod 644 /tmp/t7AZ2mTkttoSU2...            # 把文件设为所有人可读
  cat /etc/bandit_pass/bandit22 > /tmp/t7AZ2...  # 以 bandit22 身份读密码并复制出去
  ```
  - 脚本以 **bandit22** 运行 → 有权限读密码
  - 但把结果写到了 **`/tmp`（公共目录）** 且 `chmod 644` → **任何人可读**

  **③ 提权排查的标准动作**
  ```bash
  ls /etc/cron.d/                 # 系统级定时任务
  cat /etc/crontab                # 全局 crontab
  crontab -l                      # 当前用户的定时任务
  # 找到脚本后看两件事：谁在执行（身份）、我能不能改它（权限）
  ```
  > 如果某个**以 root/high-privilege 运行的脚本你能修改**，你就能让它执行任意命令 —— 这是 Linux 提权的经典手法。

  **④ `/tmp` 为什么危险**
  - 所有用户都能读写 → 敏感数据写这里等于公开
  - 且容易被其它用户抢先创建同名文件（符号链接攻击）

- **踩坑记录**：
  - `cat /tmp/xxx` 提示 No such file → cron **每分钟才跑一次**，等 1 分钟再读；或检查文件名有没有抄错（很长一串随机字符）
  - 一开始不知道从哪下手 → 记住入口永远是 `ls /etc/cron.d/`
  - 误以为要自己写脚本 → 这关是**读别人写的脚本**，找它留下的痕迹