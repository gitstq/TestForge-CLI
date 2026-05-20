#!/usr/bin/env python3
"""
TestForge TUI - 终端用户界面模块
提供交互式的终端仪表盘
"""

import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

from .analyzer import CodeAnalyzer
from .generator import TestGenerator
from .quality import QualityAssessor


class TestForgeUI:
    """TestForge TUI界面"""
    
    def __init__(self, path: str, language: str = "auto"):
        self.path = Path(path)
        self.language = language
        self.analyzer = CodeAnalyzer(path, language)
        self.running = True
        self.current_view = "main"
        
        # 数据缓存
        self.analysis_results = None
        self.test_results = None
        self.quality_results = None
    
    def run(self):
        """运行TUI界面"""
        self._print_header()
        self._print_main_menu()
        
        while self.running:
            try:
                choice = input("\n🔶 请选择操作 [1-6]: ").strip()
                
                if choice == "1":
                    self._do_analyze()
                elif choice == "2":
                    self._do_generate()
                elif choice == "3":
                    self._do_assess()
                elif choice == "4":
                    self._show_dashboard()
                elif choice == "5":
                    self._show_help()
                elif choice == "6":
                    self._quit()
                else:
                    print("⚠️ 无效选择，请重新输入")
                    
            except KeyboardInterrupt:
                self._quit()
            except Exception as e:
                print(f"❌ 错误: {e}")
    
    def _print_header(self):
        """打印头部信息"""
        header = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║     🧪  T E S T F O R G E                                       ║
