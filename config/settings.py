# _*_ coding: utf-8 _*_
from dotenv import load_dotenv
import os
"""
项目配置文件
"""
load_dotenv()

# 环境切换：test / pre / prod
ENV = os.getenv("ENV", "local")  # 如果没有，默认"test"

ENV_CONFIG = {
    "local": "http://localhost:8000",
    "test": "http://localhost:8000",
    "pre": "https://pre-httpbin.yourcompany.com",
    "prod": "https://httpbin.org"
}

BASE_URL = ENV_CONFIG[ENV]

# Token 配置
# 请求超时时间
TOKEN_KEY = "Authorization"
TOKEN_PREFIX = "Bearer "
TIMEOUT = 10
LOG_LEVEL = "INFO"

# ===================== MySQL 配置（WSL 本地）=====================
MYSQL_HOST = "localhost"   # WSL 里的 MySQL 直接写 localhost
MYSQL_PORT = 3306
MYSQL_USER = "root"        # 你的用户名
MYSQL_PASSWORD = "root"   # 你的密码
MYSQL_DB = "testdb"   # 你的数据库名