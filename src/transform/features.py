from src.transform.limpeza import *

CLEANING =[
    tratar_colunas,
    tratar_texto,
    tratar_datas,
    validar_datas,
    tratar_nulos
]
ENGINEERING = [

]

def aplicar_pipeline(df, etapas):
    for funcao in etapas:
        df = funcao(df)
    return df



