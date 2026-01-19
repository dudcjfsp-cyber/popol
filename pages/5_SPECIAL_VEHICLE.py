import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import styles

st.set_page_config(page_title="특수 차량 예약", page_icon="🚑")
styles.apply_global_styles()

st.title("🚑 환자 맞춤 이동 서비스")
st.write("병원 이동이 힘드신가요? 특수 차량을 예약하세요.")

st.markdown("---")

# 더미 데이터
vehicles = [
    {
        "model": "스타렉스 (리프트 장착)",
        "plate": "서울 12가 3456",
        "driver": "김철수 기사님",
        "feature": "휠체어 탑승 가능, 넓은 실내",
        "status": "예약 가능"
    },
    {
        "model": "카니발 (슬로프 장착)",
        "plate": "서울 78나 9012",
        "driver": "이영희 기사님",
        "feature": "낮은 차체, 편안한 승차감",
        "status": "예약 가능"
    },
    {
        "model": "레이 (복지 차량)",
        "plate": "서울 34다 5678",
        "driver": "박민수 기사님",
        "feature": "경차 혜택, 좁은 골목 이동 용이",
        "status": "운행 중"
    }
]

for v in vehicles:
    with st.container(border=True):
        st.subheader(f"🚐 {v['model']}")
        
        # 차량 정보 강조
        st.markdown(f"""
        <div style='background-color: #f9f9f9; padding: 15px; border-radius: 10px;'>
            <p style='margin: 5px 0;'>🔢 <b>차량번호:</b> {v['plate']}</p>
            <p style='margin: 5px 0;'>👤 <b>기사님:</b> {v['driver']}</p>
            <p style='margin: 5px 0;'>✨ <b>특징:</b> {v['feature']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if v['status'] == "예약 가능":
            if st.button(f"📞 예약하기 ({v['plate']})", key=f"btn_{v['plate']}"):
                st.balloons()
                st.success(f"[{v['plate']}] 차량 예약 요청이 접수되었습니다! \n\n기사님이 곧 전화드릴 예정입니다.")
        else:
             st.button(f"🚫 {v['status']}", disabled=True, key=f"btn_{v['plate']}")

st.markdown("---")
if st.button("🏠 홈으로 돌아가기"):
    st.switch_page("pages/1_HOME.py")
