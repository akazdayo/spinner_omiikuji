import time
import streamlit as st
import random
import numpy as np
import pandas as pd

daikiti = 0
syoukiti = 0
kyou = 0

with st.spinner('Wait for it...'):
    time.sleep(1)
kuji = random.randint(0, 2)

st.write("Source : https://github.com/akazdayo/spinner_omiikuji")

if kuji == 0:
    st.success("大吉")
    daikiti += 1
elif kuji == 1:
    st.warning("笑吉")
    syoukiti += 1
else:
    st.error("凶")
    kyou += 1

st.balloons()
