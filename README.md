# API 接口自动化测试框架

基于 Python + pytest + requests 构建的企业级接口自动化测试框架，支持数据驱动、多环境切换、日志记录、可视化报告生成，适配 WSL2 开发环境。持续更新......

## ✨ 项目特性

- 分层架构设计，代码解耦、易维护、易扩展
- YAML 数据驱动，测试用例与代码分离
- 多环境配置一键切换（dev/test/pre）
- 完整日志系统，支持问题定位与回溯
- Allure 可视化测试报告
- 使用 uv 进行依赖管理，环境快速搭建
- 适配 WSL2 开发/运行环境

```text
api-auto-test/
├── api/ # 业务接口封装层
├── common/ # 公共工具类（断言、日志、工具函数）
├── config/ # 多环境配置文件
├── core/ # 核心请求封装（requests）
├── datas/ # YAML 测试数据
├── logs/ # 日志输出目录
├── reports/ # Allure 报告目录
├── testcases/ # 测试用例
├── .gitignore # Git 忽略文件
├── pyproject.toml # uv 依赖配置
├── pytest.ini # pytest 配置
└── README.md # 项目说明
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