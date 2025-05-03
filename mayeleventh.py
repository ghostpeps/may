import streamlit as st

import time

happy = st.button(label="మాతృ దినోత్సవ శుభాకాంక్షలు!", icon=":material/celebration:")
if happy:
  st.balloons()
  time.sleep(0.5)
  st.balloons()
st.image(image="Happy Mother's Day (4).png")
