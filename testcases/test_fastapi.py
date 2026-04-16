from common.assert_util import AssertUtil
from common.logger import logger
from common.yaml_util import YamlUtil

# 读取 YAMl 数据
data = YamlUtil.read_yaml("test_data/user_data.yaml")

# 测试类必须以 Test 开头
class TestFastAPIBackend:
    """
    本地 FastAPI 后端完整自动化测试
    流程：登录 → 查询 → 新增 → 修改 → 删除
    """


    user_id = None
    user_data = data.get("user", {})

    def test_01_get_index(self, api):
        """测试首页接口"""
        resp = api.get_index()
        AssertUtil.assert_code(resp, 200)

    def test_02_get_all_users(self, api):
        """测试获取所有用户"""
        resp = api.get_users()
        AssertUtil.assert_code(resp, 200)

    def test_03_create_user(self, api):
        """测试创建用户"""
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
        #user_id = resp.json()["user"]["id"]
        TestFastAPIBackend.user_id = resp.json()["user"]["id"]
        logger.info(f"✅ 创建用户成功，ID：{self.user_id}")#类属性

    def test_04_get_single_user(self, api):
        """测试查询单个用户"""
        assert self.user_id is not None, "❌ 创建用户失败，未获取到 user_id"
        resp = api.get_user_info(TestFastAPIBackend.user_id)
        AssertUtil.assert_code(resp, 200)

    def test_05_update_user(self, api):
        """测试修改用户"""
        update_data = self.user_data.get("update", {})
        resp = api.update_user(
            user_id=self.user_id,
            name = update_data.get("name"),
            age=update_data.get("age"),
            email=update_data.get("email")
        )
        AssertUtil.assert_code(resp, 200)

    def test_06_delete_user(self, api):
        """测试删除用户"""
        resp = api.delete_user(self.user_id)
        AssertUtil.assert_code(resp, 200)
        logger.info("🎉 完整业务流执行成功！")

