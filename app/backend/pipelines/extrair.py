import os
import glob
import pandas as pd
from typing import List


def extrair_csv(path: str) -> List[pd.DataFrame]:
    """
    Função para extrair os csv
    
    :param path: caminho de onde está os csv
    :type path: str
    :return: lista de dataframe com o conteúdo lido
    :rtype: List[pd.DataFrame]
    """
    # Extraindo os arquivos separadamente
    arquivo_jog_mas = os.path.join(path, 'male_players.csv') # 
    arquivo_jog_fem = os.path.join(path, 'female_players.csv')   

    # Criando os df separado por gênero
    df_masc = pd.read_csv(arquivo_jog_mas, low_memory=False)
    df_fem = pd.read_csv(arquivo_jog_fem, low_memory=False)


    # Retornando os df  
    return df_masc, df_fem


