import pytest
from common.assert_util import AssertUtil
from common.logger import logger
from common.yaml_util import YamlUtil

# 读取 YAMl 数据
data = YamlUtil.read_yaml("test_data/user_data.yaml")

class TestFastAPIBackend:
    """
    本地 FastAPI 后端完整自动化测试
    流程：登录 → 查询 → 新增 → 修改 → 删除
    """
    user_id = None
    user_data = data.get("user", {})

    def test_01_get_index(self, start_test):
        """测试首页接口"""
        api = start_test
        resp = api.get_index()
        AssertUtil.assert_code(resp, 200)

    def test_02_get_all_users(self, start_test):
        """测试获取所有用户"""
        api = start_test
        resp = api.get_users()
        AssertUtil.assert_code(resp, 200)

    def test_03_create_user(self, start_test):
        """测试创建用户"""
        api = start_test
        name = self.user_data.get("name")
        age = self.user_data.get("age")
        email = self.user_data.get("email")

        resp = api.create_user(
            name=name,
            age=age,
            email=email
        )
        AssertUtil.assert_code(resp, 200)
        # 把创建的用户ID存下来，给后面用例使用
        TestFastAPIBackend.user_id = resp.json()["user"][0]
        logger.info(f"✅ 创建用户成功，ID：{self.user_id}")

    def test_04_get_single_user(self, start_test):
        """测试查询单个用户"""
        api = start_test
        assert self.user_id is not None, "❌ 创建用户失败，未获取到 user_id"
        resp = api.get_user_info(TestFastAPIBackend.user_id)
        AssertUtil.assert_code(resp, 200)

    def test_05_update_user(self, start_test):
        """测试修改用户"""
        api = start_test
        update_data = self.user_data.get("update", {})
        name = update_data.get("name")
        age = update_data.get("age")
        email = update_data.get("email")

        resp = api.update_user(
            user_id=self.user_id,
            name=name,
            age=age,
            email=email
        )
        AssertUtil.assert_code(resp, 200)

        sql = "SELECT * FROM users WHERE id = %s"
        AssertUtil.assert_db_exist(sql, [self.user_id])
        AssertUtil.assert_db_equal(sql, [self.user_id], "name", name)
        AssertUtil.assert_db_equal(sql, [self.user_id], "age", age)
        AssertUtil.assert_db_equal(sql, [self.user_id], "email", email)

    #@pytest.mark.flaky(reruns=0)
    def test_06_delete_user(self, start_test):
        """测试删除用户"""
        api = start_test
        resp = api.delete_user(self.user_id)
        AssertUtil.assert_code(resp, 200)

        sql = "SELECT * FROM users WHERE id = %s"
        AssertUtil.assert_db_not_exist(sql, [self.user_id])

