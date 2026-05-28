import plotly.express as px


def criar_grafico_genero(df_genero):
    return px.pie(
        df_genero,
        values='Total_de_Visitantes',
        names='Genero',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Safe
    )
def criar_grafico_idade(df_idade):
    return px.bar(
        df_idade,
        x='Idade',
        y='Total',
        color='Total',
        color_continuous_scale='Blues'
    )
def criar_grafico_linha_diaria(df_diaria):
    return px.line(
        df_diaria,
        x='Dia',
        y='Total',
        markers=True
    )

def criar_graficos_hora(df_hora):
    return px.bar(
        df_hora,
        x='Hora',
        y='Total',
        color_discrete_sequence=['#4B0082']
    )

