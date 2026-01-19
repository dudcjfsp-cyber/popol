# 🏥 시니어 헬스케어 & 병원 예약 서비스 (Design Thinking Practice)

이 프로젝트는 고령층 사용자를 위해 디자인된 병원 예약 및 헬스케어 보조 서비스 프로토타입입니다. 
**디자인 사고(Design Thinking)** 프로세스를 통해 사용자의 불편함을 해소하고, 더 쉽고 편리한 의료 서비스 접근 경험을 제공하는 것을 목표로 합니다.

## 📌 주요 기능 (Features)

*   **🏥 병원 찾기**: 사용자가 원하는 지역 및 진료과목의 병원을 쉽게 검색할 수 있습니다.
*   **📅 간편 예약**: 큰 글씨와 쉬운 UI로 날짜와 시간을 선택하여 병원을 예약할 수 있습니다.
*   **👤 마이 페이지**: 예약 내역을 확인하고 관리할 수 있습니다.
*   **🚐 특수 차량 호출**: 거동이 불편한 어르신을 위한 병원 이동 지원 차량 호출 서비스입니다.
*   **🤖 AI 진단 (예시)**: 간단한 증상 입력을 통해 방문해야 할 진료과를 안내받을 수 있습니다.

## 🛠️ 기술 스택 (Tech Stack)

*   **Language**: Python 3.12+
*   **Framework**: [Streamlit](https://streamlit.io/)
*   **Data Storage**: JSON (Local file storage for prototype)

## 🚀 설치 및 실행 방법 (Installation & Usage)

1.  **레포지토리 클론 (Clone)**
    ```bash
    git clone [repository_url]
    cd "디자인사고 연습"
    ```

2.  **가상환경 생성 및 활성화 (선택 사항)**
    ```bash
    python -m venv venv
    
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **패키지 설치**
    ```bash
    pip install streamlit
    ```

4.  **애플리케이션 실행**
    ```bash
    streamlit run app.py
    ```

## 📂 프로젝트 구조 (Structure)

```
📂 디자인사고 연습
├── 📄 app.py               # 메인 진입점 (Entry Point)
├── 📄 styles.py            # 공통 스타일 정의 (CSS 등)
├── 📂 pages                # 스트림릿 멀티페이지 파일들
│   ├── 1_HOME.py           # 홈 화면
│   ├── 2_HOSPITAL_SEARCH.py # 병원 검색
│   ├── 3_RESERVATION.py    # 예약 하기
│   ├── 4_MY_PAGE.py        # 마이 페이지 (예약 확인)
│   ├── 5_SPECIAL_VEHICLE.py # 특수 차량 신청
│   └── 6_AI_DIAGNOSIS.py   # AI 진단 보조
└── 📄 reservations.json    # 예약 데이터 저장 파일 (자동 생성됨)
```
