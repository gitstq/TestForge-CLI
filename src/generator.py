#!/usr/bin/env python3
"""
测试用例生成器模块 - Test Case Generator Module
根据代码分析结果自动生成测试用例
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass

from .analyzer import FunctionInfo, ClassInfo, ModuleInfo, CodeAnalyzer


@dataclass
class TestCase:
    """测试用例数据结构"""
    name: str
    target_function: str
    test_code: str
    coverage_hints: List[str]
    difficulty: str  # easy, medium, hard


@dataclass
class GenerationResult:
    """生成结果数据结构"""
    total_generated: int
    test_file_path: str
    framework: str
    coverage_estimate: float
    test_cases: List[TestCase]


class TestGenerator:
    """测试用例生成器"""
    
    FRAMEWORK_TEMPLATES = {
        "pytest": {
            "header": "import pytest\n",
            "fixture": "@pytest.fixture\n",
            "mark": "@pytest.mark",
            "assert": "assert ",
            "setup": "def setup_function():",
            "teardown": "def teardown_function():",
        },
        "unittest": {
            "header": "import unittest\n",
            "fixture": "def setUp(self):",
            "mark": "# @unittest.skip",
            "assert": "self.assert",
            "setup": "def setUp(self):",
            "teardown": "def tearDown(self):",
        }
    }
    
    def __init__(self, path: str, language: str = "auto", framework: str = "pytest"):
        self.path = Path(path)
        self.language = language if language != "auto" else self._detect_language()
        self.framework = framework
        self.analyzer = CodeAnalyzer(path, language)
    
    def _detect_language(self) -> str:
        """检测语言"""
        ext = self.path.suffix.lower()
        if ext == ".py":
            return "python"
        elif ext in {".js", ".jsx"}:
            return "javascript"
        elif ext in {".ts", ".tsx"}:
            return "typescript"
        return "python"
    
    def generate(self, output_dir: str, target_coverage: int = 80) -> GenerationResult:
        """生成测试用例"""
        # 分析代码
        modules = self.analyzer.analyze()
        
        # 创建输出目录
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # 生成测试文件
        test_file = output_path / f"test_{self._get_module_name()}.py"
        
        all_test_cases = []
        for module in modules:
            test_cases = self._generate_module_tests(module)
            all_test_cases.extend(test_cases)
        
        # 写入测试文件
        test_content = self._build_test_file(all_test_cases)
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(test_content)
        
        return GenerationResult(
            total_generated=len(all_test_cases),
            test_file_path=str(test_file),
            framework=self.framework,
            coverage_estimate=min(95, target_coverage + 15),
            test_cases=all_test_cases
        )
    
    def _get_module_name(self) -> str:
        """获取模块名称"""
        if self.path.is_file():
            return self.path.stem
        return self.path.name
    
    def _generate_module_tests(self, module: ModuleInfo) -> List[TestCase]:
        """为模块生成测试用例"""
        test_cases = []
        
        # 生成函数测试
        for func in module.functions:
            if not func.is_test:  # 跳过已有的测试函数
                test_case = self._generate_function_test(func)
                if test_case:
                    test_cases.append(test_case)
        
        # 生成类测试
        for cls in module.classes:
            test_case = self._generate_class_test(cls)
            if test_case:
                test_cases.append(test_case)
        
        return test_cases
    
    def _generate_function_test(self, func: FunctionInfo) -> Optional[TestCase]:
        """为函数生成测试用例"""
        if self.framework == "pytest":
            return self._generate_pytest_function_test(func)
        elif self.framework == "unittest":
            return self._generate_unittest_function_test(func)
        return None
    
    def _generate_pytest_function_test(self, func: FunctionInfo) -> TestCase:
        """生成pytest格式的函数测试"""
        test_name = f"test_{func.name}"
        
        # 根据参数数量和复杂度生成测试用例
        if len(func.params) == 0:
            test_code = f'''
def {test_name}():
    """测试 {func.name} 函数 - 无参数情况"""
    # 调用函数
    result = {func.name}()
    
    # 断言结果
    assert result is not None
'''
        elif len(func.params) == 1:
            test_code = f'''
def {test_name}():
    """测试 {func.name} 函数 - 单参数"""
    # 准备测试数据
    test_input = None  # TODO: 根据实际业务填充测试数据
    
    # 调用函数
    result = {func.name}(test_input)
    
    # 断言结果
    assert result is not None


def {test_name}_edge_cases():
    """测试 {func.name} 函数 - 边界情况"""
    # 空输入
    result = {func.name}([])
    assert result is not None
    
    # 大量数据
    result = {func.name}(range(1000))
    assert result is not None
'''
        else:
            # 多参数函数
            params_str = ", ".join([f"param{i}" for i in range(len(func.params))])
            test_code = f'''
@pytest.mark.parametrize("params", [
    # TODO: 添加测试用例
])
def {test_name}(params):
    """测试 {func.name} 函数 - 参数化测试"""
    # 调用函数
    result = {func.name}({params_str})
    
    # 断言结果
    assert result is not None


def {test_name}_success():
    """测试 {func.name} 函数 - 成功场景"""
    # 准备测试数据
    test_data = {{}}  # TODO: 根据实际业务填充
    
    # 调用函数
    result = {func.name}(**test_data)
    
    # 断言结果
    assert result is not None
'''
        
        # 根据复杂度确定难度
        if func.complexity < 3:
            difficulty = "easy"
        elif func.complexity < 7:
            difficulty = "medium"
        else:
            difficulty = "hard"
        
        return TestCase(
            name=test_name,
            target_function=func.name,
            test_code=test_code,
            coverage_hints=self._get_coverage_hints(func),
            difficulty=difficulty
        )
    
    def _generate_unittest_function_test(self, func: FunctionInfo) -> TestCase:
        """生成unittest格式的函数测试"""
        class_name = f"Test{func.name.title().replace('_', '')}"
        test_name = f"test_{func.name}"
        
        test_code = f'''
class {class_name}(unittest.TestCase):
    """测试 {func.name} 函数的单元测试类"""
    
    def {test_name}(self):
        """测试 {func.name} 函数 - 基本功能"""
        # 准备测试数据
        test_input = None  # TODO: 根据实际业务填充
        
        # 调用函数
        result = {func.name}(test_input)
        
        # 断言结果
        self.assertIsNotNone(result)
    
    def {test_name}_edge_cases(self):
        """测试 {func.name} 函数 - 边界情况"""
        # 空输入测试
        result = {func.name}([])
        self.assertIsNotNone(result)
'''
        
        return TestCase(
            name=test_name,
            target_function=func.name,
            test_code=test_code,
            coverage_hints=self._get_coverage_hints(func),
            difficulty="medium"
        )
    
    def _generate_class_test(self, cls: ClassInfo) -> Optional[TestCase]:
        """为类生成测试用例"""
        if not cls.methods:
            return None
        
        if self.framework == "pytest":
            test_code = f'''
class Test{cls.name.title().replace('_', '')}:
    """测试 {cls.name} 类的单元测试"""
    
    def setup_method(self):
        """每个测试方法前的setup"""
        self.instance = {cls.name}()
    
    def teardown_method(self):
        """每个测试方法后的cleanup"""
        self.instance = None
'''
        else:
            test_code = f'''
class Test{cls.name.title().replace('_', '')}(unittest.TestCase):
    """测试 {cls.name} 类的单元测试"""
    
    def setUp(self):
        """每个测试方法前的setup"""
        self.instance = {cls.name}()
    
    def tearDown(self):
        """每个测试方法后的cleanup"""
        self.instance = None
'''
        
        for method in cls.methods:
            if not method.is_test and not method.name.startswith("_"):
                test_method = f"    def test_{method.name}(self):\n"
                test_method += f'        """测试 {cls.name}.{method.name} 方法"""\n'
                test_method += f"        result = self.instance.{method.name}()\n"
                test_method += f"        self.assertIsNotNone(result)\n\n"
                test_code += test_method
        
        return TestCase(
            name=f"test_{cls.name.lower()}",
            target_function=cls.name,
            test_code=test_code,
            coverage_hints=[f"测试类 {cls.name} 的所有公共方法"],
            difficulty="medium"
        )
    
    def _get_coverage_hints(self, func: FunctionInfo) -> List[str]:
        """获取覆盖率提示"""
        hints = [
            f"测试函数入口",
            f"测试返回值验证",
        ]
        
        if func.complexity > 3:
            hints.append("测试条件分支")
        
        if len(func.params) > 0:
            hints.append("测试参数边界")
            hints.append("测试参数组合")
        
        return hints
    
    def _build_test_file(self, test_cases: List[TestCase]) -> str:
        """构建完整的测试文件"""
        template = self.FRAMEWORK_TEMPLATES.get(self.framework, self.FRAMEWORK_TEMPLATES["pytest"])
        
        header = f'''#!/usr/bin/env python3
"""
自动生成的测试文件 - Generated by TestForge
生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
框架: {self.framework}

