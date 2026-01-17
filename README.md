# ETL – Jogadores FIFA (Masculino & Feminino)

##  Visão Geral
Este projeto implementa uma **pipeline de ETL (Extract, Transform, Load)** utilizando **Python e Pandas**, com o objetivo de **extrair, tratar, unificar e disponibilizar dados de jogadores(as) de futebol** (masculino e feminino) a partir de arquivos CSV do dataset FIFA, encontrados no Kaggle.

O projeto foi desenvolvido para fins de estudos sobre **Engenharia de Dados**.

---

## Objetivos do Projeto

- Extrair dados de jogadores masculinos e femininos
- Unificar os datasets em uma única base
- Limpar e padronizar colunas
- Normalizar e traduzir valores categóricos
- Gerar um CSV final pronto para análise

 ## Tecnologias Utilizadas

- Python 
- Pandas  
- Git / GitHub  
- Virtualenv

## Etapas da Pipeline

### Extração (extrair.py)

- Leitura dos arquivos CSV masculinos e femininos  

### Transformação (transformar.py)

Principais transformações aplicadas:

- Criação da coluna genero  
- União dos DataFrames masculino e feminino  
- Seleção das colunas relevantes  
- Renomeação e padronização de colunas  
- Conversão de tipos de dados (ex: datas)  
- Normalização de valores categóricos  

### Carga (carregar.py)

- Geração do arquivo final jogadores.csv  
- Encoding compatível com Excel (utf-8-sig)  


## Como Executar o Projeto

### Ativar o ambiente virtual

    source env/Scripts/activate
    
### Executar a pipeline

    python -m app.main

Ao final da execução, o arquivo será gerado em:

    data/output/jogadores.csv

## Observação Importante sobre os Dados

O dataset FIFA contém **múltiplos registros do mesmo jogador(a)**, pois cada linha representa **uma edição ou temporada diferente do jogo**.

