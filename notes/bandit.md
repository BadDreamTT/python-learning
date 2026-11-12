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
