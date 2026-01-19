import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="병원 예약 서비스",
    page_icon="🏥",
    layout="wide",
)

# 세션 상태 초기화
if 'reservations' not in st.session_state:
    st.session_state.reservations = []

import styles
styles.apply_global_styles()

st.title("🏥 어르신을 위한 병원 예약")

st.info("왼쪽 메뉴에서 원하시는 기능을 선택해주세요.")

st.subheader("환영합니다, 김순자 님!")
st.write("오늘도 건강한 하루 보내세요.")

# 바로가기 버튼들 (실제로는 페이지 이동 로직이 필요하지만 Streamlit 멀티페이지에서는 안내 문구로 대체하거나 switch_page 사용 가능)
# 여기서는 심플한 안내만 제공
st.markdown("---")
st.write("👇 **원하시는 메뉴를 눌러주세요**")

# 컬럼 대신 수직 배치 + 헤드라인 통합 스타일 적용 (사용자 요청 반영)
if st.button("🔍 병원 찾기 (눌러주세요)", key="main_go_search"):
    st.switch_page("pages/2_HOSPITAL_SEARCH.py")

st.markdown("<br>", unsafe_allow_html=True) # 간격 추가

if st.button("📋 내 예약 확인 (눌러주세요)", key="main_go_mypage"):
    st.switch_page("pages/4_MY_PAGE.py")
