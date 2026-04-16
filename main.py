import pytest
import os
from common.path_util import get_path

if __name__ == '__main__':
    allure_result_path = get_path('report', 'allure_result')

    # ====================== 【在这里切换用例】======================
    # 1. 运行 FastAPI 基础用例
    # case_path = "testcases/test_fastapi.py"

    # 2. 运行 MySQL 数据库断言用例
    case_path = "testcases/test_api_mysql.py"

    # 3. 运行所有用例（正式测试）
    # case_path = "testcases/"
    # =================================================================

    pytest.main([
        case_path,
        "-vs",
        f"--alluredir={allure_result_path}",
        "--clean-alluredir",
        "--reruns=1",  # 失败重跑1次
        "--reruns-delay=1",  # 间隔1秒

    ])

    # 自动打开报告（需要安装 allure 并配置环境变量）
    os.system(f"allure serve {allure_result_path} --host 0.0.0.0 --port 8080")