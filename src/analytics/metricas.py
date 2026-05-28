import pandas as pd

# --- NOVA FUNÇÃO DE FILTRAGEM CENTRALIZADA ---
def filtrar_base(df, ano=None, mes=None):
    base = df.copy()
    if ano is not None:
        base = base.query("Ano == @ano")
    if mes is not None:
        base = base.query("Mes_Num == @mes")
    return base


# --- FUNÇÕES PRINCIPAIS SIMPLIFICADAS ---

# 1. Definição das funções de contagem
def Obter_Total_Visitas(df, ano=None, mes=None):
    base = filtrar_base(df, ano, mes)
    return base['Nome'].count() # Volume total de entradas

def Obter_Total_Visitantes_Unicos(df, ano=None, mes=None):
    base = filtrar_base(df, ano, mes)
    return base['Nome'].nunique() # Quantidade de pessoas físicas


def Total_Genero(df, ano=None, mes=None):
    base = filtrar_base(df, ano, mes)
    return (
        base
        .groupby('Genero', as_index=False)
        .agg(Total_de_Visitantes = ('Nome','nunique'))
        .sort_values(['Total_de_Visitantes'], ascending=[False])
        .reset_index(drop=True)
    )

def Total_Idade(df, ano=None, mes=None):
    base = filtrar_base(df, ano, mes)
    return (
        base
        .groupby("Idade", as_index=False)
        .agg(Total = ('Nome','nunique'))
        .sort_values('Total', ascending=False)
        .reset_index(drop=True)
    )

def Total_Estado_Pais(df, ano=None, mes=None):
    base = filtrar_base(df, ano, mes)
    return (
        base
        .groupby("Estado_Pais", as_index=False)
        .agg(Total = ('Nome','nunique'))
        .sort_values('Total', ascending=False)
        .reset_index(drop=True)
    )

def Total_Etinia(df, ano=None, mes=None):
    base = filtrar_base(df, ano, mes)
    return (
        base
        .groupby("Etinia", as_index=False)
        .agg(Total = ('Nome','nunique'))
        .sort_values('Total', ascending=False)
        .reset_index(drop=True)
    )

def Total_Hora(df, ano=None, mes=None):
    base = filtrar_base(df, ano, mes)
    return (
        base
        .groupby("Hora", as_index=False)
        .agg(Total = ('Nome','nunique'))
        .sort_values('Total', ascending=False)
        .reset_index(drop=True)
    )

def Total_Livre_Guiada(df, ano=None, mes=None):
    base = filtrar_base(df, ano, mes)
    return (
        base
        .groupby("Livre_Guiado", as_index=False)
        .agg(Total = ('Nome','nunique'))
        .sort_values('Total', ascending=False)
        .reset_index(drop=True)
    )

def Total_cupula(df, ano=None, mes=None):
    base = filtrar_base(df, ano, mes)
    return (
        base
        .groupby("Cupula", as_index=False)
        .agg(Total = ('Nome','nunique'))
        .sort_values('Total', ascending=False)
        .reset_index(drop=True)
    )

def Total_Visitantes_Diaria(df, ano=None, mes=None):
    base = filtrar_base(df, ano, mes)
    return (
        base
        .groupby("Dia", as_index=False)
        .agg(Total = ('Nome','nunique'))
        .sort_values('Dia', ascending=True)
        .reset_index(drop=True)
    )

def metricas(df: pd.DataFrame, ano=None, mes=None) -> dict:
    return {
        'Obter_Total_Visitantes_Unicos': Obter_Total_Visitantes_Unicos(df, ano, mes),
        'Obter_Total_Visitas': Obter_Total_Visitas(df, ano, mes),
        'total_genero': Total_Genero(df, ano, mes),
        'total_idade': Total_Idade(df, ano, mes),
        'total_estado_pais': Total_Estado_Pais(df, ano, mes),
        'total_etinia': Total_Etinia(df, ano, mes),
        'total_hora': Total_Hora(df, ano, mes),
        'total_livre_guiada': Total_Livre_Guiada(df, ano, mes),
        'total_cupula': Total_cupula(df, ano, mes),
        'Total_Visitantes_Diaria': Total_Visitantes_Diaria(df, ano, mes)
    }
