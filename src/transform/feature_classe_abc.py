import numpy as np

# Calcula a classificação da Curva ABC baseada no volume acumulado de visitas
def feature_classe_abc(df):
    # Agrupa por cliente único e ordena do maior volume de visitas para o menor
    abc = (
        df.groupby('Nome')['Total_Visitas'].max()
        .reset_index()
        .sort_values(by='Total_Visitas', ascending=False)
        .assign(
            percentual_cliente=lambda x: x['Total_Visitas'] / x['Total_Visitas'].sum(),
            percentual_acumulado=lambda x: x['percentual_cliente'].cumsum()
        )
    )

    # Classifica as faixas de Pareto (20% A, 55% B, 25% C)
    abc['Classe_abc'] = np.select(
        [
            abc['percentual_acumulado'] <= 0.20,
            abc['percentual_acumulado'] <= 0.55
        ],
        ['A', 'B'],
        default='C'
    )

    # Retorna o DataFrame original enriquecido com a classificação ABC por cliente
    return df.merge(
        abc[['Nome', 'percentual_cliente', 'percentual_acumulado', 'Classe_abc']],
        on='Nome',
        how='left'
    )

