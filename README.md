# FastAPI 接口自动化测试

基于 pytest + requests 实现的 FastAPI 接口自动化测试项目，专注用户模块 CRUD 接口测试，集成登录鉴权、数据库断言、Allure 可视化报告、YAML 配置管理。

## ✨ 项目特性

✅ 完整用户 CRUD 接口自动化用例 

✅ 登录鉴权自动获取 Token，全局关联接口

✅ 数据库断言：校验接口数据与 MySQL 一致性 

✅ YAML 管理测试配置、环境、用例数据 

✅ Allure 可视化美化测试报告 

✅ 用例失败自动重跑、日志记录 

✅ 独立于被测服务，跨环境执行

```text
# my_api_framework

├── api/                        # 接口服务层
│   └── api_service.py          # 接口请求封装（对接业务接口/第三方API）
├── common/                     # 通用工具层（核心公共方法）
│   ├── assert_util.py          # 断言工具（结果校验封装）
│   ├── db_util.py              # 数据库工具（MySQL/Redis等操作）
│   ├── logger.py               # 日志工具（日志格式/输出/落地）
│   ├── path_util.py            # 路径工具（项目绝对路径获取）
│   └── yaml_util.py            # YAML工具（测试数据/配置读取）
├── config/                     # 配置层
│   └── settings.py             # 全局配置（环境变量/基础URL/超时时间等）
├── core/                       # 核心引擎层
│   └── request_handler.py      # 请求核心封装（requests封装/请求头/签名处理）
├── logs/                       # 日志目录（运行日志落地）
├── test_data/                  # 测试数据层
│   └── user_data.yaml          # 测试数据（YAML格式存储测试用例数据）
├── testcases/                  # 测试用例层
│   ├── __init__.py             # 包标识
│   ├── test_api_mysql.py       # 数据库相关测试用例
│   └── test_fastapi.py         # FastAPI接口相关测试用例
├── .env                        # 环境变量配置（敏感信息/环境区分）
├── conftest.py                 # Pytest全局配置（fixture/钩子函数/环境初始化）
├── main.py                     # 项目入口（框架启动/执行入口）
├── pytest.ini                  # Pytest配置（用例规则/报告/插件）
```

## 🚀 快速开始（WSL2 + uv 环境）

### 环境要求

- WSL2 已安装（Ubuntu 20.04+）
- Python 3.12.3
- **uv** 包管理器

### 安装 uv（如未安装）

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

### 克隆项目并安装依赖

```bash
# 进入项目目录
cd my_api_framework
# 使用 uv 安装所有依赖
uv sync
```

### 运行测试用例

```bash
# 在项目根目录下激活虚拟环境
source .venv/bin/activate

# 直接运行所有用例
python main.py

# 自动生成allure报告，在浏览器使用一下地址打开(xxxxx每次测试会改变)
http://localhost:xxxxx
```

## ⚙️ 多环境切换

修改 `config/` 下的配置文件，可快速切换：

- 开发环境 dev
- 测试环境 test
- 预发环境 pre

## 📝 日志说明

- 日志自动生成在 `logs/` 目录
- 按天分割，支持多级日志（info/error/debug）
- 便于接口调试、问题回溯

## 📌 使用说明

- 新增接口：在 `api/` 目录封装业务接口
- 新增用例：在 `datas/` 编写 YAML 数据，`testcases/` 编写用例
- 公共方法统一放在 `common/`，实现代码复用

## 📊 项目价值

- 大幅降低回归测试成本
- 接口用例可维护性提升 80%
- 支持自动化流水线集成
- 适合企业级接口自动化落地