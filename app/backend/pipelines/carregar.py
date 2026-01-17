import pandas as pd


def carregar_csv(df: pd.DataFrame) -> None:
    """
    Função para carregar o DataFrame em um arquivo CSV

    :param df: DataFrame 
    :type df: pd.DataFrame
    :return: None
    :rtype: None
    """
    # Criando o arquivo CSV
    df.to_csv('data/output/jogadores.csv', index=False, encoding='utf-8-sig')