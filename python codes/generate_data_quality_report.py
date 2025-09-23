import pandas as pd

DATASET_FILE_PATH = 'estabelecimentos_final.csv'
CONTROLLED_VOCABULARY_ESTABLISHMENT_TYPES = [
    'Centro de Atenção Psicossocial', 'Centro de Especialidades Odontológicas',
    'Centro de Imunização', 'Centro de Referência', 'Centro de Saúde', 'Clínica',
    'Consultório na Rua', 'Farmácia', 'Hemocentro', 'Hospital', 'Maternidade',
    'Outros', 'Policlínica', 'Pronto Atendimento',
    'Rede de Frio / Armazenamento de Imunobiológicos', 'Secretaria de Saúde',
    'Superintendência Regional de Saúde', 'Unidade Básica de Saúde',
    'Unidade Sanitária', 'Unidade de Saúde', 'Unidade de Saúde da Família',
    'Vigilância em Saúde',
]

try:
    dataframe = pd.read_csv(DATASET_FILE_PATH, delimiter=';')
except FileNotFoundError:
    print(f"Erro: Arquivo '{DATASET_FILE_PATH}' não encontrado.")
    exit()

print("--- RELATÓRIO DE QUALIDADE DE DADOS ---")
print(f"Análise do arquivo: {DATASET_FILE_PATH}")
print(f"Total de Registros: {len(dataframe)}")
print("-" * 40)

# 1. COMPLETENESS METRIC (PERCENTAGE OF NULL VALUES)
print("\n1. COMPLETUDE (Valores Nulos):")
completeness_report = (dataframe.isnull().sum() / len(dataframe)) * 100
for column_name, percentage in completeness_report.items():
    print(f"- {column_name}: {percentage:.2f}% nulos")

print("\n2. UNICIDADE (Valores Únicos):")
UNIQUE_KEY_COLUMNS = ['CD_ESTABELECIMENTO']
for key_column in UNIQUE_KEY_COLUMNS:
    is_unique = dataframe[key_column].is_unique
    print(f"- A coluna '{key_column}' é 100% única? {'Sim' if is_unique else 'Não'}")

print("\n3. VALIDADE (Conformidade com as Regras):")
invalid_rows = dataframe[~dataframe['TP_ESTABELECIMENTO'].isin(CONTROLLED_VOCABULARY_ESTABLISHMENT_TYPES)]
invalid_percentage = (len(invalid_rows) / len(dataframe)) * 100
print(f"- '{'TP_ESTABELECIMENTO'}' tem valores fora do vocabulário controlado? {'Sim' if invalid_percentage > 0 else 'Não'} ({invalid_percentage:.2f}% inválidos)")

are_uris_valid = dataframe['URI_MUNICIPIO'].str.startswith('https://servicodados.ibge.gov.br/api/v1/localidades/municipios/', na=False).all()
print(f"- Todas as URIs em '{'URI_MUNICIPIO'}' seguem o padrão esperado? {'Sim' if are_uris_valid else 'Não'}")

print("-" * 40)
