from common.logger import logger

class AssertUtil:
    """通用断言工具"""

    @staticmethod
    def assert_code(response, expected_code=200):
        """断言状态码"""

        actual_code = response.status_code
        assert actual_code == expected_code,f"❌ 状态码错误：预期{expected_code}，实际{actual_code}"
        logger.info(f"✅ 状态码断言成功：{actual_code}")

    @staticmethod
    def assert_in(actual, expected):
        """断言包含"""
        assert expected in str(actual), f"断言失败！预期包含：{expected}，实际：{actual}"
        logger.info(f"✅ 包含断言成功：{expected}在结果中")