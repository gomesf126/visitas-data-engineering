import pandas as pd
import numpy as np

mapa_semana = {
    'Monday': 'Segunda-Feira',
    'Tuesday': 'Terça-Feira',
    'Wednesday': 'Quarta-Feira',
    'Thursday': 'Quinta-Feira',
    'Friday': 'Sexta-Feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

mapa_mes = {
    1:'Jan', 2:'Fev', 3:'Mar', 4:'Abr', 5:'Mai', 6:'Jun',
    7:'Jul', 8:'Ago', 9:'Set', 10:'Out', 11:'Nov', 12:'Dez'
}
mapa_trimestre = {
 1:'1° Trimestre',
 2:'2° Trimestre',
 3:'3° Trimestre',
 4:'4° Trimestre'
}
# Desmembra a data de acesso em componentes calendários e traduz dias e meses
def feature_tempo(df):
    return (df
        .assign(
            Dia     = lambda x: x['Data_De_Acesso'].dt.day,
            Mes     = lambda x: x['Data_De_Acesso'].dt.month.map(mapa_mes),
            Ano     = lambda x: x['Data_De_Acesso'].dt.year,
            Mes_Num = lambda x: x['Data_De_Acesso'].dt.month,
            Semana  = lambda x: x['Data_De_Acesso'].dt.day_name().map(mapa_semana),
            Trimestre = lambda x: x['Data_De_Acesso'].dt.quarter.map(mapa_trimestre),
            Quinzena  = lambda x: np.where(x['Data_De_Acesso'].dt.day <=15 ,'1° Quinzena', '2° Quinzena')
        )
    )
