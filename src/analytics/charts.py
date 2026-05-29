# =========================================================
# CHARTS.PY
# =========================================================

import plotly.express as px


# =========================================================
# GRÁFICO GÊNERO
# =========================================================
def criar_grafico_genero(df_genero):

    fig = px.pie(
        df_genero,
        values='Total_de_Visitantes',
        names='Genero',
        hole=0.55,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_traces(
        textinfo='percent+label'
    )

    fig.update_layout(
        title='Distribuição por Gênero',
        title_x=0.5,
        legend_orientation='h',
        template='plotly_white'
    )

    return fig


# =========================================================
# GRÁFICO IDADE
# =========================================================
def criar_grafico_idade(df_idade):

    fig = px.bar(
        df_idade,
        x='Idade',
        y='Total',
        text_auto=True
    )

    fig.update_layout(
        title='Visitantes por Idade',
        title_x=0.5,
        xaxis_title='Idade',
        yaxis_title='Total de Visitantes',
        template='plotly_white'
    )

    fig.update_traces(
        hovertemplate=
        '<b>Idade:</b> %{x}<br><b>Total:</b> %{y}<extra></extra>'
    )

    return fig


# =========================================================
# GRÁFICO LINHA DIÁRIA
# =========================================================
def criar_grafico_linha_diaria(df_diaria):

    fig = px.line(
        df_diaria,
        x='Dia',
        y='Total',
        markers=True
    )

    fig.update_layout(
        title='Fluxo Diário de Visitantes',
        title_x=0.5,
        xaxis_title='Dia',
        yaxis_title='Total',
        template='plotly_white'
    )

    fig.update_traces(
        line=dict(width=4),
        hovertemplate=
        '<b>Dia:</b> %{x}<br><b>Total:</b> %{y}<extra></extra>'
    )

    return fig


# =========================================================
# GRÁFICO HORA
# =========================================================
def criar_graficos_hora(df_hora):

    fig = px.bar(
        df_hora,
        x='Hora',
        y='Total',
        text_auto=True
    )

    fig.update_layout(
        title='Horário de Pico',
        title_x=0.5,
        xaxis_title='Hora',
        yaxis_title='Visitantes',
        template='plotly_white'
    )

    fig.update_traces(
        hovertemplate=
        '<b>Hora:</b> %{x}<br><b>Total:</b> %{y}<extra></extra>'
    )

    return fig