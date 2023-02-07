import time
import streamlit as st
import random
import numpy as np
import pandas as pd

daikiti = 0
syoukiti = 0
kyou = 0

chart = []

st.title("🎊おみくじグラフ🎊")

with st.spinner('Wait for it...'):
    time.sleep(1)


st.write("Source : https://github.com/akazdayo/spinner_omiikuji")

chart = [0, 0, 0]
daikiti = 0
syoukiti = 0
kyou = 0

values = st.slider(
    '回数',
    0, 10000, 100)

c = st.container()


with st.expander("おみくじ結果一覧"):
    for i in range(values):
        kuji = random.randint(0, 2)
        chart[kuji] += 1
        if kuji == 0:
            st.success("大吉")
            daikiti += 1
        elif kuji == 1:
            st.warning("笑吉")
            syoukiti += 1
        else:
            st.error("凶")
            kyou += 1

chart_data = pd.DataFrame(
    chart,
    index=['大吉', '笑吉', '凶'],
)
c.bar_chart(chart_data)

st.balloons()
