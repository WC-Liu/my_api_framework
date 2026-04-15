import pytest
import os
from common.path_util import get_path

if __name__ == '__main__':

    pytest.main([
        "./testcases/",
        "-vs",
        f"--alluredir={get_path('report', 'allure_result')}",
        "--clean-alluredir"

    ])

    # 自动打开报告（需要安装 allure 并配置环境变量）
    allure_result_path = get_path('report', 'allure_result')
    os.environ['LANG'] = 'zh_CN.UTF-8'
    os.system(f"allure serve {allure_result_path} --host 0.0.0.0")