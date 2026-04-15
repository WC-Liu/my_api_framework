from api.api_service import ApiService
import pytest
from common.assert_util import AssertUtil
from common.yaml_util import YamlUtil
from requests import session

# 读取 YAMl 数据
data = YamlUtil.read_yaml("test_data/demo_api_data.yaml")

# 初始化接口对象（整个测试文件只用一次）
@pytest.fixture(scope="session")
def api():
    return ApiService()


# 测试类必须以 Test 开头
class TestDemo:

    @pytest.mark.parametrize("case", data["get_demo"])
    def test_get_demo(self, case, api):
        """测试 GET 接口"""
        # 1. 准备参数
        params = {"page": case["page"]}

        # 2. 调用接口
        response = api.get_demo_data(params=params)

        # 3. 工具断言（判断结果是否正确）
        AssertUtil.assert_code(response, 200)
        AssertUtil.assert_in(response.json(), case["expect"])

    @pytest.mark.parametrize("case", data["post_demo"])
    def test_post_demo(self, case, api):
        """测试 POST 接口"""
        # 1. 准备参数
        json_data = {"name": case["name"], "job": case["job"]}

        # 2. 调用接口
        response = api.post_demo_json(json_data=json_data)

        # 3. 断言（判断结果是否正确）
        AssertUtil.assert_code(response, 200)
        AssertUtil.assert_in(response.json(), case["expect"])
