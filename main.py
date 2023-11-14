import pandas as pd
import streamlit as st
import hydralit_components as hc

#can apply customisation to almost all the properties of the card, including the progress bar
theme_bad = {'bgcolor': '#FFF0F0','title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
theme_neutral = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
theme_good = {'bgcolor': '#EFF8F7','title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}

st.title("Live Feed Analysis")
df = pd.read_csv("data.csv",delimiter=";")
col1, col2= st.columns([7,1])

with col1:
  with st.container():
    for i, row in df.iterrows():
      cur_sentiment=None
      if row["hoax"] <=0.5:
        cur_sentiment=theme_good
      elif row["hoax"] >0.5 and row["hoax"] <0.7:
        cur_sentiment=theme_neutral
      else :
        cur_sentiment=theme_bad

      hc.info_card(title=row["sumber"] +" - Indikasi Hoax "+ str(int(row["hoax"]*100))+"%", content=row["berita"]+"-"+row["jam"] , theme_override=cur_sentiment,bar_value=row["hoax"]*100, icon_size="1.96rem",title_text_size="1.96rem",content_text_size="0.8rem")

with col2:
  with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:

st.title("Hoax Detector")

st.text_area(label="hoax-analysis",placeholder="Ketikan Berita Yang Akan Diperiksa....")

st.button(label="Periksa")