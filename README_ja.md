# 🧪 TestForge

> 軽量インテリジェントテストケース生成・品質評価エンジン | Lightweight Intelligent Test Case Generation & Quality Assessment Engine

[简体中文](./README.md) | [繁體中文](./README_zh-TW.md) | [English](./README_en.md) | [日本語](./README_ja.md) | [한국어](./README_ko.md)

---

## 🎯 プロジェクト紹介

TestForgeは、開発者向けに設計された**軽量でゼロ依存**のインテリジェントテストケース生成・品質評価ツールです。コード構造を自動的に分析し、高品質のテストケースを生成し、多面的なテスト品質評価レポートを提供します。

### ✨ コアバリュー

- 🔍 **インテリジェント分析** - AST技術による深いコード解析、テスト可能なユニットの正確な識別
- ⚡ **ワンスクリプト生成** - pytest/unittest仕様に準拠したテストコードを自動生成
- 📊 **品質評価** - テストカバレッジ、アサーション品質、コード構造の多面的評価
- 🎨 **使いやすいインターフェース** - カラフルなTUIダッシュボード、直感的で便利な操作
- 🌐 **多言語サポート** - Python/JavaScript/TypeScriptに対応
- 🔒 **ゼロ依存設計** - Python 3.8+のみ、必要ありません

### 🚀 自社開発の差別化ポイント

1. **より軽量** - 既存のテストツールと比較して、より小さく、より高速
2. **よりスマート** - 組み込みのコード複雑度分析を優先的テストに実装
3. **より包括的** - テスト生成だけでなく、品質評価と改善提案を提供
4. **より使いやすい** - TUIインターフェースをサポート、一問一答式操作

---

## 📦 コア機能

### 1️⃣ コードアナライザー (Code Analyzer)

- 🔬 ASTベースの深いコード解析
- 📈 関数の複雑さを自動計算
- 🎯 テスト可能な関数、クラス、メソッドを識別
- 📋 詳細なコード構造レポートを生成

### 2️⃣ テストジェネレーター (Test Generator)

- 🧬 ユニットテストケースの自動生成
- 📝 pytestとunittestフレームワークをサポート
- 🎨 パラメータ化されたテストケースを生成
- ⚡ 境界値のケースを自動処理

### 3️⃣ 品質アセスサー (Quality Assessor)

- 📊 7次元品質評価システム
- 🎯 カバレッジスコアリング
- 💡 インテリジェントな改善提案
- 📈 履歴トレンド追跡

### 4️⃣ TUIダッシュボード (Dashboard)

- 🎨 カラフルなターミナルインターフェース
- 📊 リアルタイムデータ可視化
- ⌨️ キーボードナビゲーション操作
- 📈 統合分析ビュー

---

## 🚀 クイックスタート

### 📋 環境要件

- Python 3.8 以上
- 対応OS: Windows / macOS / Linux

### ⚡ インストール方法

#### 方法1: pipインストール（推奨）

```bash
pip install testforge
```

#### 方法2: ソースからインストール

```bash
git clone https://github.com/gitstq/TestForge.git
cd TestForge
pip install -e .
```

#### 方法3: ワンスクリプトインストール

```bash
curl -fsSL https://raw.githubusercontent.com/gitstq/TestForge/main/install.sh | bash
```

### 🎯 クイック使用方法

#### コマンドライン使用方法

```bash
# コード構造を分析
testforge analyze ./src

# テストケースを生成
testforge generate ./src -o ./tests

# テスト品質を評価
testforge assess ./tests

# TUIインターフェースを起動
testforge dashboard
```

#### TUIインターフェース使用方法

```bash
# インタラクティブインターフェースを起動
testforge

# 操作を選択:
# 1. コード分析
# 2. テスト生成
# 3. 品質評価
# 4. ダッシュボード
# 5. ヘルプ
# 6. 終了
```

---

## 📖 詳細な使用方法

### コード分析

```bash
# プロジェクト全体を分析
testforge analyze ./my_project

# 特定のファイルを分析
testforge analyze ./my_project/utils.py

# 詳細出力モード
testforge analyze ./src -v

# 言語を指定
testforge analyze ./src --lang python
```

### テスト生成

```bash
# pytestフレームワークでテストを生成
testforge generate ./src -o ./tests --framework pytest

# unittestフレームワークでテストを生成
testforge generate ./src -o ./tests --framework unittest

# 目標カバレッジを設定
testforge generate ./src -o ./tests --coverage 90
```

### 品質評価

```bash
# テストファイルの品質を評価
testforge assess ./tests/test_math.py

# テストディレクトリを評価
testforge assess ./tests

# JSON形式で出力
testforge assess ./tests --format json
```

---

## 💡 設計思想

### 🎯 設計理念

1. **ミニマリズム** - 外部依存ゼロ、使用门槛降低
2. **開発者フレンドリー** - 明確な出力、使いやすい操作
3. **実利主義** - 実際の問題を解決し、実用的な価値を提供
4. **継続的改善** - コミュニティのフィードバックを傾聴し、継続的に最適化

### 🔧 技術選択

- **言語**: Python 3.8+（成熟したエコシステム、拡張しやすい）
- **コード分析**: Python ASTモジュール（標準ライブラリ、インストール不要）
- **インターフェース**: ターミナルネイティブUI（グラフィックライブラリ不要）
- **テストフレームワーク**: pytest/unittest（業界標準）

---

## 🤝 コントリビューション

IssueとPull Requestを歓迎します！

### 🐛 バグ報告

[GitHub Issues](https://github.com/gitstq/TestForge/issues)で詳細に説明してください：
1. 再現手順
2. 期待される動作
3. 実際の動作
4. 環境情報

### 💻 コード貢献

1. このリポジトリをFork
2. フィーチャーブランチを作成 (`git checkout -b feature/AmazingFeature`)
3. 変更をコミット (`git commit -m 'Add some AmazingFeature'`)
4. ブランチにプッシュ (`git push origin feature/AmazingFeature`)
5. Pull Requestを作成

---

## 📄 ライセンス

このプロジェクトは **MIT License** を使用しています。

---

<div align="center">

**このプロジェクトが役立った場合は、⭐ Starを付けてください！**

Made with ❤️ by [GitStQ](https://github.com/gitstq)

</div>
