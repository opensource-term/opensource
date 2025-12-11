# 🖼️ Image-to-Text: AI Image Captioning Service

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Model-BLIP-yellow?logo=huggingface&logoColor=white)
![Gradio](https://img.shields.io/badge/Library-Gradio-orange?logo=gradio&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 1. 프로젝트 개요 (Project Overview)

이 프로젝트는 **멀티모달(Multi-modal) 딥러닝 모델**을 활용하여 사용자가 업로드한 이미지를 분석하고, 해당 상황을 텍스트로 설명해주는(Image Captioning) 웹 서비스입니다.

시각 장애인을 위한 웹 접근성 향상, 이미지 검색 고도화, 그리고 교육용 AI 도구로 활용될 수 있도록 오픈소스 모델인 **Salesforce의 BLIP(Bootstrapping Language-Image Pre-training)**을 기반으로 구현되었습니다.

### ✨ 주요 기능

- **이미지 업로드 및 분석:** 사용자가 이미지를 업로드하면 AI가 즉시 분석합니다.
- **영어 캡션 생성:** 이미지 내의 객체와 상황을 자연스러운 영어 문장으로 생성합니다.
- **웹 인터페이스 제공:** Gradio를 활용하여 누구나 쉽게 사용할 수 있는 UI를 제공합니다.

---

## 2. 데모 및 예시 (Demo)

아래는 실제 프로젝트 구동 화면입니다.

![데모 실행 화면](./assets/demo_screenshot.png)
_(위 이미지는 예시입니다. 실제 실행 후 스크린샷을 찍어 assets 폴더에 넣거나 경로를 수정해주세요)_

---

## 3. 사용 패키지 및 버전 (Requirements)

이 프로젝트는 **Python 3.12** 환경에서 테스트되었습니다. 주요 의존성 패키지는 다음과 같습니다. 상세 버전 정보는 `requirements.txt` 파일에 명시되어 있습니다.

- **transformers** (>=4.x): 사전 학습된 BLIP 모델 로드
- **torch** (>=2.x): 딥러닝 연산 처리
- **pillow**: 이미지 파일 처리
- **gradio**: 웹 인터페이스(GUI) 구현

---

## 4. 실행 방법 (Installation & Usage)

### 1) 저장소 클론 (Clone Repository)

먼저 프로젝트를 로컬 환경으로 가져옵니다.

```bash
git clone [https://github.com/](https://github.com/)[본인깃허브아이디]/[저장소이름].git
cd [저장소이름]
```

### 2) 필수 패키지 설치 (Install Dependencies)

아래 명령어를 입력하여 필요한 핵심 라이브러리들을 한 번에 설치합니다.
(Mac 환경에서 pip 명령어가 작동하지 않을 경우 pip3를 사용하세요!)

```bash
pip install torch transformers pillow gradio
```

### 3) 프로젝트 실행 (Run Application)

설치가 완료되면 아래 명령어로 파이썬 애플리케이션을 실행합니다.

```bash
python3 app.py
```

### 4) 웹 서비스 접속 (Access Web UI)

터미널에 로딩 메시지가 뜬 후, 아래와 같은 주소가 나타나면 브라우저에서 접속합니다.

```bash
Local URL: http://127.0.0.1:7860
```

### 5) 서비스 실행

접속 후 이미지를 업로드하고 Submit 버튼을 누르면 AI가 생성한 캡션을 확인할 수 있습니다.
