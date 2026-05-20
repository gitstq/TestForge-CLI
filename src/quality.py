#!/usr/bin/env python3
"""
测试质量评估器模块 - Test Quality Assessor Module
评估测试用例的质量、覆盖率和可靠性
"""

import ast
import json
import re
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class QualityMetric:
    """质量指标数据结构"""
    name: str
    score: float
    max_score: float
    description: str
    suggestions: List[str] = field(default_factory=list)


@dataclass
class QualityReport:
    """质量评估报告数据结构"""
    file_path: str
    timestamp: str
    overall_score: float
    metrics: List[QualityMetric]
    strengths: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


class QualityAssessor:
    """测试质量评估器"""
    
    def __init__(self, test_path: str):
        self.test_path = Path(test_path)
        self.max_scores = {
            "coverage": 25,
            "assertions": 20,
            "edge_cases": 15,
            "naming": 10,
            "documentation": 10,
            "structure": 10,
            "maintainability": 10
        }
    
    def assess(self) -> QualityReport:
        """执行质量评估"""
        if not self.test_path.exists():
            raise FileNotFoundError(f"测试文件不存在: {self.test_path}")
        
        if self.test_path.is_file():
            return self._assess_file(self.test_path)
        else:
            return self._assess_directory()
    
    def _assess_file(self, file_path: Path) -> QualityReport:
        """评估单个测试文件"""
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        metrics = []
        
        # 覆盖率评分
        coverage_metric = self._evaluate_coverage(content)
        metrics.append(coverage_metric)
        
        # 断言评分
        assertion_metric = self._evaluate_assertions(content)
        metrics.append(assertion_metric)
        
        # 边界情况评分
        edge_metric = self._evaluate_edge_cases(content)
        metrics.append(edge_metric)
        
        # 命名规范评分
        naming_metric = self._evaluate_naming(content)
        metrics.append(naming_metric)
        
        # 文档评分
        doc_metric = self._evaluate_documentation(content)
        metrics.append(doc_metric)
        
        # 结构评分
        structure_metric = self._evaluate_structure(content)
        metrics.append(structure_metric)
        
        # 可维护性评分
        maintain_metric = self._evaluate_maintainability(content)
        metrics.append(maintain_metric)
        
        # 计算总分
        total_score = sum(m.score for m in metrics)
        max_total = sum(m.max_score for m in metrics)
        overall_score = round((total_score / max_total) * 100, 2)
        
        # 分析优劣势
        strengths = [m.name for m in metrics if m.score >= m.max_score * 0.8]
        weaknesses = [m.name for m in metrics if m.score < m.max_score * 0.5]
        
        # 收集建议
        recommendations = []
        for metric in metrics:
            recommendations.extend(metric.suggestions)
        
        return QualityReport(
            file_path=str(file_path),
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            overall_score=overall_score,
            metrics=metrics,
            strengths=strengths,
            weaknesses=weaknesses,
            recommendations=recommendations[:5]  # 限制建议数量
        )
    
    def _assess_directory(self) -> QualityReport:
        """评估测试目录"""
        test_files = list(self.test_path.rglob("test_*.py"))
        
        if not test_files:
            raise ValueError(f"目录中未找到测试文件: {self.test_path}")
        
        # 汇总评估
        all_metrics = []
        
        for test_file in test_files:
            try:
                report = self._assess_file(test_file)
                all_metrics.extend(report.metrics)
            except Exception as e:
                print(f"⚠️ 评估文件失败 {test_file}: {e}")
        
        # 计算平均值
        averaged_metrics = []
        metric_names = set(m.name for m in all_metrics)
        
        for name in metric_names:
            matching = [m for m in all_metrics if m.name == name]
            avg_score = sum(m.score for m in matching) / len(matching)
            
            # 合并建议
            all_suggestions = []
            for m in matching:
                all_suggestions.extend(m.suggestions)
            
            # 去重
            seen = set()
            unique_suggestions = []
            for s in all_suggestions:
                if s not in seen:
                    seen.add(s)
                    unique_suggestions.append(s)
            
            # 使用第一个匹配项作为模板
            template = matching[0]
            averaged_metrics.append(QualityMetric(
                name=name,
                score=avg_score,
                max_score=template.max_score,
                description=template.description,
                suggestions=unique_suggestions[:3]
            ))
        
        total_score = sum(m.score for m in averaged_metrics)
        max_total = sum(m.max_score for m in averaged_metrics)
        overall_score = round((total_score / max_total) * 100, 2)
        
        return QualityReport(
            file_path=str(self.test_path),
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            overall_score=overall_score,
            metrics=averaged_metrics,
            strengths=[m.name for m in averaged_metrics if m.score >= m.max_score * 0.8],
            weaknesses=[m.name for m in averaged_metrics if m.score < m.max_score * 0.5],
            recommendations=[s for m in averaged_metrics for s in m.suggestions[:2]]
        )
    
    def _evaluate_coverage(self, content: str) -> QualityMetric:
        """评估测试覆盖率"""
        score = 50  # 基础分
        
        # 检查是否有fixture/setup
        if "setup" in content.lower() or "fixture" in content.lower():
            score += 20
        
        # 检查是否有teardown/cleanup
        if "teardown" in content.lower() or "cleanup" in content.lower():
            score += 15
        
        # 检查参数化测试
        if "parametrize" in content or "parameterized" in content:
            score += 15
        
        return QualityMetric(
            name="coverage",
            score=min(score, self.max_scores["coverage"]),
            max_score=self.max_scores["coverage"],
            description="测试覆盖率评估",
            suggestions=["添加更多测试用例覆盖不同场景" if score < 50 else "覆盖率良好"]
        )
    
    def _evaluate_assertions(self, content: str) -> QualityMetric:
        """评估断言质量"""
        score = 30
        
        # 计算断言数量
        assert_count = len(re.findall(r'\bassert\b', content))
        
        # 每个断言加分
        score += min(assert_count * 5, 40)
        
        # 检查不同类型的断言
        has_negative_asserts = "assertNot" in content or "assertFalse" in content
        if has_negative_asserts:
            score += 10
        
        # 检查异常测试
        if "raises" in content or "expect" in content.lower():
            score += 10
        
        suggestions = []
        if assert_count < 3:
            suggestions.append("增加断言数量，确保每个测试都有明确的验证")
        if not has_negative_asserts:
            suggestions.append("添加负面测试用例（assertNotEqual, assertFalse等）")
        
        return QualityMetric(
            name="assertions",
            score=min(score, self.max_scores["assertions"]),
            max_score=self.max_scores["assertions"],
            description="断言质量评估",
            suggestions=suggestions
        )
    
    def _evaluate_edge_cases(self, content: str) -> QualityMetric:
        """评估边界情况测试"""
        score = 0
        
        # 检查常见边界情况关键词
        edge_keywords = [
            "empty", "none", "null", "zero",
            "boundary", "edge", "corner",
            "max", "min", "limit",
            "large", "small"
        ]
        
        for keyword in edge_keywords:
            if keyword in content.lower():
                score += 3
        
        # 检查None/空值测试
        if "None" in content or "null" in content.lower():
            score += 5
        
        # 检查异常值测试
        if "error" in content.lower() or "exception" in content.lower():
            score += 5
        
        suggestions = []
        if score < 10:
            suggestions.append("添加边界情况测试（空值、最大值、异常输入等）")
        
        return QualityMetric(
            name="edge_cases",
            score=min(score, self.max_scores["edge_cases"]),
            max_score=self.max_scores["edge_cases"],
            description="边界情况测试评估",
            suggestions=suggestions
        )
    
    def _evaluate_naming(self, content: str) -> QualityMetric:
        """评估命名规范"""
        score = self.max_scores["naming"]
        
        # 检查测试命名是否符合规范
        test_pattern = r'def\s+(test_\w+)'
        tests = re.findall(test_pattern, content)
        
        non_compliant = [t for t in tests if not t.startswith("test_")]
        if non_compliant:
            score -= len(non_compliant) * 2
        
        # 检查驼峰命名
        camel_case = [t for t in tests if any(c.isupper() for c in t[5:])]
        if camel_case:
            score -= 2
        
        suggestions = []
        if non_compliant:
            suggestions.append("测试函数应使用snake_case命名，以test_开头")
        
        return QualityMetric(
            name="naming",
            score=max(0, score),
            max_score=self.max_scores["naming"],
            description="命名规范评估",
            suggestions=suggestions
        )
    
    def _evaluate_documentation(self, content: str) -> QualityMetric:
        """评估文档完整性"""
        score = 0
        
        # 检查模块docstring
        if content.startswith('"""') or content.startswith("'''"):
            score += 3
        
        # 计算docstring数量
        docstring_count = len(re.findall(r'""".*?"""', content, re.DOTALL))
        docstring_count += len(re.findall(r"'''.*?'''", content, re.DOTALL))
        
        score += min(docstring_count * 2, 5)
        
        # 检查函数级别的文档
        func_with_docs = len(re.findall(r'def\s+\w+.*?:\s*["\']""".*?"""', content, re.DOTALL))
        if func_with_docs > 0:
            score += min(func_with_docs * 1, 5)
        
        suggestions = []
        if docstring_count < 3:
            suggestions.append("为测试模块和测试函数添加docstring说明")
        
        return QualityMetric(
            name="documentation",
            score=min(score, self.max_scores["documentation"]),
            max_score=self.max_scores["documentation"],
            description="文档完整性评估",
            suggestions=suggestions
        )
    
    def _evaluate_structure(self, content: str) -> QualityMetric:
        """评估代码结构"""
        score = self.max_scores["structure"]
        
        # 检查代码行数
        lines = content.split('\n')
        code_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')]
        
        # 过长或过短的测试函数
        func_blocks = re.findall(r'def\s+\w+.*?(?=\ndef|\nclass|\Z)', content, re.DOTALL)
        
        too_long = [f for f in func_blocks if len(f.split('\n')) > 50]
        too_short = [f for f in func_blocks if 0 < len(f.split('\n')) < 3]
        
        score -= len(too_long) * 2
        score -= len(too_short) * 1
        
        suggestions = []
        if too_long:
            suggestions.append("将过长的测试函数拆分为多个小函数")
        if too_short:
            suggestions.append("考虑合并过短且相关的测试函数")
        
        return QualityMetric(
            name="structure",
            score=max(0, score),
            max_score=self.max_scores["structure"],
            description="代码结构评估",
            suggestions=suggestions
        )
    
    def _evaluate_maintainability(self, content: str) -> QualityMetric:
        """评估可维护性"""
        score = self.max_scores["maintainability"]
        
        # 检查硬编码
        magic_numbers = re.findall(r'\b\d{2,}\b', content)
        hard_coded = [n for n in magic_numbers if int(n) not in [100, 200, 404, 500]]  # 常见状态码除外
        
        score -= min(len(hard_coded) * 0.5, 5)
        
        # 检查重复代码
        lines = [l.strip() for l in content.split('\n') if l.strip()]
        unique_lines = set(lines)
        
        if len(lines) > 20:  # 只有足够长的文件才检查
            repetition_ratio = 1 - (len(unique_lines) / len(lines))
            if repetition_ratio > 0.3:
                score -= 5
        
        # 检查TODO/FIXME
        if "TODO" in content or "FIXME" in content:
            score -= 2
        
        suggestions = []
        if hard_coded:
            suggestions.append("使用常量替代硬编码的数字")
        if "TODO" in content or "FIXME" in content:
            suggestions.append("尽快处理代码中的TODO和FIXME标记")
        
        return QualityMetric(
            name="maintainability",
            score=max(0, score),
            max_score=self.max_scores["maintainability"],
            description="可维护性评估",
            suggestions=suggestions
        )
    
    def display_report(self, report: QualityReport, format: str = "text"):
        """显示评估报告"""
        if format == "json":
            self._display_json_report(report)
        else:
            self._display_text_report(report)
    
    def _display_text_report(self, report: QualityReport):
        """以文本格式显示报告"""
        print("\n" + "="*70)
        print("📊 TestForge 测试质量评估报告")
        print("="*70)
        print(f"📁 评估文件: {report.file_path}")
        print(f"⏰ 评估时间: {report.timestamp}")
        
        print("\n" + "-"*70)
        print("🎯 总体评分")
        print("-"*70)
        
        # 评分条
        score_bar = self._make_score_bar(report.overall_score)
        print(score_bar)
        print(f"   总分: {report.overall_score}/100")
        
        # 等级评定
        if report.overall_score >= 90:
            grade = "🟢 优秀 (A)"
        elif report.overall_score >= 75:
            grade = "🟢 良好 (B)"
        elif report.overall_score >= 60:
            grade = "🟡 及格 (C)"
        elif report.overall_score >= 40:
            grade = "🟠 需改进 (D)"
        else:
            grade = "🔴 不合格 (F)"
        
        print(f"   等级: {grade}")
        
        print("\n" + "-"*70)
        print("📈 详细指标")
        print("-"*70)
        
        for metric in report.metrics:
            metric_bar = self._make_score_bar((metric.score / metric.max_score) * 100, width=30)
            percentage = round((metric.score / metric.max_score) * 100, 1)
            
            print(f"\n   📌 {metric.name.upper()}")
            print(f"      {metric_bar} {percentage}%")
            print(f"      说明: {metric.description}")
            
            if metric.suggestions:
                print(f"      💡 建议:")
                for suggestion in metric.suggestions[:2]:
                    print(f"         - {suggestion}")
        
        if report.strengths:
            print("\n" + "-"*70)
            print("💪 优势领域")
            print("-"*70)
            for strength in report.strengths:
                print(f"   ✅ {strength}")
        
        if report.weaknesses:
            print("\n" + "-"*70)
            print("⚠️  需要改进")
            print("-"*70)
            for weakness in report.weaknesses:
                print(f"   ❌ {weakness}")
        
        if report.recommendations:
            print("\n" + "-"*70)
            print("🔧 改进建议")
            print("-"*70)
            for i, rec in enumerate(report.recommendations[:5], 1):
                print(f"   {i}. {rec}")
        
        print("\n" + "="*70)
        print("✨ 评估完成!")
        print("="*70)
    
    def _display_json_report(self, report: QualityReport):
        """以JSON格式显示报告"""
        output = {
            "file_path": report.file_path,
            "timestamp": report.timestamp,
            "overall_score": report.overall_score,
            "metrics": [
                {
                    "name": m.name,
                    "score": m.score,
                    "max_score": m.max_score,
                    "percentage": round((m.score / m.max_score) * 100, 2),
                    "description": m.description,
                    "suggestions": m.suggestions
                }
                for m in report.metrics
            ],
            "strengths": report.strengths,
            "weaknesses": report.weaknesses,
            "recommendations": report.recommendations
        }
        
        print(json.dumps(output, indent=2, ensure_ascii=False))
    
    def _make_score_bar(self, score: float, width: int = 40) -> str:
        """生成评分条"""
        filled = int(width * score / 100)
        empty = width - filled
        
        if score >= 90:
            color = "🟢"
        elif score >= 70:
            color = "🟡"
        elif score >= 50:
            color = "🟠"
        else:
            color = "🔴"
        
        bar = f"[{color}{'█' * filled}{'░' * empty}]"
        return bar
