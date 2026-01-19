import streamlit as st

def apply_global_styles():
    st.markdown("""
    <style>
        /* [수정] 글로벌 폰트 타겟 수정 (모든 div에 적용하면 레이아웃이 깨짐) */
    /* 텍스트가 들어가는 주요 요소 위주로 적용 */
    html, body, p, li, h1, h2, h3, h4, span, label, .stMarkdown, .stButton button {
        font-family: 'Malgun Gothic', sans-serif !important;
        line-height: 1.6 !important;
    }
    
    /* 텍스트 크기 강제 적용 (단, 달력 등 특정 위젯 제외를 위해 :not 사용 고려했으나 복잡하므로 덮어쓰기 전략 유지) */
    .stMarkdown p, .stMarkdown div, .stMarkdown li, .appview-container .stMarkdown {
         font-size: 39px !important;
    }
    
    /* 인풋 위젯 텍스트 크기 */
    .stDateInput input, .stSelectbox div[data-baseweb="select"] div {
        font-size: 32px !important;
        height: 60px !important;
    }
    
    /* 라벨 크기 */
    label {
        font-size: 32px !important;
    }

    /* 사이드바 폰트 */
    .css-1d391kg {
        font-size: 36px !important;
    }
    
    /* =================================================================================
       [긴급 수정] 달력(Calendar) 스타일 격리 및 복구
       글로벌 스타일의 영향을 받지 않도록 강제로 초기화합니다.
       ================================================================================= */
    
    div[data-baseweb="calendar"] {
        width: 400px !important; /* 너비 확보 */
        max-width: 90vw !important;
        background-color: #ffffff !important;
        padding: 10px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
        font-size: 18px !important; /* 기본 폰트 크기로 리셋 */
    }

    /* 달력 내부의 모든 텍스트 요소 리셋 */
    div[data-baseweb="calendar"] * {
        font-size: 22px !important; /* 날짜 숫자 크기 적절히 */
        line-height: 1.2 !important;
        font-family: 'Malgun Gothic', sans-serif !important;
        width: auto !important;
        height: auto !important;
    }
    
    /* 날짜 셀 (Grid) */
    div[data-baseweb="calendar"] div[role="grid"] div {
        margin: 0 !important;
        padding: 5px !important;
    }
    
    /* 월/연도 네비게이션 헤더 */
    div[data-baseweb="calendar"] div[aria-live="polite"] {
        font-size: 28px !important; /* 헤더는 조금 크게 */
        font-weight: bold !important;
        margin-bottom: 10px !important;
    }
    
    /* 요일 헤더 (Su Mo Tu...) */
    div[data-baseweb="calendar"] div[aria-label] {
        font-size: 20px !important;
        margin-bottom: 5px !important;
    }
    
    /* 날짜 선택 버튼 (일자) */
    div[data-baseweb="calendar"] div[role="gridcell"] {
        width: 45px !important;
        height: 45px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 22px !important;
        cursor: pointer !important;
    }
    
    /* 오늘 날짜나 선택된 날짜 강조 */
    div[data-baseweb="calendar"] div[aria-selected="true"] {
        background-color: #4CAF50 !important;
        color: white !important;
        border-radius: 50% !important;
    }
    
    /* ================================================================================= */
</style>
""", unsafe_allow_html=True)
