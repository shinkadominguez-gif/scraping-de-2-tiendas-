import streamlit as st
import pandas as pd
from pathlib import path
st.title('dashboard de precios')

csv_path = path('data) / 'precios.csv"

df = pd.read_csv(csv_path, sep=';')

st.dataframe(df)

tiendas = df['tienda'].unique()
tienda_seleccionada = st.selectbox('selecciona una tienda', tiendas)

df_filtrado = df[df['tienda'] == tienda_seleccionada]
st.dataframe(df_filtrado)
