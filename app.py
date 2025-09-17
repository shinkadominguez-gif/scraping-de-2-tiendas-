import streamlit as st
import pandas as pd
from pathlib import Path

# --- Cargar CSV ---
csv_path = Path("data") / "precios.csv"
df = pd.read_csv(csv_path, sep=';')

# --- Título ---
st.title("Dashboard de Precios de Tiendas Online")
st.markdown("Visualiza productos y precios de varias tiendas de forma interactiva.")

# --- Filtros ---
tiendas = df['tienda'].unique()
tienda_seleccionada = st.selectbox("Selecciona una tienda", tiendas)

df_filtrado = df[df['tienda'] == tienda_seleccionada]

# Buscador por nombre de producto
busqueda = st.text_input("Buscar producto (nombre)")
if busqueda:
    df_filtrado = df_filtrado[df_filtrado['nombre'].str.contains(busqueda, case=False, na=False)]

# --- Mostrar tabla ---
# Convertir links en clicables
df_filtrado['link'] = df_filtrado['link'].apply(lambda x: f"[Ir al producto]({x})" if x else "")
st.markdown("### Productos")
st.dataframe(df_filtrado[['nombre', 'precio', 'garantia', 'link']], height=400)

# --- Gráfico de precios ---
st.markdown("### Gráfico de precios")
# Convertir precios a float, eliminando símbolos
df_filtrado['precio_num'] = df_filtrado['precio'].str.replace('[^0-9,.]', '', regex=True).str.replace(',', '.').astype(float)
st.bar_chart(df_filtrado.set_index('nombre')['precio_num'])
