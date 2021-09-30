import streamlit as st
import numpy as np
import pandas as pd

st.title("Meu primeiro aplicativo streamlit")
st.write("Meu primeiro dataFrame:")
st.write(pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 30, 40, 50]
}))

pd.read_excel("Dados_alm.xlsx")
