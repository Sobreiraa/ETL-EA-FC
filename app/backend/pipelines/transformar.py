from app.backend.pipelines.extrair import extrair_csv
import pandas as pd


def unir_dataframes(df_masc: pd.DataFrame, df_fem: pd.DataFrame) -> pd.DataFrame:
    """
    Função para unir os dataframe
    
    :param df_mas: df masculino
    :param df_fem: df feminino
    :return: DataFrame transformado e limpo
    :rtype: DataFrame
    """
    # Criando a coluna dos generos
    df_masc["genero"] = "Masculino"
    df_fem["genero"] = "Feminino" 

    # Unificando os DataFrames
    df_unico = pd.concat([df_masc, df_fem], ignore_index=True)

    # Retornando o DataFrame unificado
    return df_unico


def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Função para limpar os dados do DataFrame

    :param df_total: DataFrame unificado
    :type df_total: pd.DataFrame
    :return: Retorna o DataFrame limpo
    :rtype: DataFrame
    """
    # Lista de colunas que desejo manter
    colunas_manter = [
                    "short_name", "long_name", "overall", "potential",
                    "value_eur", "age", "dob", "height_cm", "weight_kg", "club_name",
                    "league_name", "nationality_name", "preferred_foot", "pace", "shooting", "passing",
                    "dribbling", "defending", "physic", "genero"]

    # Criando o df_limpo com apenas as colunas desejadas
    df_limpo = df[colunas_manter].copy()

    # Renomeando as colunas para português
    df_limpo.columns = [
                   "nome", "nome_completo", "overall", "potencial",
                   "valor_eur", "idade", "data_nascimento", "altura_cm", "peso_kg",
                   "clube", "liga", "nacionalidade", "pe_preferido", "ritmo", "chute",
                   "passe", "drible", "defesa", "fisico", "genero"]
    
    # Transformando a coluna data_nascimento no type datetime
    df_limpo["data_nascimento"] = pd.to_datetime(df_limpo["data_nascimento"])
    
    # Traduzindo os valores da coluna pe_preferido
    df_limpo["pe_preferido"] = df_limpo["pe_preferido"].replace({
                   "Left": "Esquerdo",
                   "Right": "Direito"})
    
    # Retornando o df com apenas as informações necessárias
    return df_limpo

