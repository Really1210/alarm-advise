import streamlit as st
from transformers import pipeline

# 모델 로딩 (Hugging Face의 자연어 처리 모델 사용)
nlp = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Streamlit 제목과 설명 추가
st.title("알람 조치 챗봇")
st.write("알람에 따른 조치 방안을 추천하는 챗봇입니다. 알람의 유형에 따라 적절한 조치를 제안합니다.")

# 알람 입력 섹션
user_input = st.text_input("알람 메시지를 입력해주세요", "Link Failure: No signal detected")

# 사용자 입력 처리
if user_input:
    # 알람 유형에 따른 기본 조치 로직
    if "Link Failure: Not in operation" in user_input:
        st.write("Rilink가 비활성화되었습니다. 광레벨을 측정하고 불안정한 구간을 점검하세요.")
    elif "Link Failure: No signal detected" in user_input:
        st.write("eCPRI 연결 상태를 확인하고 광레벨을 점검하세요. 연결이 되어 있지 않은 구간을 교체해야 합니다.")
    elif "No connection" in user_input:
        st.write("DUH와 AAU 사이의 SFP 및 케이블 상태를 점검하세요. 문제가 있는 링크를 교체하세요.")
    elif "SW Error" in user_input:
        st.write("SW 모듈을 재시작하거나 보드 교체를 고려하세요.")
    elif "Ethernet frame error" in user_input:
        st.write("Ethernet 프레임 에러가 발생했습니다. L2, L3 레이어를 확인하고 프레임 에러가 있는지 점검하세요.")
    else:
        # 챗봇 모델을 사용한 답변 생성
        conversation = nlp(f"알람 메시지: {user_input}")
        st.write(f"추천 조치: {conversation[0]['generated_text']}")
