from src.analytics.metricas import Total_Visitas
import plotly.express as px


def grafico_Total_Visitantes(df, ano=None, mes=None):

    base = Total_Visitas(df, ano, mes)

    fig = px.bar(
        base,
        x='Total_Visitas',
        y='Mes_Num',
        color='Ano',
        text='Total_Visitas',
        orientation='h',
        title='Quantidade de visitantes por período'
    )

    fig.update_traces(
        textposition='outside'
    )

    fig.update_layout(
        xaxis_title='Total de visitantes',
        yaxis_title='Período'
    )

    return fig