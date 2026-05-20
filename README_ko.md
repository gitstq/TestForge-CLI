# 🧪 TestForge

> 경량 지능형 테스트 케이스 생성 및 품질 평가 엔진 | Lightweight Intelligent Test Case Generation & Quality Assessment Engine

[简体中文](./README.md) | [繁體中文](./README_zh-TW.md) | [English](./README_en.md) | [日本語](./README_ja.md) | [한국어](./README_ko.md)

---

## 🎯 프로젝트 소개

TestForge는 개발자를 위해 설계된**경량, 제로 의존성** 지능형 테스트 케이스 생성 및 품질 평가 도구입니다. 코드 구조를 자동으로 분석하고 고품질 테스트 케이스를 생성하며 다차원적인 테스트 품질 평가 보고서를 제공합니다.

### ✨ 핵심 가치

- 🔍 **지능형 분석** - AST 기술 기반 심층 코드 분석, 테스트 가능한 유닛 정확한 식별
- ⚡ **원클릭 생성** - pytest/unittest 사양에 맞는 테스트 코드 자동 생성
- 📊 **품질 평가** - 테스트 커버리지, 어설션 품질, 코드 구조 다차원 평가
- 🎨 **친숙한 인터페이스** - 컬러 TUI 대시보드, 직관적이며 편리한 조작
- 🌐 **다국어 지원** - Python/JavaScript/TypeScript 지원
- 🔒 **제로 의존성 설계** - Python 3.8+만 필요, 별도 패키지 설치 불필요

### 🚀 자사 개발 차별화 포인트

1. **더 경량** - 기존 테스트 도구 대비 더 작고 더 빠른 시작
2. **더 지능형** - 내장 코드 복잡도 분석으로 중요 경로 우선 테스트
3. **더 포괄적** - 테스트 생성뿐 아니라 품질 평가 및 개선 제안 제공
4. **더 쉬운 사용** - TUI 인터랙티브 인터페이스 지원, 일대일 답변식 조작

---

## 📦 핵심 기능

### 1️⃣ 코드 분석기 (Code Analyzer)

- 🔬 AST 기반 심층 코드 분석
- 📈 함수 복잡도 자동 계산
- 🎯 테스트 가능한 함수, 클래스, 메서드 식별
- 📋 상세 코드 구조 보고서 생성

### 2️⃣ 테스트 생성기 (Test Generator)

- 🧬 단위 테스트 케이스 자동 생성
- 📝 pytest 및 unittest 프레임워크 지원
- 🎨 파라미터화된 테스트 케이스 생성
- ⚡ 경계값 케이스 자동 처리

### 3️⃣ 품질 평가기 (Quality Assessor)

- 📊 7차원 품질 평가 시스템
- 🎯 커버리지 점수 매기기
- 💡 지능형 개선 제안
- 📈 이력 추세 추적

### 4️⃣ TUI 대시보드 (Dashboard)

- 🎨 컬러 터미널 인터페이스
- 📊 실시간 데이터 시각화
- ⌨️ 키보드 네비게이션 조작
- 📈 종합 분석 뷰

---

## 🚀 빠른 시작

### 📋 환경 요구사항

- Python 3.8 이상
- 지원 OS: Windows / macOS / Linux

### ⚡ 설치 방법

#### 방법 1: pip 설치 (권장)

```bash
pip install testforge
```

#### 방법 2: 소스에서 설치

```bash
git clone https://github.com/gitstq/TestForge.git
cd TestForge
pip install -e .
```

#### 방법 3: 원클릭 설치 스크립트

```bash
curl -fsSL https://raw.githubusercontent.com/gitstq/TestForge/main/install.sh | bash
```

### 🎯 빠른 사용법

####命令行 사용법

```bash
# 코드 구조 분석
testforge analyze ./src

# 테스트 케이스 생성
testforge generate ./src -o ./tests

# 테스트 품질 평가
testforge assess ./tests

# TUI 인터페이스 실행
testforge dashboard
```

#### TUI 인터페이스 사용법

```bash
# 인터랙티브 인터페이스 실행
testforge

# 작업 선택:
# 1. 코드 분석
# 2. 테스트 생성
# 3. 품질 평가
# 4. 대시보드
# 5. 도움말
# 6. 종료
```

---

## 📖 상세 사용 가이드

### 코드 분석

```bash
# 전체 프로젝트 분석
testforge analyze ./my_project

# 특정 파일 분석
testforge analyze ./my_project/utils.py

# 상세 출력 모드
testforge analyze ./src -v

# 언어 지정
testforge analyze ./src --lang python
```

### 테스트 생성

```bash
# pytest 프레임워크로 테스트 생성
testforge generate ./src -o ./tests --framework pytest

# unittest 프레임워크로 테스트 생성
testforge generate ./src -o ./tests --framework unittest

# 목표 커버리지 설정
testforge generate ./src -o ./tests --coverage 90
```

### 품질 평가

```bash
# 테스트 파일 품질 평가
testforge assess ./tests/test_math.py

# 테스트 디렉토리 평가
testforge assess ./tests

# JSON 형식으로 출력
testforge assess ./tests --format json
```

---

## 💡 설계 철학

### 🎯 설계 원칙

1. **미니멀리즘** - 제로 외부 의존성, 사용门槛 낮춤
2. **개발자 친화적** - 명확한 출력, 친숙한 조작
3. **실용주의** - 실제 문제 해결, 실질적 가치 제공
4. **지속적 개선** - 커뮤니티 피드백 경청, 지속 최적화

### 🔧 기술 선택

- **언어**: Python 3.8+ (성숙한 생태계, 확장 용이)
- **코드 분석**: Python AST 모듈 (표준 라이브러리, 설치 불필요)
- **인터페이스**: 터미널 네이티브 UI (그래픽 라이브러리 의존성 불필요)
- **테스트 프레임워크**: pytest/unittest (업계 표준)

---

## 🤝 기여

기여를 환영합니다! Issue와 Pull Request를 제출해 주세요.

### 🐛 버그 보고

[GitHub Issues](https://github.com/gitstq/TestForge/issues)에 상세히 설명해 주세요:
1. 재현 단계
2. 예상 동작
3. 실제 동작
4. 환경 정보

### 💻 코드 기여

1. 이 저장소를 Fork
2. 피처 브랜치 생성 (`git checkout -b feature/AmazingFeature`)
3. 변경 사항 커밋 (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치에 푸시 (`git push origin feature/AmazingFeature`)
5. Pull Request 생성

---

## 📄 라이선스

이 프로젝트는 **MIT 라이선스**를 사용합니다.

---

<div align="center">

**이 프로젝트가 도움이 되셨다면 ⭐ Star를 눌러주세요!**

Made with ❤️ by [GitStQ](https://github.com/gitstq)

</div>
