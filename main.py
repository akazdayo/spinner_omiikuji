import time
import streamlit as st
import random

with st.spinner('Wait for it...'):
    time.sleep(5)
rand = random.randint(0, 2)
if rand == 0:
    st.success("Done")
elif rand == 1:
    st.warning("Warning")
else:
    st.error("Error")
st.balloons()
