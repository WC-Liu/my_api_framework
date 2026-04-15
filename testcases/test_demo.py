from api.api_service import ApiService
import pytest
from common.assert_util import AssertUtil
from common.yaml_util import YamlUtil

# 读取 YAMl 数据
yaml_data = YamlUtil.read_yaml("test_data/demo_api_data.yaml")
get_data = yaml_data["get_demo"]
post_data = yaml_data["post_demo"]

# 初始化接口对象（整个测试文件只用一次）
api = ApiService()

# 测试类必须以 Test 开头
class TestDemo:

    @pytest.mark.parametrize("case_data", get_data)
    def test_get_demo(self, case_data):
        """测试 GET 接口"""
        # 1. 准备参数
        params = {"name": case_data["name"], "age": case_data["age"]}
        expect = case_data["expect"]

        # 2. 调用接口
        response = api.get_demo_data(params=params)

        # 3. 工具断言（判断结果是否正确）
        AssertUtil.assert_code(response, 200)
        AssertUtil.assert_in(response.json(), expect)

    @pytest.mark.parametrize("case_data", post_data)
    def test_post_demo(self, case_data):
        """测试 POST 接口"""
        # 1. 准备参数
        json_data = {"username": case_data["username"], "password": case_data["password"]}
        expect = case_data["expect"]

        # 2. 调用接口
        response = api.post_demo_json(json_data=json_data)

        # 3. 断言（判断结果是否正确）
        AssertUtil.assert_code(response, 200)
        AssertUtil.assert_in(response.json(), expect)