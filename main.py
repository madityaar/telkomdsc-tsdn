import pandas as pd
import streamlit as st
import hydralit_components as hc


HtmlFile = open("index.html", 'r', encoding='utf-8')

with open("index.html", "r") as f:
    html_data = f.read()
source_code = HtmlFile.read()
#st.components.v1.html(source_code)

st.write('---')

st.subheader('Using components.v1.html')
st.code('''st.components.v1.html(html_data)''', language='python')
st.components.v1.html(html_data,width=1080, height=720,scrolling=True)


st.title("Hoax Detector")

st.text_area(label="hoax-analysis",placeholder="Ketikan Berita Yang Akan Diperiksa....")

st.button(label="Periksa")