║     ─────────────────────────────────────────                    ║
║     智能测试用例生成与质量评估引擎                                 ║
║     Intelligent Test Case Generation & Quality Assessment        ║
║                                                                  ║
║     Version: 1.0.0  |  License: MIT  |  Zero Dependencies       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
        print(header)
    
    def _print_main_menu(self):
        """打印主菜单"""
        menu = """
╭─────────────────────────────────────────────────────────────────╮
│                        📋 主菜单                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   1️⃣  [Analyze]    分析代码结构                                 │
│                   分析项目中的可测试单元                         │
│                                                                 │
│   2️⃣  [Generate]   生成测试用例                                 │
│                   根据分析结果自动生成测试代码                    │
│                                                                 │
│   3️⃣  [Assess]     评估测试质量                                 │
│                   评估现有测试用例的质量和覆盖率                  │
│                                                                 │
│   4️⃣  [Dashboard]   显示仪表盘                                   │
│                   综合展示分析、生成、评估结果                    │
│                                                                 │
│   5️⃣  [Help]       帮助信息                                     │
│                   查看详细使用说明                               │
│                                                                 │
│   6️⃣  [Quit]       退出程序                                     │
│                   退出TestForge                                 │
│                                                                 │
╰─────────────────────────────────────────────────────────────────╯
"""
        print(menu)
    
    def _do_analyze(self):
        """执行代码分析"""
        print("\n" + "="*60)
        print("🔍 执行代码分析...")
        print("="*60)
        
        try:
            self.analysis_results = self.analyzer.analyze()
            self.analyzer.display_results(self.analysis_results, verbose=True)
            
            # 保存结果
            print("\n💾 分析结果已缓存，可用于后续操作")
            
        except Exception as e:
            print(f"❌ 分析失败: {e}")
        
        input("\n按Enter键返回主菜单...")
        self._print_main_menu()
    
    def _do_generate(self):
        """执行测试生成"""
        print("\n" + "="*60)
        print("⚙️ 执行测试用例生成...")
        print("="*60)
        
        # 获取参数
        output_dir = input("📁 输出目录 [默认: ./tests]: ").strip() or "./tests"
        framework = input("🛠️ 测试框架 [pytest/unittest, 默认: pytest]: ").strip() or "pytest"
        
        if framework not in ["pytest", "unittest"]:
            print("⚠️ 无效框架，使用默认: pytest")
            framework = "pytest"
        
        try:
            generator = TestGenerator(str(self.path), self.language, framework)
            self.test_results = generator.generate(output_dir)
            generator.display_summary(self.test_results)
            
        except Exception as e:
            print(f"❌ 生成失败: {e}")
        
        input("\n按Enter键返回主菜单...")
        self._print_main_menu()
    
    def _do_assess(self):
        """执行质量评估"""
        print("\n" + "="*60)
        print("📊 执行测试质量评估...")
        print("="*60)
        
        # 获取测试路径
        test_path = input("📁 测试文件/目录路径: ").strip()
        
        if not test_path:
            print("⚠️ 请提供有效的测试路径")
            input("\n按Enter键返回主菜单...")
            self._print_main_menu()
            return
        
        try:
            assessor = QualityAssessor(test_path)
            self.quality_results = assessor.assess()
            assessor.display_report(self.quality_results)
            
        except Exception as e:
            print(f"❌ 评估失败: {e}")
        
        input("\n按Enter键返回主菜单...")
        self._print_main_menu()
    
    def _show_dashboard(self):
        """显示仪表盘"""
        print("\n" + "="*60)
        print("📈 TestForge 综合仪表盘")
        print("="*60)
        
        # 分析状态
        if self.analysis_results:
            print("\n✅ 代码分析已完成")
            total_funcs = sum(len(r.functions) for r in self.analysis_results)
            total_classes = sum(len(r.classes) for r in self.analysis_results)
            print(f"   - 发现 {total_funcs} 个函数")
            print(f"   - 发现 {total_classes} 个类")
        else:
            print("\n⚪ 代码分析: 未执行")
        
        # 生成状态
        if self.test_results:
            print("\n✅ 测试生成已完成")
            print(f"   - 生成 {self.test_results.total_generated} 个测试用例")
            print(f"   - 输出到: {self.test_results.test_file_path}")
        else:
            print("\n⚪ 测试生成: 未执行")
        
        # 评估状态
        if self.quality_results:
            print("\n✅ 质量评估已完成")
            score = self.quality_results.overall_score
            grade = "优秀" if score >= 90 else "良好" if score >= 75 else "及格" if score >= 60 else "需改进"
            print(f"   - 总体评分: {score}/100 ({grade})")
        else:
            print("\n⚪ 质量评估: 未执行")
        
        print("\n" + "-"*60)
        print("💡 快速操作")
        print("-"*60)
        print("   输入 'analyze' - 快速分析代码")
        print("   输入 'generate' - 快速生成测试")
        print("   输入 'assess' - 快速评估质量")
        print("   输入 'back' - 返回主菜单")
        
        # 快速命令
        cmd = input("\n🔶 请输入命令: ").strip().lower()
        
        if cmd == "analyze":
            self._do_analyze()
        elif cmd == "generate":
            self._do_generate()
        elif cmd == "assess":
            self._do_assess()
        elif cmd == "back":
            self._print_main_menu()
        else:
            print("⚠️ 未知命令")
            self._print_main_menu()
    
    def _show_help(self):
        """显示帮助信息"""
        help_text = """
╭─────────────────────────────────────────────────────────────────╮
│                        📖 帮助信息                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  TestForge 是一个轻量级的智能测试用例生成与质量评估工具            │
│                                                                 │
│  📌 主要功能:                                                   │
│                                                                 │
│  1️⃣ 分析代码                                                    │
│     - 自动扫描项目中的Python/JavaScript/TypeScript代码           │
│     - 识别可测试的函数、类和方法                                  │
│     - 计算代码复杂度                                             │
│                                                                 │
│  2️⃣ 生成测试                                                    │
│     - 基于分析结果自动生成测试用例                                │
│     - 支持 pytest 和 unittest 框架                               │
│     - 生成边界情况和参数化测试                                    │
│                                                                 │
│  3️⃣ 评估质量                                                    │
│     - 评估测试覆盖率                                             │
│     - 检查断言质量                                               │
│     - 分析代码结构和可维护性                                     │
│                                                                 │
│  📌 使用方式:                                                   │
│                                                                 │
│  命令行使用:                                                    │
│    testforge analyze ./src              # 分析代码              │
│    testforge generate ./src -o ./tests  # 生成测试              │
│    testforge assess ./tests             # 评估质量              │
│    testforge dashboard                  # 启动TUI               │
│                                                                 │
│  TUI界面使用:                                                   │
│    testforge                           # 启动交互界面          │
│                                                                 │
│  📌 特性:                                                       │
│                                                                 │
│  ✨ 零外部依赖 - 仅需Python 3.8+                                 │
│  🚀 快速生成 - 一键生成完整测试文件                              │
│  📊 质量评估 - 多维度评估测试质量                                │
│  🎨 友好界面 - 彩色TUI显示                                      │
│  🌐 多语言支持 - Python/JS/TS                                   │
│                                                                 │
╰─────────────────────────────────────────────────────────────────╯
"""
        print(help_text)
        
        input("\n按Enter键返回主菜单...")
        self._print_main_menu()
    
    def _quit(self):
        """退出程序"""
        print("\n" + "="*60)
        print("👋 感谢使用 TestForge!")
        print("   如有建议，欢迎反馈!")
        print("="*60)
        self.running = False


def launch_ui(path: str = ".", language: str = "auto"):
    """启动UI的便捷函数"""
    ui = TestForgeUI(path, language)
    ui.run()
