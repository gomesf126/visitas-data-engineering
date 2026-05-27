import pandas as pd

def Total_Genero(df, ano=None, mes=None):
    base= df.copy()
    if ano is not None:
        base = base.query("Ano == @ano")
    if mes is not None:
        base = base.query("Mes_Num == @mes")
    return (
        base
        .groupby('Genero', as_index=False)#as index impede que o genero vire indice
        .agg(
            Total_Clientes = ('Nome','nunique'),
            Tot_Visitas = ('Nome','count')
        )
        .sort_values(['Total_Clientes','Tot_Visitas'], ascending=[False,False])
        .reset_index(drop=True)#impede que o index vire uma coluna
    )
def Total_Visitantes(df):
    Total_visitantes = df['Nome'].nunique()
    return Total_visitantes

def Total_Idade(df, ano=None, mes=None ):
    base= df.copy()
    if ano is not None:
        base = base.query("Ano == @ano")
    if mes is not None:
        base = base.query("Mes_Num == @mes")
    return (base.
            groupby("Idade", as_index=False)
            .agg(Total = ('Nome','nunique'))
            .sort_values('Total', ascending=False)
            .reset_index(drop=True))

def Total_Estado_Pais(df, ano=None, mes=None):
    base= df.copy()
    if ano is not None:
        base = base.query("Ano == @ano")
    if mes is not None:
        base = base.query("Mes_Num == @mes")
    return (base.groupby("Estado_Pais",as_index=False)
            .agg(Total =('Nome','nunique'))
            .sort_values('Total', ascending=False)
            .reset_index(drop=True))


def Total_Etinia(df, ano=None, mes=None):
    base= df.copy()
    if ano is not None:
        base = base.query("Ano == @ano")
    if mes is not None:
        base = base.query("Mes_Num == @mes")

    return (base.groupby("Etinia",as_index=False)
            .agg(Total =('Nome','nunique'))
            .sort_values('Total', ascending=False)
            .reset_index(drop=True))


def Total_Hora(df, ano=None, mes=None):
    base = df.copy()
    if ano is not None:
        base = base.query("Ano == @ano")
    if mes is not None:
        base = base.query("Mes_Num == @mes")

    return (base.groupby("Hora",as_index=False)
            .agg(Total =('Nome','nunique'))
            .sort_values('Total', ascending=False)
            .reset_index(drop=True))


def Total_Livre_Guiada(df, ano=None, mes=None):
    base = df.copy()
    if ano is not None:
        base = base.query("Ano == @ano")
    if mes is not None:
        base = base.query("Mes_Num == @mes")

    return (base.groupby("Livre_Guiado",as_index=False)
            .agg(Total =('Nome','nunique'))
            .sort_values('Total', ascending=False)
            .reset_index(drop=True))

def Total_cupula(df, ano=None, mes=None):
    base = df.copy()
    if ano is not None:
        base = base.query("Ano == @ano")
    if mes is not None:
        base = base.query("Mes_Num == @mes")

    return (base.groupby("Cupula",as_index=False)
            .agg(Total =('Nome','nunique'))
            .sort_values('Total', ascending=False)
            .reset_index(drop=True))


def metricas(df: pd.DataFrame) -> dict:

    return {

        'total_visitantes': Total_Visitantes(df),

        'total_genero': Total_Genero(df),

        'total_idade': Total_Idade(df),

        'total_estado_pais': Total_Estado_Pais(df),

        'total_etinia': Total_Etinia(df),

        'total_hora': Total_Hora(df),

        'total_livre_guiada': Total_Livre_Guiada(df),

        'total_cupula': Total_cupula(df)
    }