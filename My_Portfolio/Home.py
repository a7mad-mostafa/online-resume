import streamlit as st
import os

os.chdir(r"H:\My Drive\Python 4 Juniors\14- Streamlit Portfolio\My_Portfolio")

st.markdown("<h1 style='text-align: center;  font-family: cursive;'>Anas Ahmad</h1>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; '>Junior Python Developer</h5>", unsafe_allow_html=True)

st.markdown('<br>', unsafe_allow_html=True)

st.subheader("About Me",divider='rainbow')

c1,c2,c3 = st.columns([1.2, 0.2, 0.5])

with c1:
    st.markdown('<br>', unsafe_allow_html=True)
    st.write(""" 
             I’m a student passionate about learning programming and exploring new technologies. Currently, I’m building my skills in Python. I love solving problems and am eager to apply what I’ve learned in real-world projects. My goal is to become a skilled software developer and contribute to meaningful projects.
             """)
    
with c3:
    st.image("anas.jpeg")


st.subheader("My :blue[skills] ⚒️",divider='rainbow')
st.markdown("###### 📍 Location: Egypt")
st.markdown("###### 📚 Interest: Coding, Swimming")
st.markdown("###### 👀 Linkedin: [My Profile](https://www.linkedin.com/in/anas-ahmad-dev/)")