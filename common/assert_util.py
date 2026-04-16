from common.logger import logger
from common.db_util import db

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

    @staticmethod
    def assert_db_exist(sql, params=None):
        """断言数据库结果存在"""
        result = db.query(sql, params)
        assert len(result) > 0, "❌ 数据库数据不存在"
        logger.info("✅ 数据库数据存在")

    @staticmethod
    def assert_db_equal(sql, params, field, expect):
        """断言字段值相等"""
        result = db.query(sql, params)
        assert len(result) > 0, "❌ 数据库未查询到数据"
        actual = result[0][field]
        assert actual == expect, f"❌ 字段【{field}】错误：预期 {expect}，实际 {actual}"
        logger.info(f"✅ 数据库字段断言通过：{field} = {expect}")