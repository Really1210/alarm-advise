import streamlit as st

# Streamlit 제목과 설명 추가
st.title("알람 조치 챗봇")
st.write("알람에 따른 조치 방안을 추천하는 챗봇입니다. 알람의 유형에 따라 적절한 조치를 제안합니다.")

# 알람 입력 섹션
user_input = st.text_input("알람 메시지를 입력하거나 특정 단어를 입력해주세요", "Link")

# 알람과 대응 방법을 담은 딕셔너리
alarms = {
    "Link Failure: Not in operation": "Rilink가 비활성화되었습니다. 광레벨을 측정하고 불안정한 구간을 점검하세요.",
    "Link Failure: No signal detected": "eCPRI 연결 상태를 확인하고 광레벨을 점검하세요. 연결이 되어 있지 않은 구간을 교체해야 합니다.",
    "No connection": "DUH와 AAU 사이의 SFP 및 케이블 상태를 점검하세요. 문제가 있는 링크를 교체하세요.",
    "SW Error": "SW 모듈을 재시작하거나 보드 교체를 고려하세요.",
    "Ethernet frame error": "Ethernet 프레임 에러가 발생했습니다. L2, L3 레이어를 확인하고 프레임 에러가 있는지 점검하세요."
}

# 사용자 입력 처리
if user_input:
    found = False  # 해당하는 알람이 있는지 확인하기 위한 변수
    for alarm, action in alarms.items():
        if user_input.lower() in alarm.lower():  # 입력된 문구가 알람 메시지에 포함되어 있으면
            st.write(f"**{alarm}**: {action}")
            found = True
    
    if not found:
        st.write("해당 알람에 대한 정보를 찾을 수 없습니다. 시스템 로그를 확인하세요.")
