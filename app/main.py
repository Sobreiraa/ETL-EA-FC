from app.backend.pipelines.extrair import extrair_csv
from app.backend.pipelines.transformar import unir_dataframes, limpar_dados
from app.backend.pipelines.carregar import carregar_csv


def main():
    # Caminho onde estão os arquivos CSV de entrada
    path_csv = "data/input"

    # Extração
    df_masc, df_fem = extrair_csv(path_csv)

    # Transformação - unir dataframes
    df_unificado = unir_dataframes(df_masc, df_fem)

    # Transformação - limpeza e padronização
    df_limpo = limpar_dados(df_unificado)

    # Carga
    carregar_csv(df_limpo)

    print("Pipeline executada com sucesso!")


if __name__ == "__main__":
    main()


