# TestForge 测试模块

## 测试文件说明

此目录包含 TestForge 自身的单元测试和集成测试。

### 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行特定测试文件
pytest tests/test_analyzer.py -v

# 生成覆盖率报告
pytest tests/ --cov=src --cov-report=html
```

### 测试结构

- `test_analyzer.py` - 代码分析器测试
- `test_generator.py` - 测试生成器测试
- `test_quality.py` - 质量评估器测试
- `conftest.py` - pytest 配置和 fixtures
