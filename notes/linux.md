# Linux 常用命令速查

## 文件与目录

- `ls -a`：显示隐藏文件（Bandit Level 3 用过）
- `ls -l`：查看详细信息，输出的第一列是**权限位**，共 10 位

  第一位是文件类型：

  | 符号 | 类型 |
  |---|---|
  | `-` | 普通文件 |
  | `d` | 目录 |
  | `l` | 软链接 |
  | `c` | 字符设备 |
  | `b` | 块设备 |

  后 9 位是权限，每 3 位一组：第 2~4 位属主（u）、第 5~7 位属组（g）、第 8~10 位其他用户（o）；
  每组里的 `rwx` 分别是读、写、执行，`-` 表示无权限。

## 查找与过滤
- `grep -n "关键词" 文件`
eg: `grep -n "关键词" xxxx.txt` -n显示行号,根据关键词在文件中搜索显示匹配行
- `find . -type f -size 1033c ! -executable -exec file {}\;`
- `find` 的条件可以自由组合：`-type`、`-size`、`! -executable` 都能叠加
- `-exec 命令 {} \;`：对每个找到的文件执行命令，`{}` 是文件名占位符，`\;` 是结束标记（要转义，不然被 shell 吃掉）
- 注意：`file` 命令不支持 `-type`/`-size`，筛选必须用 `find`，`file` 只负责判断类型

## 排序去重
- `sort file | uniq -c`
- `sort`将文件内容按照字母顺序重新排序,再有管道传下去,找出唯一的内容.
- `-c`会在内容前标记上行号.-u是直接打印出唯一值.`
- `-d`是打印出全部重复值.
- `uniq`去重打印出全部值
## 权限
- `chmod 755 file`
- `chmod +x hello.sh`这是给加上了执行权限
- r,w,x,-.分别是数字4210.所以755的意思就是主:rwx,组r-x,其他人:r-x
- 还可以改文件所有者要sudo`sudo chown 用户名 hello.sh`需要输入密码
## 进程与端口
- `ps aux | grep python`
- `ps aux | grep 关键字`：找进程，第二列是 PID；注意 grep 自己也会被匹配，加 `| grep -v grep` 过滤
- `ss -tlnp`：看本机监听端口，排查"端口被占 / 服务没起来"
- `kill <PID>`：默认 SIGTERM（优雅退出）；`kill -9 <PID>` 强杀
- `ss -tlnp | grep 端口号`被占用时打印一行
- 假定端口被占就会输出类似于`LISTEN 0  5  0.0.0.0:8000  0.0.0.0:*  users:(("python3",pid=4010,fd=4))`空闲时候是没有任何出输的
- 实际用途：启动服务报 `Address already in use` 时，用 `ss -tlnp | grep 端口` 找 PID 再 kill

### 踩坑：`kill <PID>` 直接敲了
- 报错：`bash: 未预期的记号 "newline" 附近有语法错误`
- 原因：`<` 是 shell 的重定向符，`<PID>` 是占位符，要换成真实数字

## 网络与故障排查

| 命令 | 作用 | 备注 |
|---|---|---|
| `ip a` | 看网卡和 IP | 没有 `inet 192.168.x.x` 说明没拿到地址 |
| `ping -c 3 223.5.5.5` | 测网络通不通 | 用 IP，**不经过 DNS** |
| `ping -c 3 baidu.com` | 测 DNS 是否正常 | 上一个通、这个不通 = DNS 坏了 |
| `cat /etc/resolv.conf` | 看 DNS 服务器 | 正常应有 `nameserver` 一行 |
| `sudo dhclient -r && sudo dhclient` | 重新获取 IP | DHCP 没发地址时用 |
| `sudo nmcli networking off && sudo nmcli networking on` | 重启网络服务 | 改完生效最快的方式 |
| `ss -tlnp \| grep 22` | 看 SSH 服务在不在 | 连不上时先确认服务端在监听 |

**排查顺序（三步定位）**：

1. `ping -c 3 223.5.5.5` → 不通 = **根本没有网络**（网卡/IP/宿主机问题）
2. 通了但 `ping baidu.com` 不通 → **DNS 问题**（改 resolv.conf 或换 223.5.5.5）
3. 都通但 `ssh` 连不上 → **对方服务/端口/防火墙**问题，不是你的网络问题
### 踩坑：Ubuntu 显示"线缆已拔出"
- 现象：网络设置里"有线"显示线缆已拔出，`ssh` 报 `Could not resolve hostname`
- 排查：`ip a` 没有 IP → 说明链路层断，不是 DNS
- 原因：**Windows 宿主机的 `VMware NAT Service` 停了**
- 解决：Windows `services.msc` 启动该服务 → 虚拟机里 `sudo nmcli networking off && sudo nmcli networking on`
- 教训：虚拟机"断网"先别在虚拟机里折腾，**先看宿主机的 VMware 服务**
