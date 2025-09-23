import pandas as pd


INPUT_CSV_PATH = 'dm_estabelecimentos_es.csv'
OUTPUT_CSV_PATH = 'estabelecimentos_classificados_es.csv'
TRADE_NAME_COLUMN = 'NM_FANTASIA'

try:
    dataframe = pd.read_csv(INPUT_CSV_PATH, sep=',', encoding='utf-8-sig')
    print(f"Arquivo '{INPUT_CSV_PATH}' lido com sucesso.")
except FileNotFoundError:
    print(f"ERRO: O arquivo '{INPUT_CSV_PATH}' não foi encontrado.")
    dataframe = None
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
    dataframe = None

if dataframe is not None:
    def classify_establishment_type(trade_name: str) -> str:
        """Classifies a health establishment based on its trade name."""
        trade_name_upper = str(trade_name).upper()
        if 'HOSPITAL' in trade_name_upper or 'HOSP.' in trade_name_upper: return 'Hospital'
        elif 'USF' in trade_name_upper or 'UNIDADE DE SAUDE DA FAMILIA' in trade_name_upper: return 'Unidade de Saúde da Família'
        elif 'UBS' in trade_name_upper or 'UNIDADE BASICA DE SAUDE' in trade_name_upper: return 'Unidade Básica de Saúde'
        # ... (rest of the classification rules) ...
        else: return 'Outros'

    try:
        if TRADE_NAME_COLUMN not in dataframe.columns:
            print(f"ERRO CRÍTICO: A coluna '{TRADE_NAME_COLUMN}' não foi encontrada no arquivo.")
            print(f"Colunas disponíveis: {dataframe.columns.tolist()}")
        else:
            dataframe['TP_ESTABELECIMENTO'] = dataframe[TRADE_NAME_COLUMN].apply(classify_establishment_type)
            dataframe['URI_MUNICIPIO'] = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios/' + dataframe['CD_MUNICIPIO'].astype(str)

            print("\n### Amostra do DataFrame com as novas colunas:")
            print(dataframe[[TRADE_NAME_COLUMN, 'TP_ESTABELECIMENTO', 'URI_MUNICIPIO']].head())
            print("\n" + "=" * 50 + "\n")
            print("### Contagem por Tipo de Estabelecimento (Atualizado):")
            print(dataframe['TP_ESTABELECIMENTO'].value_counts())

            dataframe.to_csv(OUTPUT_CSV_PATH, sep=';', encoding='utf-8-sig', index=False)

            output_json_path = 'estabelecimentos_classificados_es.json'
            dataframe.to_json(output_json_path, orient='records', lines=True, force_ascii=False)

            print("### SUCESSO! ###")
            print(f"O arquivo final com os dados classificados foi salvo como '{OUTPUT_CSV_PATH}'")
            print(f"Uma versão em JSON também foi salva como '{output_json_path}'")
    except Exception as e:
        print(f"\nUm erro inesperado ocorreu durante o processamento: {e}")
