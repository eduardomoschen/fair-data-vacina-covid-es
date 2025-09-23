import pandas as pd


INPUT_CSV_PATH = 'estabelecimentos_classificados_es.csv'
OUTPUT_CSV_PATH = 'estabelecimentos_final.csv'
COLUMN_TO_REMOVE = 'SK_DM_ESTABELECIMENTOS'

try:
    dataframe = pd.read_csv(INPUT_CSV_PATH, sep=';', encoding='utf-8-sig')
    print(f"Arquivo '{INPUT_CSV_PATH}' lido com sucesso.")

    if COLUMN_TO_REMOVE in dataframe.columns:
        dataframe = dataframe.drop(columns=[COLUMN_TO_REMOVE])
        print(f"A coluna '{COLUMN_TO_REMOVE}' foi removida.")
        dataframe.to_csv(OUTPUT_CSV_PATH, sep=';', encoding='utf-8-sig', index=False)
        print(f"O novo arquivo foi salvo como '{OUTPUT_CSV_PATH}' sem a coluna indesejada.")
    else:
        print(f"\nERRO: A coluna '{COLUMN_TO_REMOVE}' não foi encontrada no arquivo '{INPUT_CSV_PATH}'.")
        print("Nenhuma alteração foi feita.")
        print("Colunas disponíveis no arquivo:", dataframe.columns.tolist())
except FileNotFoundError:
    print(f"ERRO: O arquivo de entrada '{INPUT_CSV_PATH}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
