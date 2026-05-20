#!/usr/bin/env python3
"""
代码分析器模块 - Code Analyzer Module
使用AST分析代码结构，识别可测试的函数和方法
"""

import ast
import os
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field


@dataclass
class FunctionInfo:
    """函数信息数据结构"""
    name: str
    line_number: int
    params: List[str]
    return_type: Optional[str]
    complexity: int
    docstring: Optional[str]
    is_async: bool = False
    is_test: bool = False


@dataclass
class ClassInfo:
    """类信息数据结构"""
    name: str
    line_number: int
    methods: List[FunctionInfo]
    base_classes: List[str] = field(default_factory=list)


@dataclass
class ModuleInfo:
    """模块信息数据结构"""
    path: str
    functions: List[FunctionInfo] = field(default_factory=list)
    classes: List[ClassInfo] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    total_lines: int = 0


class CodeAnalyzer:
    """代码分析器 - 使用AST分析Python代码结构"""
    
    SUPPORTED_LANGUAGES = {"python", "javascript", "typescript"}
    
    def __init__(self, path: str, language: str = "auto"):
        self.path = Path(path)
        self.language = self._detect_language(language)
        self.results: List[ModuleInfo] = []
    
    def _detect_language(self, language: str) -> str:
        """自动检测编程语言"""
        if language != "auto":
            return language
        
        ext = self.path.suffix.lower()
        lang_map = {
            ".py": "python",
            ".js": "javascript",
            ".ts": "typescript",
            ".jsx": "javascript",
            ".tsx": "typescript"
        }
        return lang_map.get(ext, "python")
    
    def analyze(self) -> List[ModuleInfo]:
        """执行代码分析"""
        if self.language == "python":
            return self._analyze_python()
        else:
            return self._analyze_js_ts()
    
    def _analyze_python(self) -> List[ModuleInfo]:
        """分析Python代码"""
        results = []
        
        for file_path in self._get_python_files():
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                tree = ast.parse(content, filename=str(file_path))
                module_info = self._extract_module_info(tree, str(file_path), content)
                results.append(module_info)
                
            except SyntaxError as e:
                print(f"⚠️ 语法错误 in {file_path}: {e}")
            except Exception as e:
                print(f"⚠️ 分析错误 in {file_path}: {e}")
        
        self.results = results
        return results
    
    def _analyze_js_ts(self) -> List[ModuleInfo]:
        """分析JavaScript/TypeScript代码（简化版）"""
        results = []
        
        extensions = {".js", ".jsx", ".ts", ".tsx"} if self.language == "javascript" else {".ts", ".tsx"}
        
        for file_path in self.path.rglob("*"):
            if file_path.suffix in extensions:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    # 简化分析：提取函数声明
                    module_info = ModuleInfo(path=str(file_path))
                    module_info.total_lines = len(content.splitlines())
                    
                    # 简单的正则匹配（实际项目中应使用专门的JS解析器）
                    import re
                    func_pattern = r'(?:export\s+)?(?:async\s+)?function\s+(\w+)|const\s+(\w+)\s*=\s*(?:async\s+)?\([^)]*\)\s*=>'
                    matches = re.finditer(func_pattern, content)
                    
                    for match in matches:
                        func_name = match.group(1) or match.group(2)
                        if func_name and not func_name.startswith("_"):
                            module_info.functions.append(FunctionInfo(
                                name=func_name,
                                line_number=content[:match.start()].count('\n') + 1,
                                params=[],
                                return_type=None,
                                complexity=1,
                                docstring=None
                            ))
                    
                    results.append(module_info)
                    
                except Exception as e:
                    print(f"⚠️ 分析错误 in {file_path}: {e}")
        
        self.results = results
        return results
    
    def _get_python_files(self) -> List[Path]:
        """获取所有Python文件"""
        files = []
        if self.path.is_file() and self.path.suffix == ".py":
            files.append(self.path)
        elif self.path.is_dir():
            for pattern in ["*.py", "**/*.py"]:
                files.extend(self.path.glob(pattern))
        return sorted(files)
    
    def _extract_module_info(self, tree: ast.AST, file_path: str, content: str) -> ModuleInfo:
        """从AST提取模块信息"""
        module_info = ModuleInfo(path=file_path)
        module_info.total_lines = len(content.splitlines())
        
        # 提取导入
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    module_info.imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    module_info.imports.append(node.module)
        
        # 提取函数和类
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                func_info = self._extract_function_info(node)
                module_info.functions.append(func_info)
            elif isinstance(node, ast.ClassDef):
                class_info = self._extract_class_info(node)
                module_info.classes.append(class_info)
        
        return module_info
    
    def _extract_function_info(self, node) -> FunctionInfo:
        """提取函数信息"""
        params = [arg.arg for arg in node.args.args]
        
        # 获取返回类型注解
        return_type = None
        if node.returns:
            return_type = ast.unparse(node.returns) if hasattr(ast, 'unparse') else "Any"
        
        # 计算复杂度
        complexity = self._calculate_complexity(node)
        
        # 获取文档字符串
        docstring = ast.get_docstring(node)
        
        return FunctionInfo(
            name=node.name,
            line_number=node.lineno,
            params=params,
            return_type=return_type,
            complexity=complexity,
            docstring=docstring,
            is_async=isinstance(node, ast.AsyncFunctionDef),
            is_test=node.name.startswith("test_") or node.name.endswith("_test")
        )
    
    def _extract_class_info(self, node) -> ClassInfo:
        """提取类信息"""
        base_classes = []
        for base in node.bases:
            if isinstance(base, ast.Name):
                base_classes.append(base.id)
        
        methods = []
        for item in node.body:
            if isinstance(item, ast.FunctionDef) or isinstance(item, ast.AsyncFunctionDef):
                methods.append(self._extract_function_info(item))
        
        return ClassInfo(
            name=node.name,
            line_number=node.lineno,
            methods=methods,
            base_classes=base_classes
        )
    
    def _calculate_complexity(self, node: ast.FunctionDef) -> int:
        """计算函数复杂度"""
        complexity = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
        return complexity
    
    def display_results(self, results: List[ModuleInfo], verbose: bool = False):
        """显示分析结果"""
        total_functions = sum(len(r.functions) for r in results)
        total_classes = sum(len(r.classes) for r in results)
        total_lines = sum(r.total_lines for r in results)
        
        print("\n" + "="*60)
        print("📊 代码分析报告")
        print("="*60)
        print(f"📁 分析路径: {self.path}")
        print(f"📄 分析文件: {len(results)} 个")
        print(f"📝 总代码行数: {total_lines}")
        print(f"🔧 函数数量: {total_functions}")
        print(f"🏛️ 类数量: {total_classes}")
        
        if verbose:
            print("\n" + "-"*60)
            print("📋 详细函数列表:")
            print("-"*60)
            
            for module in results:
                print(f"\n📂 {Path(module.path).name}")
                for func in module.functions:
                    complexity_indicator = "🟢" if func.complexity < 5 else "🟡" if func.complexity < 10 else "🔴"
                    test_indicator = "✓" if func.is_test else "○"
                    async_indicator = "⚡" if func.is_async else "  "
                    
                    print(f"  {test_indicator} {async_indicator} {complexity_indicator} {func.name}() @ L{func.line_number}")
                    if func.params:
                        print(f"      参数: {', '.join(func.params)}")
                    if func.docstring:
                        print(f"      说明: {func.docstring[:50]}...")
        
        print("\n" + "="*60)
        print("✨ 分析完成！")
        print("="*60)
