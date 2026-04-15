import requests
import json
from common.logger import logger
from config.settings import TOKEN_KEY, TOKEN_PREFIX
from urllib3.util import timeout


class RequestHandler:
    """请求封装类：统一处理所有接口请求"""

    def __init__(self):
        # 初始化会话（保持cookie/会话，提高请求效率）
        self.session = requests.Session()
        self.token = None

    def set_token(self ,token):
        """外部设置token"""
        self.token = token
        logger.info(f"✅ token已设置：{self.token}")

    def send_request(self, method, url, **kwargs):
        """

        :param method: 请求方法 GET/POST/PUT/DELETE
        :param url: 请求地址
        :param kwargs: 其他参数：params，json，headers，data
        :return: 响应参数
        """
        # 统一转大写，避免大小写问题
        method = method.upper()

        # 自动添加 token 到请求头
        if self.token:
            headers = kwargs.get("headers", {})
            headers[TOKEN_KEY] = TOKEN_PREFIX + self.token
            kwargs["headers"] = headers

        # 防止程序直接崩掉，保证测试能跑完，还能知道是哪一步出了问题。
        try:
            # 打印以下日志到控制台和文件；安全写法：kwargs.get()，不存在返回None
            logger.info(f"发送请求：{method} {url}")
            if kwargs.get("params"):
                logger.info(f"请求参数：{kwargs.get('params')}")
            if kwargs.get("json"):
                logger.info(f"请求JSON：{kwargs.get('json')}")

            # 发送请求
            response = self.session.request(method, url=url, timeout=10, **kwargs)

            # 打印日志（私有方法，给人看的，建议你别在外部调用、别修改）
            self._print_log(response)

            return response

        except Exception as e:
            print(f"请求异常：{str(e)}")     #str(e)用户可读
            raise e

    def _print_log(self, response):
        """打印请求日志（私有方法）"""
        logger.info("=" * 50)
        logger.info(f"请求地址：{response.url}")
        logger.info(f"请求方法：{response.request.method}")
        logger.info(f"响应状态码：{response.status_code}")

        # 尝试打印响应体
        try:
            logger.info(f"响应内容：{json.dumps(response.json(), ensure_ascii=False, indent=4)}")
        except:
            logger.info(f"响应内容：{response.text}")
        logger.info("=" * 50)
