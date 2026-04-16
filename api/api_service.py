from core.request_handler import RequestHandler
from config.settings import BASE_URL

class ApiService:
    """
    接口服务类
    所有业务接口都在这里封装成方法
    测试用例直接调用方法即可
    """
    def __init__(self):
        self.req = RequestHandler()

    # ====================== 1. 登录（form-data）======================
    def login(self, username, password):
        """登录接口，获取token"""
        url =f"{BASE_URL}/login"
        data = {
            "username": username,
            "password": password
        }
        return self.req.send_request("POST", url, data=data)

    # ====================== 2. 首页 ======================
    def get_index(self):
        url = f"{BASE_URL}/"
        return self.req.send_request("GET", url)

    # ====================== 3. 获取所有用户 ======================
    def get_users(self):
        url = f"{BASE_URL}/users"
        return self.req.send_request("GET", url)

    # ====================== 4. 获取单个用户 ======================
    def get_user_info(self, user_id):
        """演示 POST JSON 请求"""
        url = f"{BASE_URL}/users/{user_id}"
        return self.req.send_request("GET", url)

    # ====================== 5. 新建用户 ======================
    def create_user(self, name, age, email):
        url = f"{BASE_URL}/users"
        json_data = {
            "name": name,
            "age": age,
            "email": email
        }
        return self.req.send_request("POST", url, json=json_data)

    # ====================== 6. 修改用户 ======================
    def update_user(self, user_id, name, age, email):
        url = f"{BASE_URL}/users/{user_id}"
        json_data = {
            "name": name,
            "age": age,
            "email": email
        }
        return self.req.send_request("PUT", url, json=json_data)

    # ====================== 7. 删除用户 ======================
    def delete_user(self, user_id):
        url = f"{BASE_URL}/users/{user_id}"
        return self.req.send_request("DELETE", url)