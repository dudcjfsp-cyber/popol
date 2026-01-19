import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import styles

st.set_page_config(page_title="내 정보", page_icon="👤")
styles.apply_global_styles()

st.title("👤 나의 예약 내역")

# [위치 이동] 환자 맞춤 서비스 (최상단 노출)
st.markdown("""
<div style='background-color: #FFEBEE; padding: 20px; border-radius: 15px; border: 2px solid #FFCDD2; margin-bottom: 20px;'>
    <h3 style='color: #D32F2F; margin: 0;'>🚑 <strong>환자 맞춤 특별 서비스</strong></h3>
    <p style='color: #B71C1C; margin-top: 10px;'>
        거동이 불편하신가요? 병원까지 편안하게 모셔다 드리는 <strong>특수 차량</strong>을 이용해보세요.
    </p>
</div>
""", unsafe_allow_html=True)

if st.button("🚐 특수 차량 예약하러 가기 (눌러주세요)", type="primary", key="go_special_vehicle"):
    st.switch_page("pages/5_SPECIAL_VEHICLE.py")

st.markdown("---")

st.write("▼ 잡아둔 병원 예약 목록입니다.")

import json
import os

# 파일에서 데이터 로드 함수
def load_reservations():
    file_path = "reservations.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return []
    return []

reservations = load_reservations()

if not reservations:
    st.info("아직 예약된 내역이 없습니다.")
    st.markdown("""
    **병원 예약이 필요하신가요?**
    """)
    if st.button("병원 예약하러 가기"):
        st.switch_page("pages/2_HOSPITAL_SEARCH.py")
else:
    # 최신 예약이 위로 오도록 역순 정렬
    for i, res in enumerate(reversed(reservations)):
        with st.container(border=True):
            st.subheader(f"🏥 {res['hospital']}")
            
            # 텍스트 크기 강제 확대
            st.markdown(f"""
            <div style='font-size: 24px; font-weight: bold; color: #333;'>
                📅 {res['date']} <br>
                ⏰ {res['time']}
            </div>
            """, unsafe_allow_html=True)
            
            st.caption(f"예약 확정 일시: {res['created_at']}")
            
            # 키 값에 인덱스(i)를 추가하여 중복 방지
            if st.button("예약 취소 (전화 문의)", key=f"cancel_{res['created_at']}_{i}"):
                st.error("취소는 병원으로 전화 부탁드립니다.\n\n📞 02-123-4567")

st.markdown("---")
if st.button("🏠 홈으로 돌아가기"):
    st.switch_page("pages/1_HOME.py")
