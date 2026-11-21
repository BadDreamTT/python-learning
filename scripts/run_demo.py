import argparse

parser = argparse.ArgumentParser(description="接口测试运行")
parser.add_argument("--timeout",type=int, default=10,help = "超时秒数")
parser.add_argument("--verbose",action="store_true",help = "输出调试信息")
parser.add_argument("--env", choices=["dev","test","prod"],default="test")
args = parser.parse_args()

print("timeout =",args.timeout)
print("verbose =",args.verbose)