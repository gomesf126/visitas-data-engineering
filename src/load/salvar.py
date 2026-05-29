import pandas as pd
from src.config.caminhos import DATA_PROCESSED
import logging
logger = logging.getLogger(__name__)


def salvar_df(df, nome_arquivo='Arquivo_tratado.csv'):
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    caminho =  DATA_PROCESSED / nome_arquivo
    df.to_csv(caminho, index=False, encoding='utf-8-sig')
    logging.info("Arquivo salvo em %s",caminho)


def salvar_metricas(metricas: dict):

    DATA_PROCESSED.mkdir( parents=True, exist_ok=True)

    for name, dado in metricas.items():
        # Salva apenas DataFrames
        if isinstance(dado, pd.DataFrame):

            caminho = DATA_PROCESSED / f"{name}.csv"

            dado.to_csv(caminho, index=False, encoding='utf-8-sig' )

            logger.info('Métrica %s salva em %s',name, caminho)

        else:

            logger.warning( '%s ignorado. Tipo encontrado: %s',name,type(dado)
            )