import pandas as pd
from src.extract.extrair import extrair,montar_tabela
from src.pipeline.pipeline import pipeline
import streamlit as st
from src.analytics.charts import *

st.set_page_config(page_title="Dashboard Dinâmico", layout="wide")

arquivo, erros = extrair()
df= montar_tabela(arquivo)
df = pipeline(df)

print(df.columns)

# 1. Filtro de Ano (Pega os anos únicos da base + opção "Todos")
ano_disponivel = sorted(df['Ano'].unique(), reverse=True)
ano_selecionado = st.selectbox("Selecione o Ano", ano_disponivel)

# 2. Filtro de Mês (Filtra os meses disponíveis com base no ano escolhido)
meses_disponivel = sorted(df[df['Ano'] == ano_selecionado]['Mes_Num'].dropna().unique())
mes_selecionado = st.selectbox("Selecione o Mês", meses_disponivel)



