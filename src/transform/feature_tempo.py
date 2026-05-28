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
    1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho',
    7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'
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
            Dia     = lambda x: x['Data_De_Acesso'].dt.day.astype('Int64'),
            Mes     = lambda x: x['Data_De_Acesso'].dt.month.map(mapa_mes),
            Ano=lambda x: x['Data_De_Acesso'].dt.year.astype('Int64'),
            Mes_Num=lambda x: x['Data_De_Acesso'].dt.month.astype('Int64'),
            Semana  = lambda x: x['Data_De_Acesso'].dt.day_name().map(mapa_semana),
            Trimestre = lambda x: x['Data_De_Acesso'].dt.quarter.map(mapa_trimestre),
            Quinzena  = lambda x: np.where(x['Data_De_Acesso'].dt.day <=15 ,'1° Quinzena', '2° Quinzena')
        )
    )
