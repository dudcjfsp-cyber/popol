import streamlit as st
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import styles

st.set_page_config(page_title="AI 진단", page_icon="📷")
styles.apply_global_styles()

st.title("📷 상처 사진 촬영")
st.write("카메라가 켜지면 상처 부위를 찍어주세요.")

st.markdown("---")

# 카메라 입력
img_file = st.camera_input("여기를 눌러 사진을 찍으세요")

st.markdown("""
<div style='text-align: center; margin-top: 10px; margin-bottom: 20px;'>
    <p style='font-size: 24px; font-weight: bold; color: #555;'>
        사진촬영 후 적절한 진료 과를 매칭해드립니다.
    </p>
</div>
""", unsafe_allow_html=True)

if img_file is not None:
    st.success("사진 촬영 완료!")
    
    with st.spinner("사진을 분석하여 진료과를 찾는 중입니다..."):
        time.sleep(2) # 분석 시뮬레이션
        
    st.markdown("---")
    st.subheader("💡 분석 결과")
    
    # 결과 강조 박스
    st.markdown("""
    <div style='background-color: #E3F2FD; padding: 20px; border-radius: 15px; border: 2px solid #2196F3; margin-bottom: 20px; text-align: center;'>
        <p style='font-size: 24px; color: #555; margin: 0;'>추천 진료과는</p>
        <h2 style='color: #1565C0; margin: 10px 0; font-size: 48px;'>정형외과</h2>
        <p style='font-size: 24px; color: #555; margin: 0;'>입니다.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("근처 정형외과를 찾아보시겠습니까?")
    
    if st.button("🏥 근처 정형외과 찾으러 가기 (추천)", type="primary"):
        # 검색어 세팅 시뮬레이션 (실제 구현 시 state 전달 고려)
        st.switch_page("pages/2_HOSPITAL_SEARCH.py")

st.markdown("---")
if st.button("🏠 홈으로 돌아가기"):
    st.switch_page("pages/1_HOME.py")
