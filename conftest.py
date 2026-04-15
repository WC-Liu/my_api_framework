import pytest
from common.logger import logger
from api.api_service import ApiService

api = ApiService()

@pytest.fixture(scope="session", autouse=True)
def start_test():
    logger.info("\n" + "=" * 60)
    logger.info("🚀 开始自动化测试")
    logger.info("=" * 60)

    # 🔥 全局自动登录，所有用例自动带 token
    res = api.login("test@demo.com", "123456")
    token = "mock_token_123456789"
    api.req.set_token(token)

    yield
    logger.info("\n" + "=" * 60)
    logger.info("🏁 测试结束")
    logger.info("=" * 60)