# import library
import pandas as pd 
import numpy as np
import streamlit as st 

# Function untuk menjalankan streamlit model prediksi
def run():
    # Title
    st.title('Exploratory Data Analysis (EDA)')
    st.write('---')

    # Judul visualisasi 1
    st.write('### Distribusi label')

    st.image('distribusiLabel.png')
    st.write('---')

    # Judul visualisasi 2
    st.write('### Gambar Sign Language Gesture')

    st.image('gambarLabel.png')
    st.write('---')

    # Create by Hafidz
    st.markdown(
        """
        <style>
        .right-align {
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        "<p class='right-align'>Created by Muhammad Hafidz Adityaswara</p>",
        unsafe_allow_html=True
    )


# Menjalankan perintah setelah halaman terbuka
if __name__ == "__main__":
    run()
