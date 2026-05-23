from src.config.caminhos import DATA_RAW
import pandas as pd
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def ler_arquivo(arquivo):
    try:
        logger.info(f"Lendo o arquivo {arquivo}")
        df = pd.read_csv(arquivo, sep=',', encoding='utf-8')
        logger.info('Arquivo lido com sucesso!')
    except Exception as erro:
        logger.error(f"Erro ao ler o arquivo {arquivo} : {erro}")
        raise
    return df


def validar_coluna(df, arquivo):
    SCHEMA = ['Data de acesso ', 'Nome', 'Genero', 'Idade', 'Etinia', 'Estado/Pais',
             'Livre/Guiada', 'Cùpula', 'Hora', 'Mês']
    coluna = set(df.columns)
    obrigatorias = set(SCHEMA)

    faltantes = obrigatorias-coluna
    coluna_extra = coluna-obrigatorias

    if faltantes:
        raise ValueError(f"Arquivo {arquivo} com coluna(s) {faltantes} faltando")
    if coluna_extra:
        logger.warning(f'Arquivo {arquivo} com coluna(s) extras: {coluna_extra}')
    return df


def extrair():
    tabelas=[]
    arquivo_falhos=[]
    try:
        for arquivo in DATA_RAW.glob("*.csv"):

            df = ler_arquivo(arquivo)
            df = validar_coluna(df, arquivo)
            logger.info(f"Arquivo {arquivo.name} validado com sucesso")
            tabelas.append(df)

    except Exception as erros:
            logger.error(f"Falha ao processar o arquivo {arquivo}: {erros}")
            arquivo_falhos.append(arquivo)

    if not tabelas:
        raise ValueError("Nenhum arquivo carregado!")
    logger.info(f"{len(tabelas)} Arquivos carregados com sucesso!")

    return tabelas, arquivo_falhos

def montar_tabela(tabela):
    if not tabela:
        raise ValueError(f"Erro ao montar a tabela {tabela} ")
    return pd.concat(tabela, ignore_index=True)


