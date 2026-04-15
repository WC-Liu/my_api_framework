import pytest
import os
from common.path_util import get_path

if __name__ == '__main__':
    allure_result_path = get_path('report', 'allure_result')

    pytest.main([
        "./testcases/",
        "-vs",
        f"--alluredir={allure_result_path}",
        "--clean-alluredir",
        "--reruns=1",  # 失败重跑1次
        "--reruns-delay=1",  # 间隔1秒

    ])

    # 自动打开报告（需要安装 allure 并配置环境变量）
    os.system(f"allure serve {allure_result_path} --host 0.0.0.0")