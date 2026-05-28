import pandas as pd
from src.extract.extrair import extrair,montar_tabela
from src.pipeline.pipeline import pipeline
from src.analytics.metricas import metricas
#from src.analytics.metricas import Obter_Total_Visitas,Obter_Total_Visitantes_Unicos
import  logging

def main():
    arquivo, errors = extrair()

    if errors:
        logging.warning(f"Arquivo com erro {errors}")

    df = montar_tabela(arquivo)
    logging.info(f"Registros carregados {len(df)}")
    logging.info("Pipeline carregado com sucesso")

    df = pipeline(df)
    metrica = metricas(df)

    #res = Obter_Total_Visitantes_Unicos(df ,2026,2)
    #print(res)

    for nome, tabela in metrica.items():

        print(f"{nome} \n")
        print(tabela)

    return df
if __name__ == '__main__':
    main()