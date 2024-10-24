import streamlit as st
import json
import os

# 파일 경로 설정 (알람 정보를 저장할 JSON 파일 경로)
ALARM_FILE = 'alarms.json'

# 알람 데이터를 JSON 파일에서 읽어오기
def load_alarms():
    if os.path.exists(ALARM_FILE):
        with open(ALARM_FILE, 'r') as file:
            return json.load(file)
    return {}

# 알람 데이터를 JSON 파일에 저장하기
def save_alarms(alarms):
    with open(ALARM_FILE, 'w') as file:
        json.dump(alarms, file)

# 초기 알람 불러오기
alarms = load_alarms()

# Streamlit 제목과 설명 추가
st.title("알람 조치 챗봇")
st.write("알람에 따른 조치 방안을 추천하는 챗봇입니다. 알람의 유형에 따라 적절한 조치를 제안합니다.")

# 사용자 입력 섹션 (알람 메시지 검색)
user_input = st.text_input("알람 메시지를 입력하거나 특정 단어를 입력해주세요", "Link")

# 사용자 입력 처리
if user_input:
    found = False  # 해당하는 알람이 있는지 확인하기 위한 변수
    for alarm, details in alarms.items():
        if user_input.lower() in alarm.lower():  # 입력된 문구가 알람 메시지에 포함되어 있으면
            description = details.get('description', '설명 없음')  # 설명이 없으면 기본값 설정
            action = details.get('action', '조치 방법 없음')  # 조치 방법이 없으면 기본값 설정
            st.write(f"**알람 명**: {alarm}")
            st.write(f"**설명**: {description}")
            st.write(f"**조치 방법**: {action}")
            found = True
    
    if not found:
        st.write("해당 알람에 대한 정보를 찾을 수 없습니다. 시스템 로그를 확인하세요.")

# 알람 추가 섹션
st.write("---")
st.write("### 새로운 알람 추가")

# 알람 이름과 설명, 조치 방법 입력
new_alarm_name = st.text_input("새로운 알람 명", "")
new_alarm_description = st.text_input("새로운 알람 설명", "")
new_alarm_action = st.text_input("새로운 알람 조치 방법", "")

# 추가 버튼을 누르면 딕셔너리에 새로운 알람을 추가하고 JSON 파일에 저장
if st.button("알람 추가"):
    if new_alarm_name and new_alarm_description and new_alarm_action:  # 알람 이름, 설명, 조치 방법이 모두 입력된 경우
        alarms[new_alarm_name] = {
            'description': new_alarm_description,
            'action': new_alarm_action
        }
        save_alarms(alarms)  # 새로운 알람을 JSON 파일에 저장
        st.success(f"새로운 알람 '{new_alarm_name}'가 성공적으로 추가되었습니다.")
    else:
        st.error("알람 이름, 설명, 조치 방법을 모두 입력해주세요.")

# 알람 수정 섹션
st.write("---")
st.write("### 알람 수정")

# 수정할 알람 이름 입력
modify_alarm_name = st.text_input("수정할 알람 명", "")
modify_password = st.text_input("비밀번호를 입력하세요", type="password")

if modify_alarm_name in alarms and modify_password == "1109443":
    # 수정할 알람 설명과 조치 방법 입력
    modify_alarm_description = st.text_input("수정된 알람 설명", alarms[modify_alarm_name].get('description', ''))
    modify_alarm_action = st.text_input("수정된 알람 조치 방법", alarms[modify_alarm_name].get('action', ''))

    if st.button("알람 수정"):
        # 알람 수정하고 저장
        alarms[modify_alarm_name] = {
            'description': modify_alarm_description,
            'action': modify_alarm_action
        }
        save_alarms(alarms)
        st.success(f"알람 '{modify_alarm_name}'가 성공적으로 수정되었습니다.")
else:
    if modify_alarm_name and modify_password != "1109443":
        st.error("잘못된 비밀번호입니다.")

# 업데이트된 알람 리스트 출력
st.write("---")
st.write("### 현재 알람 리스트")

# 현재 알람 목록을 출력
for alarm, details in alarms.items():
    description = details.get('description', '설명 없음')
    action = details.get('action', '조치 방법 없음')
    st.write(f"**알람 명**: {alarm}")
    st.write(f"**설명**: {description}")
    st.write(f"**조치 방법**: {action}")
