import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import styles

st.set_page_config(page_title="홈 - 병원 예약", page_icon="🏠")
styles.apply_global_styles()

st.title("🏠 홈 화면")

st.markdown("### 무엇을 도와드릴까요?")

# [신규] 상처 사진 촬영 버튼
if st.button("📷 상처부위 사진을 찍어주세요 (눌러주세요)", type="primary", key="go_diagnosis"):
    st.switch_page("pages/6_AI_DIAGNOSIS.py")

st.markdown("---")

st.markdown("""
### 안녕하세요, 김순자 님!
원하시는 서비스를 선택해주세요.
""")

st.markdown("---")

# 큰 버튼 배치를 위해 컬럼 사용 안 하고 수직 배치로 가독성 높임
st.write("▼ **서대문구 주변의 디스크 전문, 의료급여 가능 병원을 찾습니다.**")
if st.button("🔍 병원 찾기 (눌러주세요)", key="go_search"):
    st.switch_page("pages/2_HOSPITAL_SEARCH.py")

st.markdown("---")

st.write("▼ **잡아둔 병원 예약 날짜와 시간을 확인합니다.**")
if st.button("📋 내 예약 확인 (눌러주세요)", key="go_mypage"):
    st.switch_page("pages/4_MY_PAGE.py")

st.markdown("---")
st.info("도움이 필요하시면 **02-123-4567**로 전화주세요.")
