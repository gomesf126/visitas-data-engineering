import pandas as pd
import numpy as np


def tratar_colunas(df):
    """Padroniza os nomes das colunas mapeando termos específicos para o formato Title_Case com underscores."""
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


def tratar_texto(df):
    """Remove espaços em branco residuais e padroniza as colunas de texto para o formato capitalizado."""
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


def tratar_datas(df):
    """Converte strings de datas em objetos datetime válidos e limpa a coluna de horas como string pura."""
    data = df['Data_De_Acesso'].astype(str).str.strip()
    mes = df['Mes'].astype(str).str.strip()

    df['Hora'] = df['Hora'].astype(str).str.strip().str.title()

    data_iso = pd.to_datetime(data, format='%Y/%m/%d', errors='coerce')
    data_us = pd.to_datetime(data, format='%m/%d/%Y', errors='coerce')
    data_br = pd.to_datetime(data, format='%d/%m/%Y', errors='coerce')

    df['Data_De_Acesso'] = data_iso.fillna(data_us).fillna(data_br)
    df['Mes'] = pd.to_datetime(mes, format='%m', errors='coerce')
    return df


def validar_datas(df):
    """Preenche lacunas de datas vazias, reconstrói meses faltantes e padroniza textos de horas ausentes."""
    return (df.assign(
        Data_De_Acesso=lambda x: x['Data_De_Acesso'].fillna(x['Data_De_Acesso'].min()),
        Mes=lambda x: x['Mes'].dt.month.fillna(x['Data_De_Acesso'].dt.month).astype('Int64'),
        Hora=lambda x: x['Hora'].replace(['Nan', 'None', ''], 'Não informado').fillna("Não informado")
    ))


def tratar_nulos(df):
    """Substitui valores nulos de colunas categóricas por termos textuais padrão de controle."""
    return (df.assign(
        Nome=lambda x: x['Nome'].fillna('Nome ausente'),
        Genero=lambda x: x['Genero'].fillna('Sem genero'),
        Idade=lambda x: x['Idade'].fillna("A declarar"),
        Etinia=lambda x: x['Etinia'].fillna('Sem etinia'),
        Estado_Pais=lambda x: x['Estado_Pais'].fillna('A declarar'),
        Livre_Guiado=lambda x: x['Livre_Guiado'].fillna('Ausente'),
        Cupula=lambda x: x['Cupula'].fillna('Ausente')
    ))
