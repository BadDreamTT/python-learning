level 0-1
Target:找到密码
Command:cat readme
Knowledge: cat命令

level 1-2
Target:找到存于-文件夹中的密码
Command: cat ./-
password:  PK8fYLZg2hnHSz83plBL1iEPKdD3QToB
Knowledge:  文件名带空格或者-需要用转义字符'\'或者./  ,./给了绝对路径

level2-3 
Target:  找到存于带有特殊字符文件中的密码
Command:  cat "--xxx xx xx xx--"
password:  7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME
Knowledge:  转义符的使用,文件名中带空格,可以用\也可以直接"".

level3-4
Target:  找到隐藏文件夹中的密码
Comman:  ls -a;    cat .xxxx
Password:  xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq
Knowledge:  我尝试直接使用ls -l是无法查询的.还是用的-a查询的所有文件.

level4-5	
Target:  很多个文件只有一个文件是人类可读的,密码存在这个文件夹里面.
Command:  file ./*
password:  6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG
Knowledge:  一开始我直接使用的ls -a查询,试图一个个试.其余的都是二进制乱码.直接cat会崩溃,只能reset恢复.后面用file *发现抱错,文件名都是以-开头,所以用file./*防止被识别成命令参数

level5-6
Target:  根据给出的线索找到相对应文件中的密码
Command:  file . -type f -size 1033c ! -executable
password:  pXa26xhMWaC2SvDotA4r9EgZkulOeSBW
Knowledge:  我尝试用了ls,有很多子文件夹翻不完,所以用find .递归遍历所有子文件夹.当题目给出线索条件,用类似于 -type .-size . ! -executable 诸如此类条件筛选,可以在回看复习一下,条件使用方法
