import streamlit as st

import time

st.title(":material/celebration: మాతృ దినోత్సవ శుభాకాంక్షలు!")
happy = st.button(label="మాతృ దినోత్సవ శుభాకాంక్షలు!", icon=":material/celebration:")
if happy:
  st.balloons()
  time.sleep(0.5)
  st.balloons()
st.markdown(":green-badge[డాష్‌బోర్డ్‌లోని పెట్టెలో చూడండి]")
st.write("-భవిష్")
