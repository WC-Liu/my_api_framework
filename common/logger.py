import logging
import os
from datetime import datetime
from common.path_util import get_path

# 日志存放目录
LOG_DIR = get_path("logs")
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

# 日志文件名（按日期生成）
log_file = os.path.join(LOG_DIR, datetime.now().strftime("%Y-%m-%d") + ".log")

# 日志配置
logger = logging.getLogger("my_api_framework")
logger.setLevel(logging.INFO)
logger.handlers.clear() # 避免重复打印

# 文件处理器
file_handler = logging.FileHandler(log_file, encoding = "utf-8")
file_handler.setLevel(logging.INFO)

# 控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 日志格式
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)-5s - %(filename)-15s - %(lineno)3d - %(message)s"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 添加处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)