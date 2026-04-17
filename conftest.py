import pytest
from common.logger import logger
from api.api_service import ApiService
from common.db_util import db

TEST_TABLES = ["users"]

@pytest.fixture(scope="session", autouse=True)
def start_test():
    api = ApiService()
    logger.info("\n" + "=" * 60)
    logger.info("🚀 开始自动化测试")
    logger.info("=" * 60)

    # 登录鉴权
    res = api.login(username="testuser", password="testpass")
    token = res.json()["access_token"]
    logger.info(f"✅ 登录成功，token：{token[:20]}...")
    api.req.set_token(token)

    db.connect()
    yield api
    db.close()
    
    logger.info("\n" + "=" * 60)
    logger.info("🏁 测试结束")
    logger.info("=" * 60)

@pytest.fixture(scope="class", autouse=True)
def clean_after_test():
    """
    每个测试类跑完后清空一次
    """
    yield

    logger.info("\n🧹 测试类执行完毕，清空测试库")
    try:
        db.query("SET FOREIGN_KEY_CHECKS = 0")
        for table in TEST_TABLES:
            db.query(f"TRUNCATE TABLE {table}")
        db.query("SET FOREIGN_KEY_CHECKS = 1")
        db.conn.commit()
    except Exception as e:
        logger.error(f"❌ 清空失败: {e}")