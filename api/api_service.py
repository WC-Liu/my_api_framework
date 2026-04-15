from core.request_handler import RequestHandler
from config.settings import BASE_URL, LOGIN_URL

class ApiService:
    """
    接口服务类
    所有业务接口都在这里封装成方法
    测试用例直接调用方法即可
    """
    def __init__(self):
        self.req = RequestHandler()

    def login(self, username, password):
        """登录接口，获取token"""
        url =f"{BASE_URL}{LOGIN_URL}"
        json_data = {
            "username": username,
            "password": password
        }
        return self.req.send_request("POST", url, json=json_data)
    # 示例：GET 请求接口
    def get_demo_data(self, params=None):
        """演示 GET 接口"""
        url = f"{BASE_URL}/get"
        return self.req.send_request("GET", url, params=params)

    def post_demo_json(self, json_data):
        """演示 POST JSON 请求"""
        url = f"{BASE_URL}/post"
        return self.req.send_request("POST", url, json=json_data)

    def post_demo_form(self, data):
        """演示 POST 表单接口"""
        url = f"{BASE_URL}/post"
        return self.req.send_request("POST", url, data=data)