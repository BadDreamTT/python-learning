print("【1】a.py 开始加载，__name__ =", __name__)

def hello():
    print("【3】hello 函数执行了")

print("【2】a.py 加载结束")

if __name__ == "__main__":
    print("【4】我是被直接运行的，所以这行会打印")
    hello()