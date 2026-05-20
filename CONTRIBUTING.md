# Contributing to TestForge

感谢您对 TestForge 项目的关注！🎉

本文档将指导您如何为 TestForge 做出贡献。

## 📋 目录

- [行为准则](#行为准则)
- [入门指南](#入门指南)
- [开发环境设置](#开发环境设置)
- [开发流程](#开发流程)
- [提交规范](#提交规范)
- [测试指南](#测试指南)
- [文档贡献](#文档贡献)

## 🎭 行为准则

请尊重所有社区成员，保持友好和专业的交流态度。我们不容忍任何形式的骚扰行为。

## 🚀 入门指南

### 了解项目

在开始贡献之前，请先：

1. 阅读项目的 README 文件，了解项目背景和目标
2. 查看现有的 Issues，了解当前的需求和改进方向
3. 熟悉项目的基本使用方法

### 选择任务

您可以从以下类型的任务开始：

- 🐛 **Bug修复** - 修复已知问题
- 📝 **文档改进** - 完善README或添加示例
- 🎨 **代码优化** - 提升代码质量或性能
- ✨ **新功能** - 实现新的功能或特性

## 💻 开发环境设置

### 1. 克隆仓库

```bash
git clone https://github.com/gitstq/TestForge.git
cd TestForge
```

### 2. 创建虚拟环境（推荐）

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
.\venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
# 开发依赖
pip install pytest pytest-cov black mypy

# 安装项目
pip install -e .
```

### 4. 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行特定测试
pytest tests/test_analyzer.py -v

# 生成覆盖率报告
pytest tests/ --cov=src --cov-report=html
```

## 🔨 开发流程

### 1. 创建分支

```bash
# 创建功能分支
git checkout -b feature/your-feature-name

# 创建修复分支
git checkout -b fix/issue-description
```

### 2. 进行开发

请遵循以下开发原则：

- ✅ 编写清晰、可读的代码
- ✅ 添加必要的注释和文档
- ✅ 确保代码符合项目规范
- ✅ 编写或更新相关测试

### 3. 提交代码

```bash
# 添加更改
git add .

# 提交（遵循提交规范）
git commit -m "feat: 添加新功能"
```

### 4. 推送并创建PR

```bash
# 推送到远程
git push origin feature/your-feature-name

# 在GitHub上创建Pull Request
```

## 📝 提交规范

我们使用 Angular 提交规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 类型 (type)

- `feat`: 新功能
- `fix`: Bug修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 代码重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建/工具相关

### 示例

```
feat(analyzer): 添加JavaScript代码分析支持

- 支持ES6+语法
- 添加类和方法识别
- 支持async/await检测

Closes #123
```

```
fix(generator): 修复pytest参数化测试生成错误

- 修正参数解析逻辑
- 添加边界情况处理
- 更新测试用例

Related to #456
```

## 🧪 测试指南

### 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行特定模块测试
pytest tests/test_analyzer.py -v

# 运行带覆盖率的测试
pytest tests/ --cov=src --cov-report=term-missing
```

### 编写测试

- 测试文件命名：`test_<module_name>.py`
- 测试函数命名：`test_<functionality>`
- 使用清晰的断言消息
- 覆盖正常情况和边界情况

### 示例

```python
def test_analyzer_initialization():
    """测试分析器初始化"""
    from src.analyzer import CodeAnalyzer
    
    analyzer = CodeAnalyzer("./src", "python")
    
    assert analyzer is not None
    assert analyzer.language == "python"
```

## 📚 文档贡献

文档改进同样重要！您可以：

- ✏️ 修正拼写错误或语法问题
- 📖 添加或改进使用示例
- 🌐 翻译文档到其他语言
- 📝 完善API文档

### 文档更新

- README 文件位于项目根目录
- 文档使用 Markdown 格式
- 请保持语言简洁清晰

## ❓ 获取帮助

如果您在贡献过程中遇到问题：

1. 查看项目的 [FAQ](./docs/faq.md)
2. 搜索现有的 [Issues](https://github.com/gitstq/TestForge/issues)
3. 创建新的 Issue 寻求帮助

## 📄 许可证

通过贡献代码，您同意您的贡献将在 MIT 许可证下发布。

---

再次感谢您的贡献！🙏

<div align="center">

**让我们一起让 TestForge 变得更好！**

</div>
