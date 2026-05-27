from src.transform.limpeza import *
from src.transform.feature_cliente import feature_cliente
from src.transform.feature_tempo import feature_tempo
from src.transform.feature_churn import churn_cliente
from src.transform.feature_classe_abc import feature_classe_abc
CLEANING =[
    tratar_colunas,
    tratar_texto,
    tratar_datas,
    validar_datas,
    tratar_nulos
]
ENGINEERING = [
    feature_tempo,
    feature_cliente,
    churn_cliente,
    feature_classe_abc
]

def aplicar_pipeline(df, etapas):
    for funcao in etapas:
        df = funcao(df)
    return df



