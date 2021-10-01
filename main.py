import streamlit as st
import numpy as np
import pandas as pd

st.title("Meu primeiro aplicativo streamlit")
st.write("Meu primeiro dataFrame:")
st.write(pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 30, 40, 50]
}))



"Utilizando os comandos mágicos:"

df = pd.DataFrame({
    "Primeira coluna": [1, 2, 3, 4, 5],
    "Second column": [10, 20, 30, 40, 50]
})

df


"Gerando Gráficos"

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)



"Plotando um mapa"

map_data = pd.DataFrame(
    np.random.randn(1000, 2)/[50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)

st.map(map_data)


"Widgets interativos:"
"Usando checkbox para exibir/esconder dados."

if st.checkbox("Exibir DataFrame"):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

    chart_data

"Caixa de seleção de opções"

option = st.sidebar.selectbox(
    "Escolha um número",
    df['Primeira coluna']
)

'Número escolhido:', option


left_column, right_column = st.columns(2)
pressed = left_column.button("Press me?")
if pressed:
    right_column.write("Whoohoo!")

expander = st.expander("FAQ")
expander.write("Aqui poderia ser informado texto de qualquer tipo")

