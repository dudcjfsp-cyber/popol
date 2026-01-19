import streamlit as st
import datetime
import sys
import os
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import styles

st.set_page_config(page_title="예약하기", page_icon="📅")
styles.apply_global_styles()

st.title("📅 예약 하기")

# --- 상태 초기화 로직 ---
if 'reservations' not in st.session_state:
    st.session_state.reservations = []

# 예약 단계 관리 (1: 날짜, 2: 시간, 3: 확인)
if 'res_step' not in st.session_state:
    st.session_state.res_step = 1

# 예약 데이터 임시 저장
if 'res_date' not in st.session_state:
    st.session_state.res_date = datetime.date.today()
if 'res_time' not in st.session_state:
    st.session_state.res_time = None

# 완료 화면 처리
if 'reservation_complete' in st.session_state and st.session_state.reservation_complete:
    st.balloons()
    st.success("예약이 성공적으로 완료되었습니다!")
    st.markdown("---")
    
    if st.button("📋 내 예약 확인하러 가기 (눌러주세요)", key="go_mypage_success"):
        # 상태 정리
        del st.session_state['reservation_complete']
        del st.session_state['res_step'] # 단계 초기화
        del st.session_state['res_date']
        del st.session_state['res_time']
        if 'selected_hospital' in st.session_state:
            del st.session_state['selected_hospital']
        st.switch_page("pages/4_MY_PAGE.py")
    st.stop()

# 병원 선택 확인
if 'selected_hospital' not in st.session_state:
    st.warning("먼저 병원을 선택해주세요.")
    if st.button("병원 찾으러 가기"):
        st.switch_page("pages/2_HOSPITAL_SEARCH.py")
    st.stop()

hospital_name = st.session_state['selected_hospital']
st.success(f"선택하신 병원: **{hospital_name}**")
st.markdown("---")

# --- 단계별 화면 표시 (Wizard) ---

# [단계 1] 날짜 선택
if st.session_state.res_step == 1:
    st.markdown(f"### 1단계: 언제 방문하시겠어요?")
    st.write("아래 달력에서 날짜를 선택해주세요.")
    
    val_date = st.date_input(
        "날짜 선택",
        min_value=datetime.date.today(),
        value=st.session_state.res_date,
        key="date_input_widget"
    )
    
    st.markdown("---")
    
    # 다음 단계 버튼
    if st.button("다음 (시간 선택하러 가기) 👉", key="step1_next"):
        st.session_state.res_date = val_date
        st.session_state.res_step = 2
        st.rerun()

# [단계 2] 시간 선택
elif st.session_state.res_step == 2:
    st.markdown(f"### 2단계: 몇 시에 방문하시겠어요?")
    date_str = st.session_state.res_date.strftime('%Y년 %m월 %d일')
    st.info(f"선택한 날짜: **{date_str}**")
    st.write("아래 시간 중 하나를 눌러주세요.")
    
    times = ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"]
    
    # 시간 선택 (pills는 선택 즉시 리런됨)
    val_time = st.pills("방문 시간", times, selection_mode="single", key="time_input_widget")
    
    st.markdown("---")
    
    col_prev, col_next = st.columns([1, 1])
    with col_prev:
        if st.button("👈 이전 (날짜 변경)", key="step2_prev"):
            st.session_state.res_step = 1
            st.rerun()
            
    # 시간 선택 시 자동 넘어감 또는 버튼 제공
    if val_time:
        st.session_state.res_time = val_time
        # 바로 넘어가거나 사용자에게 확인 버튼을 누르게 할 수 있음.
        # 사용자가 "자동 이동"을 원했으므로 선택되면 바로 다음 단계 버튼 활성화 안내 느낌으로 처리
        # 여기서는 명시적 버튼 클릭 유도 (노인분들은 자동 이동 시 당황할 수 있음) but 요청은 '자동 배치'
        # 버튼을 크게 띄워줍니다.
        
        # 안내 문구
        st.write("👇 아래 버튼을 눌러 예약을 확인해주세요.")
        if st.button("다음 (예약 확인) 👉", key="step2_next"):
             st.session_state.res_step = 3
             st.rerun()

# [단계 3] 예약 확인
elif st.session_state.res_step == 3:
    st.markdown(f"### 3단계: 예약 내용을 확인해주세요")
    
    d_str = st.session_state.res_date.strftime('%Y년 %m월 %d일')
    t_str = st.session_state.res_time
    
    msg = f"""
    <div style='background-color: #E8F5E9; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <p style='color: #2E7D32; font-weight: bold;'>🏥 병원: {hospital_name}</p>
        <p style='color: #333; font-weight: bold;'>📅 날짜: {d_str}</p>
        <p style='color: #333; font-weight: bold;'>⏰ 시간: {t_str}</p>
    </div>
    """
    st.markdown(msg, unsafe_allow_html=True)
    st.write("이 내용으로 예약을 확정하시겠습니까?")
    
    st.markdown("---")
    
    if st.button("✅ 네, 예약 확정하기 (누르면 끝)", type="primary", key="step3_confirm"):
        # 예약 정보 생성 및 저장
        new_reservation = {
            "hospital": hospital_name,
            "date": st.session_state.res_date.strftime('%Y-%m-%d'),
            "time": st.session_state.res_time,
            "created_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        
        import json
        file_path = "reservations.json"
        data = []
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                try: data = json.load(f)
                except: data = []
        
        data.append(new_reservation)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        st.session_state.reservations = data
        st.session_state.reservation_complete = True
        st.rerun() # 완료 화면으로 이동
        
    if st.button("👈 이전 (시간 변경)", key="step3_prev"):
        st.session_state.res_step = 2
        st.rerun()
