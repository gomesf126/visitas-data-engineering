import numpy as np

# Calcula indicadores de retenção (Recência) e fidelidade (Frequência) do visitante
def churn_cliente(df):
    data_maxima = df['Data_De_Acesso'].max()

    return (df
        .assign(
            Ultima_visita    = lambda x: x.groupby('Nome')['Data_De_Acesso'].transform('max'),
            Data_Atual       = lambda x: data_maxima,
            Dias_Sem_visitas = lambda x: (data_maxima - x['Ultima_visita']).dt.days,
            Total_Visitas    = lambda x: x.groupby('Nome')['Nome'].transform('count')
        )
        .assign(
            Segmento_Churn = lambda x: np.select(
                [
                    (x['Dias_Sem_visitas'] >= 0) & (x['Dias_Sem_visitas'] < 30),
                    (x['Dias_Sem_visitas'] >= 30) & (x['Dias_Sem_visitas'] <= 40),
                    x['Dias_Sem_visitas'] > 40
                ],
                ['Ativo', 'Em Risco', 'Churn'],
                default="Não informado"
            )
        )
        .assign(
            Segmento_Fidelidade = lambda x: np.select(
                [
                    x['Total_Visitas'] == 1,
                    x['Total_Visitas'].between(2, 5),
                    x['Total_Visitas'] > 5
                ],
                ['Novo', 'Recorrente', 'Fiel'],
                default="Não informado"
            )
        )
    )










