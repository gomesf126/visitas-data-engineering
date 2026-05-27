from src.extract.extrair import extrair,montar_tabela
from src.pipeline.pipeline import pipeline
import streamlit as st
from src.analytics.graficos import grafico_Total_Visitantes


arquivo, erros = extrair()
df= montar_tabela(arquivo)
df = pipeline(df)

print(df.columns)

mes = st.selectbox('Selecione o mês', sorted(df['Mes_Num'].unique()))
ano = st.selectbox('Selecione o ano', sorted(df['Ano'].unique()))
fig = grafico_Total_Visitantes(df, ano, mes)
st.plotly_chart(fig, use_container_width=True)
