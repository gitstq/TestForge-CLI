# 🧪 TestForge

> 輕量級智慧測試用例生成與品質評估引擎 | Lightweight Intelligent Test Case Generation & Quality Assessment Engine

[简体中文](./README.md) | [繁體中文](./README_zh-TW.md) | [English](./README_en.md) | [日本語](./README_ja.md) | [한국어](./README_ko.md)

---

## 🎯 專案介紹

TestForge 是一款專為開發者設計的**輕量級、零依賴**智慧測試用例生成與品質評估工具。它能夠自動分析程式碼結構，生成高質量的測試用例，並提供多維度的測試品質評估報告。

### ✨ 核心價值

- 🔍 **智慧分析** - 基於AST技術深度解析程式碼結構，精準識別可測試單元
- ⚡ **一鍵生成** - 自動生成符合pytest/unittest規範的測試程式碼
- 📊 **品質評估** - 多維度評估測試覆蓋率、斷言品質、程式碼結構
- 🎨 **友好介面** - 彩色TUI儀表板，操作直觀便捷
- 🌐 **多語言支援** - 支援Python/JavaScript/TypeScript
- 🔒 **零依賴設計** - 僅需Python 3.8+，無需安裝任何第三方套件

### 🚀 自研差異化亮點

1. **更輕量** - 相比現有測試工具，TestForge體積更小、啟動更快
2. **更智慧** - 內建程式碼複雜度分析，優先測試關鍵路徑
3. **更全面** - 不僅生成測試，還提供品質評估和改進建議
4. **更易用** - 支援TUI互動介面，一問一答式操作

---

## 📦 核心功能

### 1️⃣ 程式碼分析器 (Code Analyzer)

- 🔬 基於AST的深度程式碼解析
- 📈 自動計算函數複雜度
- 🎯 識別可測試的函數、類別、方法
- 📋 生成詳細的程式碼結構報告

### 2️⃣ 測試生成器 (Test Generator)

- 🧬 自動生成單元測試用例
- 📝 支援pytest和unittest框架
- 🎨 生成參數化測試用例
- ⚡ 自動處理邊界情況

### 3️⃣ 品質評估器 (Quality Assessor)

- 📊 七維度品質評估體系
- 🎯 覆蓋率評分
- 💡 智慧改進建議
- 📈 歷史趨勢追蹤

### 4️⃣ TUI儀表板 (Dashboard)

- 🎨 彩色終端介面
- 📊 即時資料視覺化
- ⌨️ 鍵盤導航操作
- 📈 綜合分析視圖

---

## 🚀 快速開始

### 📋 環境需求

- Python 3.8 或更高版本
- 支援作業系統: Windows / macOS / Linux

### ⚡ 安裝方式

#### 方式一：pip安裝 (推薦)

```bash
pip install testforge
```

#### 方式二：從原始碼安裝

```bash
git clone https://github.com/gitstq/TestForge.git
cd TestForge
pip install -e .
```

#### 方式三：一鍵安裝腳本

```bash
curl -fsSL https://raw.githubusercontent.com/gitstq/TestForge/main/install.sh | bash
```

### 🎯 快速使用

#### 命令列使用

```bash
# 分析程式碼結構
testforge analyze ./src

# 生成測試用例
testforge generate ./src -o ./tests

# 評估測試品質
testforge assess ./tests

# 啟動TUI介面
testforge dashboard
```

#### TUI介面使用

```bash
# 啟動互動式介面
testforge

# 選擇操作:
# 1. 分析程式碼
# 2. 生成測試
# 3. 評估品質
# 4. 綜合儀表板
# 5. 幫助資訊
# 6. 退出程式
```

---

## 📖 詳細使用指南

### 分析程式碼

```bash
# 分析整個專案
testforge analyze ./my_project

# 分析特定檔案
testforge analyze ./my_project/utils.py

# 詳細輸出模式
testforge analyze ./src -v

# 指定語言
testforge analyze ./src --lang python
```

### 生成測試

```bash
# 使用pytest框架生成測試
testforge generate ./src -o ./tests --framework pytest

# 使用unittest框架生成測試
testforge generate ./src -o ./tests --framework unittest

# 設定目標覆蓋率
testforge generate ./src -o ./tests --coverage 90
```

### 評估品質

```bash
# 評估測試檔案品質
testforge assess ./tests/test_math.py

# 評估測試目錄
testforge assess ./tests

# 輸出JSON格式
testforge assess ./tests --format json
```

---

## 💡 設計思路

### 🎯 設計理念

1. **極簡主義** - 零外部依賴，降低使用門檻
2. **開發者友好** - 清晰的輸出，友好的互動
3. **實用主義** - 解決真實問題，提供實際價值
4. **持續迭代** - 傾聽社區回饋，不斷優化改進

### 🔧 技術選型

- **語言**: Python 3.8+ (生態成熟，易於擴展)
- **程式碼分析**: Python AST模組 (標準庫，無需安裝)
- **介面**: 終端原生UI (無需圖形庫依賴)
- **測試框架**: pytest/unittest (業界標準)

---

## 🤝 貢獻指南

歡迎提交Issue和Pull Request！

### 🐛 錯誤回報

請在 [GitHub Issues](https://github.com/gitstq/TestForge/issues) 中詳細描述：
1. 重現步驟
2. 預期行為
3. 實際行為
4. 環境資訊

### 💻 程式碼貢獻

1. Fork本倉庫
2. 建立特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 建立Pull Request

---

## 📄 開源協議

本專案採用 **MIT License** 開源協議。

---

<div align="center">

**如果這個專案對您有幫助，請給個 ⭐ Star！**

Made with ❤️ by [GitStQ](https://github.com/gitstq)

</div>
