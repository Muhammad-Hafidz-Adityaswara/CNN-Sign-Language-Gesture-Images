# Import Library
import streamlit as st

# Import halaman streamlit yang sudah dibuat
import eda
import prediction

# Tombol navigasi
navigasi = st.sidebar.selectbox('Select Page :', 
                                ('Home Page','EDA','Sign Language Gesture Prediction'))
st.write('---')

if navigasi == 'Home Page':
    st.header('Home Page') 
    st.write('---')
    st.write('Creator   : Muhammad Hafidz Adityaswara')
    st.write('From      : HCK - 012')
    st.write('---')


elif navigasi == 'Sign Language Gesture Prediction':
    prediction.run()
else :
    eda.run()