import pytest
from api.api_service import ApiService
from common.assert_util import AssertUtil
from common.logger import logger
from common.db_util import db
from common.yaml_util import YamlUtil

data = YamlUtil.read_yaml("test_data/user_data.yaml")
class TestApiMsql:

    user_id = None
    user_data = data.get("user", {})

    def test_create_user_and_check_db(self, api):
        name = self.user_data.get("name")
        age = self.user_data.get("age")
        email = self.user_data.get("email")

        resp = api.create_user(name, age, email)
        AssertUtil.assert_code(resp, 200)

        TestApiMsql.user_id = resp.json()["user"][0]
        logger.info(f"✅ 创建用户ID：{TestApiMsql.user_id}")

        # ===================== 数据库断言开始 =====================
        sql = "SELECT * FROM users WHERE id = %s"
        #result = db.query(sql, self.user_id)

        AssertUtil.assert_db_exist(sql, [TestApiMsql.user_id])

        AssertUtil.assert_db_equal(sql, [TestApiMsql.user_id], "name", name)
        AssertUtil.assert_db_equal(sql, [TestApiMsql.user_id], "age", age)
        AssertUtil.assert_db_equal(sql, [TestApiMsql.user_id], "email", email)

