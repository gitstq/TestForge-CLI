# 🧪 TestForge

> Lightweight Intelligent Test Case Generation & Quality Assessment Engine

[简体中文](./README.md) | [繁體中文](./README_zh-TW.md) | [English](./README_en.md) | [日本語](./README_ja.md) | [한국어](./README_ko.md)

---

## 🎯 Project Introduction

TestForge is a **lightweight, zero-dependency** intelligent test case generation and quality assessment tool designed specifically for developers. It can automatically analyze code structure, generate high-quality test cases, and provide multi-dimensional test quality assessment reports.

### ✨ Core Value

- 🔍 **Intelligent Analysis** - Deep code parsing based on AST technology, accurately identifying testable units
- ⚡ **One-Click Generation** - Automatically generate test code conforming to pytest/unittest specifications
- 📊 **Quality Assessment** - Multi-dimensional evaluation of test coverage, assertion quality, and code structure
- 🎨 **User-Friendly Interface** - Colorful TUI dashboard, intuitive and convenient operation
- 🌐 **Multi-Language Support** - Supports Python/JavaScript/TypeScript
- 🔒 **Zero-Dependency Design** - Only requires Python 3.8+, no third-party packages needed

### 🚀 Self-Developed Differentiation Highlights

1. **Lighter** - Smaller size and faster startup compared to existing testing tools
2. **Smarter** - Built-in code complexity analysis, prioritizing critical paths for testing
3. **More Comprehensive** - Not only generates tests, but also provides quality assessment and improvement suggestions
4. **Easier to Use** - Supports TUI interactive interface, one-question-one-answer operation

---

## 📦 Core Features

### 1️⃣ Code Analyzer

- 🔬 Deep code parsing based on AST
- 📈 Automatic function complexity calculation
- 🎯 Identification of testable functions, classes, and methods
- 📋 Detailed code structure reports

### 2️⃣ Test Generator

- 🧬 Automatic unit test case generation
- 📝 Support for pytest and unittest frameworks
- 🎨 Parameterized test case generation
- ⚡ Automatic boundary case handling

### 3️⃣ Quality Assessor

- 📊 Seven-dimensional quality assessment system
- 🎯 Coverage scoring
- 💡 Smart improvement suggestions
- 📈 Historical trend tracking

### 4️⃣ TUI Dashboard

- 🎨 Colorful terminal interface
- 📊 Real-time data visualization
- ⌨️ Keyboard navigation
- 📈 Comprehensive analysis view

---

## 🚀 Quick Start

### 📋 Requirements

- Python 3.8 or higher
- Supported OS: Windows / macOS / Linux

### ⚡ Installation

#### Method 1: pip install (Recommended)

```bash
pip install testforge
```

#### Method 2: From Source

```bash
git clone https://github.com/gitstq/TestForge.git
cd TestForge
pip install -e .
```

#### Method 3: One-Click Installation Script

```bash
curl -fsSL https://raw.githubusercontent.com/gitstq/TestForge/main/install.sh | bash
```

### 🎯 Quick Usage

#### Command Line Usage

```bash
# Analyze code structure
testforge analyze ./src

# Generate test cases
testforge generate ./src -o ./tests

# Assess test quality
testforge assess ./tests

# Launch TUI interface
testforge dashboard
```

#### TUI Interface Usage

```bash
# Launch interactive interface
testforge

# Select operation:
# 1. Analyze code
# 2. Generate tests
# 3. Assess quality
# 4. Dashboard
# 5. Help
# 6. Quit
```

---

## 📖 Detailed Usage Guide

### Analyze Code

```bash
# Analyze entire project
testforge analyze ./my_project

# Analyze specific file
testforge analyze ./my_project/utils.py

# Verbose output mode
testforge analyze ./src -v

# Specify language
testforge analyze ./src --lang python
```

### Generate Tests

```bash
# Generate tests with pytest framework
testforge generate ./src -o ./tests --framework pytest

# Generate tests with unittest framework
testforge generate ./src -o ./tests --framework unittest

# Set target coverage
testforge generate ./src -o ./tests --coverage 90
```

### Assess Quality

```bash
# Assess test file quality
testforge assess ./tests/test_math.py

# Assess test directory
testforge assess ./tests

# Output JSON format
testforge assess ./tests --format json
```

---

## 💡 Design Philosophy

### 🎯 Design Principles

1. **Minimalism** - Zero external dependencies, lower barrier to use
2. **Developer-Friendly** - Clear output, friendly interaction
3. **Pragmatism** - Solve real problems, provide practical value
4. **Continuous Iteration** - Listen to community feedback, continuously optimize and improve

### 🔧 Technical Choices

- **Language**: Python 3.8+ (mature ecosystem, easy to extend)
- **Code Analysis**: Python AST module (standard library, no installation needed)
- **Interface**: Terminal native UI (no graphics library dependencies)
- **Test Framework**: pytest/unittest (industry standard)

---

## 🤝 Contributing

Contributions are welcome! Please submit Issues and Pull Requests.

### 🐛 Bug Reports

Please describe in detail in [GitHub Issues](https://github.com/gitstq/TestForge/issues):
1. Reproduction steps
2. Expected behavior
3. Actual behavior
4. Environment information

### 💻 Code Contribution

1. Fork this repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Create Pull Request

---

## 📄 License

This project uses **MIT License**.

```
MIT License

Copyright (c) 2025 GitStQ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

**If this project helps you, please give it a ⭐ Star!**

Made with ❤️ by [GitStQ](https://github.com/gitstq)

</div>
