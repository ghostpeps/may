import streamlit as st

import time

happy = st.button(label="మాతృ దినోత్సవ శుభాకాంక్షలు!", icon=":material/celebration:")
if happy:
  st.audio("mother.wav", autoplay=True)
  st.balloons()
  time.sleep(0.5)
  st.balloons()
st.write("-భవిష్")
st.write("")
