import time
import streamlit as st
import random
import numpy as np
import pandas as pd

daikiti = 0
syoukiti = 0
kyou = 0

chart = []

st.title("πγγΏγγγ°γ©γπ")

st.write("Source : https://github.com/akazdayo/spinner_omiikuji")

chart = [0, 0, 0]
daikiti = 0
syoukiti = 0
kyou = 0

values = st.slider(
    'εζ°',
    0, 10000, 100)

c = st.container()

with st.spinner('Wait for it...'):
    with st.expander("γγΏγγη΅ζδΈθ¦§"):
        for i in range(values):
            kuji = random.randint(0, 2)
            chart[kuji] += 1
            if kuji == 0:
                st.success("ε€§ε")
                daikiti += 1
            elif kuji == 1:
                st.warning("η¬ε")
                syoukiti += 1
            else:
                st.error("εΆ")
                kyou += 1

chart_data = pd.DataFrame(
    chart,
    index=['ε€§ε', 'η¬ε', 'εΆ']
)
c.bar_chart(chart_data)

st.balloons()
