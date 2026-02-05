import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------
# Carregar dados
# -----------------------
df = pd.read_csv("dados/lote_frango.csv")

# -----------------------
# Configuração da página
# -----------------------
st.set_page_config(page_title="Dashboard Granja", layout="wide")

# -----------------------
# Título
# -----------------------
st.title("Dashboard Granja 🐓")

# -----------------------
# Filtros interativos
# -----------------------
st.sidebar.header("Filtros")
idade_max = st.sidebar.slider(
    "Idade máxima (dias)", 
    min_value=int(df["Idade"].min()), 
    max_value=int(df["Idade"].max()), 
    value=int(df["Idade"].max())
)

peso_min = st.sidebar.slider(
    "Peso mínimo (kg)", 
    min_value=float(df["Peso_Medio_kg"].min()), 
    max_value=float(df["Peso_Medio_kg"].max()), 
    value=float(df["Peso_Medio_kg"].min())
)

# Aplicar filtros
df_filtrado = df[(df["Idade"] <= idade_max) & (df["Peso_Medio_kg"] >= peso_min)]

# -----------------------
# Mostrar tabela
# -----------------------
st.subheader("Tabela de Dados")
st.dataframe(df_filtrado)

# -----------------------
# Gráfico interativo
# -----------------------
st.subheader("Evolução do Peso Médio por Idade")
fig = px.line(
    df_filtrado, 
    x="Idade", 
    y="Peso_Medio_kg", 
    markers=True,
    title="Peso Médio dos Frangos ao Longo do Tempo",
    labels={"Idade": "Idade (dias)", "Peso_Medio_kg": "Peso Médio (kg)"}
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------
# Estatísticas rápidas
# -----------------------
st.subheader("Estatísticas Rápidas")
col1, col2, col3 = st.columns(3)
col1.metric("Peso Máximo", f"{df_filtrado['Peso_Medio_kg'].max():.2f} kg")
col2.metric("Peso Médio", f"{df_filtrado['Peso_Medio_kg'].mean():.2f} kg")
col3.metric("Peso Mínimo", f"{df_filtrado['Peso_Medio_kg'].min():.2f} kg")