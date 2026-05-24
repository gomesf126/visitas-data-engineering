import numpy as np
import pandas as pd

# Gera segmentações demográficas e perfis comportamentais dos visitantes
def feature_cliente(df):
    return (df
    .assign(
        Total_Visitas = lambda x: x.groupby('Nome')['Nome'].transform('count'),
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

        Perfil_visita=lambda x: (
                x['Genero'].astype(str).str.strip() + ' - ' +
                x['Livre_Guiado'].astype(str).str.strip()
        ),

        Local_Visitante=lambda x: np.select(
            [
                x['Estado_Pais'] == "Df",
                x['Estado_Pais'] == "Outros Estados",
                x['Estado_Pais'] == "Outros Paises"
            ],
            ["DF", "Outros Estados", "Outros Paises"],
            default="Não informado"
        ),

        Tipo_Guia=lambda x: np.select(
            [
                x['Livre_Guiado'] == "Livre",
                x['Livre_Guiado'] == "Guiado"
            ],
            ["Livre", "Guiado"],
            default="Não informado"
        ),

        Cupula_Visita=lambda x: np.select(
            [
                x['Cupula'] == 'Sim',
                x['Cupula'] == 'Não'
            ],
            ['Sim', 'Não'],
            default="Não informado"
        ),

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
    .assign(Hora_num=lambda x: x['Hora'].astype(str).str.strip())
    .assign(
        Hora_visita=lambda x: np.where(
            x['Hora_num'].isin(['11:00', '14:30', '16:00', '17:00', '18:00', 'Extra']),
            x['Hora_num'],
            "Não informado"
        )
    )
)
