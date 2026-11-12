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