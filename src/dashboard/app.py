import sys
from pathlib import Path

#sys.path.append(str(Path(__file__).resolve().parents[2]))

import pandas as pd
import streamlit as st

from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from zoneinfo import ZoneInfo
hora_brasil = datetime.now(
    ZoneInfo("America/Sao_Paulo")
)

from src.analytics.metricas import metricas
from src.analytics.charts import *

from src.extract.extrair import extrair, montar_tabela
from src.pipeline.pipeline import pipeline
from src.transform.feature_tempo import mapa_mes

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Dashboard Dinâmico",
    layout="wide"
)
# AUTO REFRESH
# Atualiza a cada 1 minuto
st_autorefresh(
    interval=60 * 1000,
    key="tempo"
)

# CACHE BASE
@st.cache_data
def carregar_dados_projeto():
    arquivo, erros = extrair()
    df = montar_tabela(arquivo)
    df = pipeline(df)
    return df

# CACHE MÉTRICAS
@st.cache_data
def carregar_metricas(df, ano, mes):
    return metricas(
        df.copy(),
        ano=ano,
        mes=mes
    )

# CACHE GRÁFICOS
@st.cache_data
def carregar_graficos(res):
    return {
        'fig_genero': criar_grafico_genero(res['total_genero']),
        'fig_idade':  criar_grafico_idade(res['total_idade']),
        'fig_diaria': criar_grafico_linha_diaria( res ['total_visitantes_diaria']),
        'fig_hora':   criar_graficos_hora(res['total_hora']),
        'fig_cupula': criar_grafico_cupula(res['total_cupula']),
        'fig_grafico_livre_guiado' :criar_grafico_livre_guiado(res['total_livre_guiada'])
    }
# CARREGAMENTO DA BASE
df = carregar_dados_projeto()

# ------------------------------SIDEBAR--------------------------

st.sidebar.header("Filtros")

anos_disponiveis = sorted(df['Ano'].dropna().unique(),reverse=True)
ano_selecionado = st.sidebar.selectbox("Selecione o Ano", anos_disponiveis)

meses_disponiveis = sorted(df[df['Ano'] == ano_selecionado]['Mes_Num'].dropna().unique())
mes_selecionado = st.sidebar.selectbox(
    "Selecione o Mês", meses_disponiveis, format_func=lambda x: mapa_mes.get(x, str(x)) )

# -----------------------------MÉTRICAS--------------------------
res = carregar_metricas(df, ano_selecionado, mes_selecionado)

# GRÁFICOS
graficos = carregar_graficos(res)



# TÍTULO
nome_mes = mapa_mes.get(mes_selecionado)

st.markdown(
    f"""
    <h1 style='text-align:center;'>
        Dashboard de Visitas - {nome_mes}/{ano_selecionado}
    </h1>
    """,
    unsafe_allow_html=True
)

st.subheader("Indicadores Principais")

# FUNÇÃO GRÁFICO
def renderizar_grafico(titulo, figura):
    with st.container(border=True):
        st.subheader(titulo)
        st.plotly_chart( figura,use_container_width=True)


# MÉTRICAS PRINCIPAIS PARA OS CARDS
total_unicos = res['Obter_Total_Visitantes_Unicos']
total_visitas = res['Obter_Total_Visitas']

# CARDS
c1, c2, c3, c4 = st.columns(4)


# CARD VISITANTES ÚNICOS
with c1:
    st.metric('👥 Visitantes únicos', total_unicos)

with c2:
    st.metric('📅 Total de visitas', total_visitas)

# CARD DATA
with c3:

    st.metric(
        label="📆 Data atual",
        value=datetime.now().strftime("%d/%m/%Y")
    )

# CARD HORA

with c4:
    st.metric(
        label="⏰ Hora atual",
        value=hora_brasil.strftime("%H:%M")
    )

# SEÇÃO GRÁFICOS

st.markdown("---")

st.subheader("Análise Gráfica")

# GRÁFICO PRINCIPAL

renderizar_grafico(
    "Fluxo Diário de Visitantes",
    graficos['fig_diaria']
)

# SEGUNDA LINHA

g1, g2 , g3 = st.columns(3)

with g1:
    renderizar_grafico(
        "Distribuição por Gênero",
        graficos['fig_genero']
    )

with g2:
    renderizar_grafico(
        "Visitantes por Idade",
        graficos['fig_idade']
    )
with g3:
    with st.container(border=True):
        st.subheader("Horário de Pico",)
        st.plotly_chart(graficos['fig_hora'], use_container_width=True)

# TERCEIRA LINHA

g4, g5  , g6= st.columns(3)

with g4:
    with st.container(border=True):
        st.subheader('Visitas por cúpula')
        st.plotly_chart( graficos['fig_cupula'], use_container_width=True)

with g5:
    with st.container(border=True):
        st.subheader('Visita livre ou guiada')
        st.plotly_chart(graficos['fig_grafico_livre_guiado'], use_container_width=True)

with g6:
        with st.container(border=True):
            st.subheader("Tabela de Gênero")
            st.dataframe(
                res['total_genero'], use_container_width=True
            )
st.write(list(res.keys()))