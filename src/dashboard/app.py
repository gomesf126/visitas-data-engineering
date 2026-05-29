# =========================================================
# APP.PY
# =========================================================

import pandas as pd
import streamlit as st

from datetime import datetime
from streamlit_autorefresh import st_autorefresh

from src.analytics.metricas import metricas
from src.analytics.charts import *

from src.extract.extrair import extrair, montar_tabela
from src.pipeline.pipeline import pipeline
from src.transform.feature_tempo import mapa_mes


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Dashboard Dinâmico",
    layout="wide"
)

# Atualização automática
st_autorefresh(interval=1000, key="tempo")


# =========================================================
# CACHE
# =========================================================
@st.cache_data
def carregar_dados_projeto():

    arquivo, erros = extrair()

    df = montar_tabela(arquivo)

    df = pipeline(df)

    return df


df = carregar_dados_projeto()


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.header("Filtros")


# ---------------- ANO ----------------
anos_disponiveis = sorted(
    df['Ano'].dropna().unique(),
    reverse=True
)

ano_selecionado = st.sidebar.selectbox(
    "Selecione o Ano",
    anos_disponiveis
)


# ---------------- MÊS ----------------
meses_disponiveis = sorted(
    df[df['Ano'] == ano_selecionado]['Mes_Num']
    .dropna()
    .unique()
)

mes_selecionado = st.sidebar.selectbox(
    "Selecione o Mês",
    meses_disponiveis,
    format_func=lambda x: mapa_mes.get(x, str(x))
)


# =========================================================
# MÉTRICAS
# =========================================================
res = metricas(
    df.copy(),
    ano=ano_selecionado,
    mes=mes_selecionado
)


# =========================================================
# TÍTULO
# =========================================================
nome_mes = mapa_mes.get(mes_selecionado)

st.markdown(
    f"""
    <h1 style='text-align:left;'>
        Dashboard de Visitas - {nome_mes}/{ano_selecionado}
    </h1>
    """,
    unsafe_allow_html=True
)

st.subheader("Indicadores Principais")


# =========================================================
# FUNÇÃO PADRÃO DOS CARDS
# =========================================================
def criar_card(coluna, titulo, valor):

    with coluna:

        st.metric(
            label=titulo,
            value=f"{valor:,}".replace(",", ".")
        )


# =========================================================
# FUNÇÃO PADRÃO DOS GRÁFICOS
# =========================================================
def renderizar_grafico(titulo, figura):

    with st.container(border=True):

        st.subheader(titulo)

        st.plotly_chart(
            figura,
            use_container_width=True
        )


# =========================================================
# CARDS PRINCIPAIS
# =========================================================
total_unicos = res['Obter_Total_Visitantes_Unicos']

total_visitas = res['Obter_Total_Visitas']

agora = datetime.now()


c1, c2, c3, c4 = st.columns(4)

criar_card(
    c1,
    '👥 Visitantes únicos',
    total_unicos
)

criar_card(
    c2,
    '📅 Total de visitas',
    total_visitas
)

with c3:

    st.metric(
        label="📆 Data atual",
        value=agora.strftime("%d/%m/%Y")
    )

with c4:

    st.metric(
        label="⏰ Hora atual",
        value=agora.strftime("%H:%M:%S")
    )


# =========================================================
# CRIAÇÃO DOS GRÁFICOS
# =========================================================
fig_genero = criar_grafico_genero(
    res['total_genero']
)

fig_idade = criar_grafico_idade(
    res['total_idade']
)

fig_diaria = criar_grafico_linha_diaria(
    res['Total_Visitantes_Diaria']
)

fig_hora = criar_graficos_hora(
    res['total_hora']
)


# =========================================================
# SEÇÃO GRÁFICOS
# =========================================================
st.markdown("---")

st.subheader("Análise Gráfica")


# =========================================================
# GRÁFICO PRINCIPAL
# =========================================================
renderizar_grafico(
    "Fluxo Diário de Visitantes",
    fig_diaria
)


# =========================================================
# SEGUNDA LINHA
# =========================================================
g1, g2 = st.columns(2)

with g1:

    renderizar_grafico(
        "Distribuição por Gênero",
        fig_genero
    )

with g2:

    renderizar_grafico(
        "Visitantes por Idade",
        fig_idade
    )


# =========================================================
# TERCEIRA LINHA
# =========================================================
g3, g4 = st.columns(2)

with g3:

    renderizar_grafico(
        "Horário de Pico",
        fig_hora
    )

with g4:

    with st.container(border=True):

        st.subheader("Tabela de Gênero")

        st.dataframe(
            res['total_genero'],
            use_container_width=True
        )