import time
import streamlit as st
import pandas as pd
import numpy as np

"Demonstração de progresso:"

# adicionando um marcador

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    # Atualiza a barra de progresso de acordo com cada iteração.
    latest_interation.text(f'Iteration {i+1}')
    bar.progress( i + 1)
    time.sleep(0.1)

