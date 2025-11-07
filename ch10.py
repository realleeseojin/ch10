import streamlit as st
import pandas as pd
import numpy as np

def myintro_page():
    st.title('나의 소개 페이지')
    st.header('자기소개')
    st.text('안녕하세요 저는 홍길동입니다.')
    st.write('저는 **데이터 분석**과 *머신러닝*에 관심이 많습니다.')
    st.subheader('좋아하는 것')
    st.write('저는 독서와 영화를 좋아합니다.')
    st.write('가장 자주 방문하는 사이트는 [streamlit.io](https://streamlit.io) 입니다.')
    st.subheader('앞으로의 목표')
    st.write('해적왕이 될겁니다.')
    st.caption('제가 좋아하는 파이썬 코드 예시')
    st.code('''
        Hello World!!('print')
    ''')
    st.caption('피타고라스 정리')
    st.latex(r'a^2 = c^2 - b^2')
def pinkgongju():
    st.image('images/player.jpg')
def data():
       schedule = {
            '요일' : ['월', '화', '수', '목', '금'],
            '1교시' : ['', '전자기파와 광학', '', '전자기파와 광학', ''],
            '2교시' : ['', '', '', '', '컴퓨팅 탐색'],
            '3교시' : ['기본 물리 수학', '', '기본 물리 수학', 'NPU기반 인공지능 추론 실습', '컴퓨팅 탐색'],
            '4교시' : ['', '', '', 'NPU기반 인공지능 추론 실습', ''],

       }
       st.subheader('정적 시간표')
       st.table(schedule)
       st.subheader('동적 시간표')
       json_data = {"컴퓨팅 탐색" : {'교수' : '변해선', '강의실' : 22}, '전자기파와 광학' : {'교수' : '김현용', '강의실' : 25}}
       st.json(json_data)
       st.subheader('이번 학기 요약')
       col1, col2 = st.columns(2)
       with col1:
        st.metric(label="수강 과목 수", value="5")

        with col2:
            st.metric(label="총 학점", value="16", delta="+2", delta_color="normal")

st.button('button', on_click=myintro_page, args=())
st.button('핑크공주', on_click=pinkgongju, args=())
st.button('시간표', on_click=data, args=())
