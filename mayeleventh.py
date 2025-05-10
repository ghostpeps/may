import streamlit as st

import time

happy = st.button(label="మాతృ దినోత్సవ శుభాకాంక్షలు!", icon=":material/celebration:")
if happy:
  st.balloons()
  time.sleep(0.5)
  st.balloons()
st.write("-భవిష్")
st.markdown(":green-badge[:material/deployed_code:డాష్‌బోర్డ్‌లోని పెట్టెలో చూడండి]")
