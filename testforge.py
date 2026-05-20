#!/usr/bin/env python3
"""
TestForge - 智能测试用例生成与质量评估引擎
Lightweight Intelligent Test Case Generation & Quality Assessment Engine

Author: GitStQ
License: MIT
"""

import sys
import argparse
from pathlib import Path
from src.analyzer import CodeAnalyzer
from src.generator import TestGenerator
from src.quality import QualityAssessor
from src.tui import TestForgeUI

__version__ = "1.0.0"
__author__ = "GitStQ"


def main():
    """Main entry point for TestForge CLI"""
    parser = argparse.ArgumentParser(
        description="🧪 TestForge - 智能测试用例生成与质量评估引擎",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  testforge analyze ./src              # 分析代码结构
  testforge generate ./src -o ./tests   # 生成测试用例
  testforge assess ./tests              # 评估测试质量
  testforge dashboard ./src             # 启动TUI仪表盘
        """
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"TestForge v{__version__}"
    )
    
    parser.add_argument(
        "--lang",
        choices=["python", "javascript", "typescript", "auto"],
        default="auto",
        help="指定编程语言 (默认: auto)"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # analyze command
    analyze_parser = subparsers.add_parser("analyze", help="分析代码结构")
    analyze_parser.add_argument("path", help="代码路径")
    analyze_parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    
    # generate command
    generate_parser = subparsers.add_parser("generate", help="生成测试用例")
    generate_parser.add_argument("path", help="代码路径")
    generate_parser.add_argument("--output", "-o", default="./tests", help="输出目录")
    generate_parser.add_argument("--framework", "-f", 
                                  choices=["pytest", "unittest", "jest", "vitest"],
                                  default="pytest",
                                  help="测试框架")
    generate_parser.add_argument("--coverage", "-c", type=int, default=80, 
                                  help="目标覆盖率")
    
    # assess command
    assess_parser = subparsers.add_parser("assess", help="评估测试质量")
    assess_parser.add_argument("path", help="测试文件路径")
    assess_parser.add_argument("--format", choices=["json", "text"], default="text")
    
    # dashboard command
    dashboard_parser = subparsers.add_parser("dashboard", help="启动TUI仪表盘")
    dashboard_parser.add_argument("path", nargs="?", default=".", help="项目路径")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    try:
        if args.command == "analyze":
            print(f"🔍 正在分析代码: {args.path}")
            analyzer = CodeAnalyzer(args.path, args.lang)
            results = analyzer.analyze()
            analyzer.display_results(results, args.verbose)
            
        elif args.command == "generate":
            print(f"⚙️ 正在生成测试用例: {args.path}")
            generator = TestGenerator(args.path, args.lang, args.framework)
            results = generator.generate(args.output, args.coverage)
            generator.display_summary(results)
            
        elif args.command == "assess":
            print(f"📊 正在评估测试质量: {args.path}")
            assessor = QualityAssessor(args.path)
            results = assessor.assess()
            assessor.display_report(results, args.format)
            
        elif args.command == "dashboard":
            print(f"📈 启动TUI仪表盘: {args.path}")
            ui = TestForgeUI(args.path, args.lang)
            ui.run()
            
        return 0
        
    except KeyboardInterrupt:
        print("\n\n👋 已取消操作")
        return 130
    except Exception as e:
        print(f"\n❌ 错误: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
