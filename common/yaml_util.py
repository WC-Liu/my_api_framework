import sys

import yaml
import os
from common.logger import logger
from yaml import safe_load
from common.path_util import get_path

class YamlUtil:
    """YAML 读写工具类"""

    @staticmethod
    def read_yaml(yaml_relative_path):
        """
        读取 YAML 文件
        :param yaml_path: YAML路径
        :return: 字典/列表数据
        """
        yaml_path = get_path(yaml_relative_path)

        if not os.path.exists(yaml_path):
            logger.error(f"YAML 文件不存在：{yaml_path}")
            raise FileExistsError(f"YAML 文件不存在：{yaml_path}")

        with open(yaml_path, "r", encoding="utf-8") as f:
            data = safe_load(f)
            if "pytest" in sys.modules:
                logger.info(f"YAML 读取成功：{yaml_path}")
            return data