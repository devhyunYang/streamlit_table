import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title = "st.table()"
)

st.title('st.table()')
# st.header('이미지처리하기')
st.text('다양한 데이터 유형을 st.table()을 통해 테이터프레임을 생성하고 st.table()을 이용하여 테이블을 만듭니다.')

# 리스트
st.subheader('리스트 활용')
menu_data = ['Smoothie', 'Coke', 'Latte', 'Americano', 'Cake']
st.table(menu_data)

# NumPy 배열 생성
st.subheader('NumPy 배열')
data_1 = np.random.randn(8, 4)
data_2 = np.random.randint(1, 10, size=(8, 4))
data_3 = np.random.rand(8,4)

st.text('1. randn')
st.table(data_1)

st.text('2. randint')
st.table(data_2)

st.text('3. rand')
st.table(data_3)

st.subheader('NumPy 배열')
# 데이터프레임 생성
cafe_data = {'메뉴명': ['Juice', 'Americano', 'Latte', 'espresso'],
        '가격': [5000, 3000, 4000, 2000],
        '핫/아이스 가능 여부': ['불가능', '가능', '가능', '가능']}
df = pd.DataFrame(cafe_data)

# 테이블 생성
st.table(df)
