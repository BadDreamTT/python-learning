"""加载配置文件"""

import os
from pathlib import Path
import yaml

def load_config(filename: str = "config.yaml") -> dict:
    #找到config.yaml的完整路径(和本文件同一个目录)

    file_path = Path(__file__).parent / filename

    #打开文件,读成python字典
    with open(str(file_path), "r") as f:
        config = yaml.safe_load(f)

    if os.getenv("BASE_URL"):
        config["base_url"] = os.getenv("BASE_URL")
    if os.getenv("TIMEOUT"):
        config["timeout"] = int(os.getenv("TIMEOUT"))

    return config

if __name__ == "__main__":
    cfg=load_config()
    print(cfg)