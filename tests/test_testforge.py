#!/usr/bin/env python3
"""
TestForge 核心测试文件示例
此文件展示了TestForge生成的测试用例格式
"""

import pytest
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


# ============================================================================
# 测试示例：分析器模块
# ============================================================================

def test_analyzer_initialization():
    """测试分析器初始化"""
    from src.analyzer import CodeAnalyzer
    
    analyzer = CodeAnalyzer("./src", "python")
    
    assert analyzer is not None
    assert analyzer.language == "python"
    assert analyzer.path.name == "src"


def test_analyzer_detect_language():
    """测试语言自动检测"""
    from src.analyzer import CodeAnalyzer
    
    # Python检测
    analyzer_py = CodeAnalyzer("test.py", "auto")
    assert analyzer_py.language == "python"
    
    # JavaScript检测
    analyzer_js = CodeAnalyzer("test.js", "auto")
    assert analyzer_js.language == "javascript"
    
    # TypeScript检测
    analyzer_ts = CodeAnalyzer("test.ts", "auto")
    assert analyzer_ts.language == "typescript"


def test_analyzer_analyze_empty():
    """测试分析空目录"""
    from src.analyzer import CodeAnalyzer
    import tempfile
    import shutil
    
    # 创建临时目录
    temp_dir = tempfile.mkdtemp()
    
    try:
        analyzer = CodeAnalyzer(temp_dir, "python")
        results = analyzer.analyze()
        
        assert results is not None
        assert len(results) == 0
    finally:
        shutil.rmtree(temp_dir)


def test_analyzer_analyze_python_file():
    """测试分析Python文件"""
    from src.analyzer import CodeAnalyzer
    import tempfile
    import shutil
    
    # 创建临时Python文件
    temp_dir = tempfile.mkdtemp()
    test_file = Path(temp_dir) / "sample.py"
    
    test_code = '''
def hello():
    """Say hello"""
    return "Hello, World!"

def add(a, b):
    """Add two numbers"""
    return a + b

class Calculator:
    """Simple calculator"""
    
    def multiply(self, x, y):
        """Multiply two numbers"""
        return x * y
'''
    
    test_file.write_text(test_code)
    
    try:
        analyzer = CodeAnalyzer(test_file, "python")
        results = analyzer.analyze()
        
        assert len(results) == 1
        assert len(results[0].functions) >= 2
        assert len(results[0].classes) >= 1
    finally:
        shutil.rmtree(temp_dir)


# ============================================================================
# 测试示例：生成器模块
# ============================================================================

def test_generator_initialization():
    """测试生成器初始化"""
    from src.generator import TestGenerator
    
    generator = TestGenerator("./src", "python", "pytest")
    
    assert generator is not None
    assert generator.framework == "pytest"
    assert generator.language == "python"


def test_generator_framework_options():
    """测试不同的测试框架"""
    from src.generator import TestGenerator
    
    # pytest框架
    gen_pytest = TestGenerator("./src", "python", "pytest")
    assert gen_pytest.framework == "pytest"
    
    # unittest框架
    gen_unittest = TestGenerator("./src", "python", "unittest")
    assert gen_unittest.framework == "unittest"


# ============================================================================
# 测试示例：质量评估模块
# ============================================================================

def test_quality_assessor_initialization():
    """测试质量评估器初始化"""
    from src.quality import QualityAssessor
    
    assessor = QualityAssessor("./tests")
    
    assert assessor is not None
    assert assessor.test_path.name == "tests"


def test_quality_assessor_invalid_path():
    """测试无效路径"""
    from src.quality import QualityAssessor
    
    assessor = QualityAssessor("/nonexistent/path")
    
    with pytest.raises(FileNotFoundError):
        assessor.assess()


def test_quality_evaluate_naming():
    """测试命名规范评估"""
    from src.quality import QualityAssessor
    
    assessor = QualityAssessor("./tests")
    
    # 符合规范的代码
    good_code = '''
def test_something():
    """Good test"""
    assert True
    
def test_another_thing():
    """Another good test"""
    assert 1 == 1
'''
    
    metric = assessor._evaluate_naming(good_code)
    
    assert metric.name == "naming"
    assert metric.score >= 8  # 应该得到高分


def test_quality_evaluate_assertions():
    """测试断言评估"""
    from src.quality import QualityAssessor
    
    assessor = QualityAssessor("./tests")
    
    # 有断言的代码
    code_with_asserts = '''
def test_addition():
    assert 1 + 1 == 2
    assert 2 + 2 == 4
    assert 5 - 3 == 2
    
def test_multiplication():
    assert 2 * 3 == 6
    assert 4 * 4 == 16
'''
    
    metric = assessor._evaluate_assertions(code_with_asserts)
    
    assert metric.name == "assertions"
    assert metric.score > 30  # 应该有较高分数


# ============================================================================
# 测试示例：TUI模块
# ============================================================================

def test_tui_initialization():
    """测试TUI初始化"""
    from src.tui import TestForgeUI
    
    ui = TestForgeUI("./src", "python")
    
    assert ui is not None
    assert ui.path.name == "src"
    assert ui.language == "python"
    assert ui.running == True


# ============================================================================
# 集成测试
# ============================================================================

def test_full_workflow():
    """测试完整工作流程"""
    import tempfile
    import shutil
    from pathlib import Path
    
    # 创建临时项目
    temp_dir = tempfile.mkdtemp()
    src_dir = Path(temp_dir) / "src"
    src_dir.mkdir()
    
    # 创建示例代码
    sample_code = '''
def calculate_sum(a, b):
    """Calculate sum of two numbers"""
    return a + b

def calculate_product(a, b):
    """Calculate product of two numbers"""
    return a * b
'''
    
    (src_dir / "math_utils.py").write_text(sample_code)
    
    try:
        # 1. 分析
        from src.analyzer import CodeAnalyzer
        analyzer = CodeAnalyzer(str(src_dir), "python")
        analysis_results = analyzer.analyze()
        
        assert len(analysis_results) == 1
        assert len(analysis_results[0].functions) == 2
        
        # 2. 生成
        from src.generator import TestGenerator
        tests_dir = Path(temp_dir) / "tests"
        generator = TestGenerator(str(src_dir), "python", "pytest")
        gen_results = generator.generate(str(tests_dir))
        
        assert gen_results.total_generated >= 2
        assert tests_dir.exists()
        
        # 3. 评估
        from src.quality import QualityAssessor
        assessor = QualityAssessor(str(tests_dir))
        quality_results = assessor.assess()
        
        assert quality_results.overall_score > 0
        
    finally:
        shutil.rmtree(temp_dir)


# ============================================================================
# 运行测试
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
