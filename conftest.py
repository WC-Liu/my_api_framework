import pytest
from common.logger import logger
from api.api_service import ApiService

api = ApiService()

@pytest.fixture(scope="session", autouse=True)
def start_test():
    logger.info("\n====== 接口自动化测试开始 =====")

    # ================= 安全版本：模拟登录 =================
    # 因为 httpbin.org 没有真正登录接口，所以直接模拟 token
    mock_token = "this_is_a_test_token_from_my_framework"
    api.req.set_token(mock_token)  # 给请求对象设置 token
    # ====================================================

    # 🔥 全局自动登录，所有用例自动带 token
    #res = api.login("admin", "123456")
    #token = res.json()["token"]
    #api.req.set_token(token)

    yield
    logger.info("\n===== 接口自动化测试结束=====")