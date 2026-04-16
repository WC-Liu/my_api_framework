import pytest
from common.logger import logger
from api.api_service import ApiService
from common.db_util import db

@pytest.fixture(scope="session", autouse=True)
def api():
    api = ApiService()
    logger.info("\n" + "=" * 60)
    logger.info("🚀 开始自动化测试")
    logger.info("=" * 60)

    # 1. 登录
    res = api.login(username="testuser", password="testpass")
    # 2. 提取token
    token = res.json()["access_token"]
    logger.info(f"✅ 登录成功，token：{token[:20]}...")
    # 3. 全局设置 token，所有接口自动携带
    api.req.set_token(token)

    db.connect()

    yield api

    db.close()
    
    logger.info("\n" + "=" * 60)
    logger.info("🏁 测试结束")
    logger.info("=" * 60)