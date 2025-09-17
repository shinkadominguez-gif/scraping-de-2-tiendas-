import streamlit as st
import pandas as pd

st.title('dashboard de precios')

df = pd.read_csv('data\precios.csv', sep=';')

st.dataframe(df)

tiendas = df['tienda'].unique()
tienda_seleccionada = st.selectbox('selecciona una tienda', tiendas)

df_filtrado = df[df['tienda'] == tienda_seleccionada]
st.dataframe(df_filtrado)