⚠️  注意: 此文件由TestForge自动生成
    请根据实际业务需求补充和修改测试用例
"""

{template["header"]}
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


# ============================================================================
# 测试用例
# ============================================================================

'''
        
        content = header
        
        # 添加模块级docstring
        content += '"""测试模块 - Test Module"""\n\n'
        
        for test_case in test_cases:
            content += f'# 测试目标: {test_case.target_function}\n'
            content += f'# 难度等级: {test_case.difficulty}\n'
            content += test_case.test_code
            content += "\n\n"
        
        # 添加main入口
        if self.framework == "pytest":
            content += '''
# ============================================================================
# 运行测试
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
'''
        else:
            content += '''
# ============================================================================
# 运行测试
# ============================================================================

if __name__ == "__main__":
    unittest.main(verbosity=2)
'''
        
        return content
    
    def display_summary(self, results: GenerationResult):
        """显示生成摘要"""
        print("\n" + "="*60)
        print("✅ 测试用例生成完成!")
        print("="*60)
        print(f"📁 生成文件: {results.test_file_path}")
        print(f"🧪 生成用例: {results.total_generated} 个")
        print(f"🎯 测试框架: {results.framework}")
        print(f"📊 预估覆盖率: {results.coverage_estimate}%")
        
        difficulty_stats = {}
        for tc in results.test_cases:
            difficulty_stats[tc.difficulty] = difficulty_stats.get(tc.difficulty, 0) + 1
        
        if difficulty_stats:
            print(f"\n📈 难度分布:")
            for level, count in sorted(difficulty_stats.items()):
                indicator = "🟢" if level == "easy" else "🟡" if level == "medium" else "🔴"
                print(f"   {indicator} {level}: {count} 个")
        
        print("\n" + "="*60)
        print("💡 下一步操作:")
        print("   1. 根据业务需求补充测试数据")
        print(f"   2. 运行测试: pytest {results.test_file_path} -v")
        print("   3. 检查覆盖率: pytest --cov")
        print("   4. 使用 assess 命令评估测试质量")
        print("="*60)
