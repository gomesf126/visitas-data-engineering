import pandas as pd

from src.analytics.metricas import metricas
from src.extract.extrair import extrair,montar_tabela
from src.pipeline.pipeline import pipeline
import streamlit as st
from src.analytics.charts import *
from src.transform.feature_tempo import mapa_mes

st.set_page_config(page_title="Dashboard Dinâmico", layout="wide")

# --- 1. CARREGAMENTO DOS DADOS COM CACHE ---
# Isolar o pipeline garante que a leitura do arquivo aconteça apenas uma vez na memória
@st.cache_data
def carregar_dados_projeto():
    arquivo, erros = extrair()
    df = montar_tabela(arquivo)
    df = pipeline(df)
    return df

df= carregar_dados_projeto()

# --- . CONFIGURAÇÃO DOS FILTROS (SIDEBAR) ---
st.sidebar.header("Filtros")


ano_disponivel = sorted(df['Ano'].unique(), reverse=True)
ano_selecionado = st.sidebar.selectbox("Selecione o Ano", ano_disponivel)


meses_disponivel = sorted(df[df['Ano'] == ano_selecionado]['Mes_Num'].dropna().unique())
mes_selecionado = st.sidebar.selectbox("Selecione o Mês", meses_disponivel,format_func= lambda x:mapa_mes.get(x, str(x)))


#-------------PROCESSAR DADOS METRICS-------------
res = metricas(df.copy() , ano =ano_selecionado, mes=mes_selecionado)

# --- . RENDERIZAÇÃO DA INTERFACE (TÍTULOS FIRST) --
#st.title(f"Dashboard de Visitas {mes_selecionado}/{ano_selecionado}")
st.markdown(
    f"<h1 style='text-align: left;'>Dashboard de Visitas {mes_selecionado:02d}/{ano_selecionado}</h1>",
    unsafe_allow_html=True
)
st.subheader("Indicadores Principais")

#------------------------CARDS---------------------
c1,c2,c3 = st.columns(3)

with c1:
    total_unicos = res['Obter_Total_Visitantes_Unicos']
    st.metric(
        label = '👥 Visitantes únicos',
        value=f"{total_unicos:,}"#.replace(',','.')
    )
with c2:
    total_mes = res['Obter_Total_Visitas']
    st.metric(
        label='📅 Total de visitas no mês',
        value=f"{total_mes:,}"#.replace(',','.')
    )


















