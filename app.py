import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("My title")
st.header("This is header")
st.write("Hello mypage")

st.write("## streamlit image test")
st.image('dog.jpg')

st.write("## streamlit dataframe test")
data = pd.read_csv("iris.csv")
data

st.write("## streamlit bar chart test")
var = [10,20,30]
var
st.bar_chart(var)
st.line_chart(var)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)
st.bar_chart(chart_data)

dt = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
dt
st.map(dt)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)



st.write("## streamlit display widgets test")
st.button("click me!")
#체크박스
agree = st.checkbox('I agree')
disagree = st.checkbox('I don\'t agree')
if agree:
    st.write("agree!")

if disagree:
    st.write("disagree!")
#라디오 버튼
kind = st.radio('Pick one', ['cats', 'dogs'])
if kind == 'cats':
    st.write('This is cats.')
else:
    st.write("This is dogs.")
#선택박스
option = st.selectbox('Pick one', ['cats', 'dogs'])
st.write('you selected ', option)

#멀티선택
options = st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.write(len(options))
for i in options:
    st.write('you selected: ', i)
#슬라이더
age = st.slider('Pick a number', 0, 100)
st.write("you are ", age, ' years old')

st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
#st.download_button('Download file', data)
#st.camera_input("Take a picture")
#st.color_picker('Pick a color')

with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')

