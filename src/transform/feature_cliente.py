import numpy as np
import pandas as pd

from src.extract.extrair import extrair, montar_tabela
from src.transform.limpeza import *
from src.pipeline.pipeline import pipeline


def feature_cliente(df):
    """Gera novas colunas de segmentação e perfil com base nos dados tratados dos visitantes."""
    return (df
    .assign(
        # ------------- IDADE E SEGMENTAÇÃO -------------
        Idade=lambda x: x['Idade'].astype(str).str.strip(),
        Segmento_Idade=lambda x: np.select(
            [
                x['Idade'].str.contains('0-12', na=False),
                x['Idade'].str.contains('13-17', na=False),
                x['Idade'].str.contains('18-59', na=False),
                x['Idade'].str.contains('60  +', na=False)
            ],
            ["Criança", "Jovem", "Adulto", "Senior"],
            default='Não informado'
        ),

        # ------------ PERFIL DOS VISITANTES -----------
        Perfil_visita=lambda x: (
                x['Genero'].astype(str).str.strip() + ' - ' +
                x['Livre_Guiado'].astype(str).str.strip()
        ),

        # ------------- VISITANTES POR REGIÃO E INTERNACIONAL -------------
        Local_Visitante=lambda x: np.select(
            [
                x['Estado_Pais'] == "Df",
                x['Estado_Pais'] == "Outros Estados",
                x['Estado_Pais'] == "Outros Paises"
            ],
            ["DF", "Outros Estados", "Outros Paises"],
            default="Não informado"
        ),

        # -------------- PUBLICO GUIADO -------------------
        Livre_Guiado=lambda x: x['Livre_Guiado'].astype(str).str.strip(),
        Tipo_Guia=lambda x: np.select(
            [
                x['Livre_Guiado'] == "Livre",
                x['Livre_Guiado'] == "Guiado"
            ],
            ["Livre", "Guiado"],
            default="Não informado"
        ),

        # ---------------- VISITOU CÚPULA ---------------
        Cupula_Visita=lambda x: np.select(
            [
                x['Cupula'] == 'Sim',
                x['Cupula'] == 'Não'
            ],
            ['Sim', 'Não'],
            default="Não informado"
        ),

        # ---------------- ETNIA ---------------
        Tipo_Etinia=lambda x: np.select(
            [
                x['Etinia'] == 'Branco',
                x['Etinia'] == 'Negro',
                x['Etinia'] == 'Outro'
            ],
            ["Branco", "Negro", "Outro"],
            default="Não informado"
        )
    )
    # ------------- REAPROVEITAMENTO DE COLUNAS (HORA) -------------
    .assign(Hora_num=lambda x: x['Hora'].astype(str).str.strip())
    .assign(
        Hora_visita=lambda x: np.where(
            x['Hora_num'].isin(['11:00', '14:30', '16:00', '17:00', '18:00', 'Extra']),
            x['Hora_num'],
            "Não informado"
        )
    )
    )


# ------------- FLUXO DE EXECUÇÃO PRINCIPAL -------------
arquivo, erros = extrair()
df = montar_tabela(arquivo)
df = tratar_colunas(df)
df = pipeline(df)
df = feature_cliente(df)

# ------------- VISUALIZAÇÃO DOS RESULTADOS -------------
print("\n--- COLUNAS DO DATAFRAME ---")
print(df.columns)

print("\n--- PRÉVIA DOS DADOS (700 LINHAS) ---")
print(df.head(700))

print("\n--- VALORES ÚNICOS DE ESTADO_PAIS ---")
print(df['Estado_Pais'].unique())

print("\n--- COLUNAS DE SEGMENTAÇÃO CRIADAS ---")
print(df[['Perfil_visita', 'Tipo_Guia', 'Local_Visitante', 'Cupula_Visita', 'Tipo_Etinia']])

print("\n--- FILTRO DE HORÁRIOS EXTRA ---")
print(df.query("Hora_visita == 'Extra'")[['Hora_visita']])
