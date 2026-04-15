from common.logger import logger

class AssertUtil:
    """通用断言工具"""

    @staticmethod
    def assert_code(response, expected_code=200):
        """断言状态码"""
        try:
            actual_code = response.status_code
        except AttributeError:
            logger.error("❌ 传入的response对象不包含status_code属性！")
            raise
        assert actual_code == expected_code, \
        f"状态码断言失败！预期：{expected_code}，实际：{actual_code}"
        logger.info(f"✅ 状态码断言成功：{actual_code}")

    @staticmethod
    def assert_in(actual, expected):
        """断言包含"""
        assert actual is not None, "❌ 实际结果actual为None，无法进行包含断言"
        assert expected in str(actual), f"断言失败！预期包含：{expected}，实际：{actual}"
        logger.info(f"✅ 包含断言成功：{expected}在结果中")