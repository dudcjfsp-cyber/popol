import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import styles

st.set_page_config(page_title="병원 찾기", page_icon="🔍")
styles.apply_global_styles()

st.title("🔍 병원 찾기")
st.write("서대문구 근처의 병원 목록입니다.")

# 검색 필터 (단순화)
only_open = st.checkbox("지금 진료 중인 병원만 보기", value=True)
medical_aid = st.checkbox("의료급여 혜택 병원만 보기", value=True)

st.markdown("---")

# 더미 데이터
hospitals = [
    {
        "name": "서대문 정형외과",
        "tags": ["디스크 전문", "의료급여"],
        "distance": "도보 5분",
        "status": "진료중",
        "desc": "친절한 원장님, 물리치료실 완비"
    },
    {
        "name": "연세 사랑 병원",
        "tags": ["척추 수술", "주차 가능"],
        "distance": "버스 10분",
        "status": "진료중",
        "desc": "대학병원 출신 의료진"
    },
    {
        "name": "튼튼 재활 의원",
        "tags": ["재활 전문", "의료급여"],
        "distance": "도보 15분",
        "status": "점심시간",
        "desc": "넓은 대기실, 최신 장비"
    }
]

# 병원 목록 출력
for hosp in hospitals:
    # 필터 로직
    if medical_aid and "의료급여" not in hosp["tags"]:
        continue
    if only_open and hosp["status"] != "진료중":
        continue

    with st.container(border=True):
        st.subheader(f"🏥 {hosp['name']}")
        
        # 태그 표시
        tags_str = " ".join([f"#{t}" for t in hosp["tags"]])
        st.markdown(f"**{tags_str}**")
        
        st.write(f"📍 거리: {hosp['distance']} | 상태: {hosp['status']}")
        st.write(f"💡 {hosp['desc']}")
        
        if st.button(f"{hosp['name']} 예약하기", key=f"btn_{hosp['name']}"):
            # 선택한 병원을 세션에 저장하고 예약 페이지로 이동
            st.session_state['selected_hospital'] = hosp['name']
            st.switch_page("pages/3_RESERVATION.py")
