import pandas as pd
import numpy as np

# Padroniza os cabeçalhos para Title_Case e remove caracteres especiais
def tratar_colunas(df):
    df = df.rename(columns={
        'Estado/Pais': 'Estado_Pais',
        'Livre/Guiada': 'Livre_Guiado',
        'Cùpula': 'Cupula',
        'Mês': 'Mes'
    })

    df.columns = (df.columns
                  .astype(str)
                  .str.strip()
                  .str.title()
                  .str.replace(' ', '_')
                  .str.replace(r'[^a-zA-Z0-9_]', '', regex=True))
    return df

# Remove espaços e capitaliza os textos categóricos
def tratar_texto(df):
    return (df
    .assign(
        Nome=lambda x: x['Nome'].astype(str).str.strip().str.title(),
        Genero=lambda x: x['Genero'].astype(str).str.strip().str.title(),
        Idade=lambda x: x['Idade'].astype(str).str.strip().str.title(),
        Etinia=lambda x: x['Etinia'].astype(str).str.strip().str.title(),
        Estado_Pais=lambda x: x['Estado_Pais'].astype(str).str.strip().str.title(),
        Livre_Guiado=lambda x: x['Livre_Guiado'].astype(str).str.strip().str.title(),
        Cupula=lambda x: x['Cupula'].astype(str).str.strip().str.title(),
        Hora=lambda x: x['Hora'].astype(str).str.strip().str.title()
    )
    )

# Converte strings de datas em datetime de forma resiliente
def tratar_datas(df):
    data = df['Data_De_Acesso'].astype(str).str.strip()
    mes = df['Mes'].astype(str).str.strip()

    df['Hora'] = df['Hora'].astype(str).str.strip().str.title()

    data_iso = pd.to_datetime(data, format='%Y/%m/%d', errors='coerce')
    data_us = pd.to_datetime(data, format='%m/%d/%Y', errors='coerce')
    data_br = pd.to_datetime(data, format='%d/%m/%Y', errors='coerce')

    df['Data_De_Acesso'] = data_iso.fillna(data_us).fillna(data_br)
    df['Mes'] = pd.to_datetime(mes, format='%m', errors='coerce')
    return df

# Trata nulos temporais e reconstrói o número do mês
def validar_datas(df):
    return (df.assign(
        Data_De_Acesso=lambda x: x['Data_De_Acesso'].fillna(x['Data_De_Acesso'].min()),
        Mes=lambda x: x['Mes'].dt.month.fillna(x['Data_De_Acesso'].dt.month).astype('Int64'),
        Hora=lambda x: x['Hora'].replace(['Nan', 'None', ''], 'Não informado').fillna("Não informado")
    ))

# Preenche nulos categóricos com termos padrão de controle
def tratar_nulos(df):
    return (df.assign(
        Nome=lambda x: x['Nome'].fillna('Nome ausente'),
        Genero=lambda x: x['Genero'].fillna('Sem genero'),
        Idade=lambda x: x['Idade'].fillna("A declarar"),
        Etinia=lambda x: x['Etinia'].fillna('Sem etinia'),
        Estado_Pais=lambda x: x['Estado_Pais'].fillna('A declarar'),
        Livre_Guiado=lambda x: x['Livre_Guiado'].fillna('Ausente'),
        Cupula=lambda x: x['Cupula'].fillna('Ausente')
    ))
