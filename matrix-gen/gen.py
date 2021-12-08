import streamlit as st
import numpy as np

st.markdown("<h1 style='text-align: center; color: orange;'>RANDOM MATRIX GENERATOR</h1>", unsafe_allow_html=True)

a=st.number_input("Enter number of rows",2)
b=st.number_input("Enter number of columns",2)
min=st.number_input("Enter MINIMUM value",1)
max=st.number_input("Enter MAXIMUM value",1)

array=np.random.randint(low=min,high=max,size=(a,b))

st.markdown("<h1 style='text-align: center; color: yellow;'>ANSWER</h1>", unsafe_allow_html=True)

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    button_1 = st.button('APPLY')

if button_1:
    st.write(array)
    st.balloons()

    
