def feature_cliente(df):
    return df.assign(
        Total_Visitas=lambda x: x.groupby('Nome')['Nome'].transform('count'),
        Total_Diaria = lambda x: x.groupby('Dia')['Nome'].transform('count')
    )
