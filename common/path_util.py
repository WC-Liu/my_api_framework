import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_path(*args):
    """拼接项目绝对路径"""

    return os.path.join(BASE_DIR, *args)