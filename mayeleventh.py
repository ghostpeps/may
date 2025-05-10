import streamlit as st

import time

st.title(":material/celebration: మాతృ దినోత్సవ శుభాకాంక్షలు!")
happy = st.button(label="మాతృ దినోత్సవ శుభాకాంక్షలు!", icon=":material/celebration:")
if happy:
  st.balloons()
  time.sleep(1)
  st.balloons()
  time.sleep(1)
  st.balloons()
st.markdown(":green-badge[డాష్‌బోర్డ్‌లోని పెట్టెలో చూడండి]")
st.video(data="mothersday.mp4", loop=True, autoplay=True, muted=False)
st.write("-భవిష్")
