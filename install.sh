#!/bin/bash
# TestForge 一键安装脚本
# 自动安装依赖并配置环境

set -e

echo "========================================"
echo "🧪 TestForge 安装程序"
echo "========================================"

# 检查Python版本
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ 错误: 未找到Python"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    echo "❌ 错误: Python 3.8+ 必需，当前版本: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python版本检查通过: $PYTHON_VERSION"

# 创建虚拟环境（可选）
if [ "$1" == "--venv" ]; then
    echo "📦 创建虚拟环境..."
    $PYTHON_CMD -m venv venv
    source venv/bin/activate
    echo "✅ 虚拟环境已激活"
fi

# 安装TestForge
echo "📦 安装TestForge..."
$PYTHON_CMD -m pip install --upgrade pip
$PYTHON_CMD -m pip install -e .

# 安装开发依赖（可选）
if [ "$2" == "--dev" ]; then
    echo "📦 安装开发依赖..."
    $PYTHON_CMD -m pip install pytest pytest-cov black mypy
fi

# 配置Shell补全
echo "🔧 配置Shell命令补全..."

SHELL_RC=""
if [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
fi

if [ -n "$SHELL_RC" ]; then
    echo "export PATH=\"\$PATH:\$(pwd)\"" >> "$SHELL_RC"
    echo "✅ 已添加路径到 $SHELL_RC"
fi

# 创建别名（可选）
if [ "$1" == "--alias" ]; then
    echo "🔧 创建别名..."
    if [ -n "$BASH_VERSION" ]; then
        echo "alias tf='testforge'" >> "$HOME/.bashrc"
    elif [ -n "$ZSH_VERSION" ]; then
        echo "alias tf='testforge'" >> "$HOME/.zshrc"
    fi
    echo "✅ 别名 'tf' 已创建"
fi

echo ""
echo "========================================"
echo "✅ TestForge 安装完成!"
echo "========================================"
echo ""
echo "🚀 快速开始:"
echo "   testforge --help              # 查看帮助"
echo "   testforge dashboard           # 启动TUI界面"
echo "   testforge analyze ./src        # 分析代码"
echo ""
echo "💡 提示: 运行 'tf' 如果你使用了 --alias 选项"
echo ""
