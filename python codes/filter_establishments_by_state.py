import pandas as pd
import requests
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


INPUT_CSV_PATH = 'path_to_file/dm_estabelecimentos.csv'
OUTPUT_CSV_PATH = 'path_to_file/dm_estabelecimentos_es.csv'

STATE_CODE_FILTER = 32          # Espírito Santo's state code
BATCH_SIZE = 5000               # How many codes to process per batch
REQUEST_DELAY_S = 0.2           # Seconds between requests
REQUEST_TIMEOUT_S = 10          # Timeout for each request in seconds


http_session = requests.Session()
retry_strategy = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)
http_adapter = HTTPAdapter(max_retries=retry_strategy)
http_session.mount("https://", http_adapter)

dataframe = pd.read_csv(INPUT_CSV_PATH, dtype=str)
cnes_codes = dataframe['CD_ESTABELECIMENTO'].unique()

cnes_to_municipality_map = {}

for batch_start_index in range(0, len(cnes_codes), BATCH_SIZE):
    batch_end_index = min(batch_start_index + BATCH_SIZE, len(cnes_codes))
    batch_of_codes = cnes_codes[batch_start_index:batch_end_index]
    print(f'📦 Processando lote [{batch_start_index}:{batch_end_index}] ({len(batch_of_codes)} itens)...')

    for cnes_code in batch_of_codes:
        cnes_code_7digit = cnes_code.zfill(7)
        api_url = f'https://apidadosabertos.saude.gov.br/cnes/estabelecimentos/{cnes_code_7digit}'

        try:
            response = http_session.get(api_url, timeout=REQUEST_TIMEOUT_S)
        except requests.RequestException as e:
            print(f'❌ {cnes_code_7digit} → erro de conexão: {e}')
            time.sleep(REQUEST_DELAY_S * 5)
            continue

        if response.status_code != 200:
            time.sleep(REQUEST_DELAY_S)
            continue

        json_data = response.json()
        try:
            state_code = int(json_data.get('codigo_uf', 0))
        except (TypeError, ValueError):
            time.sleep(REQUEST_DELAY_S)
            continue

        if state_code == STATE_CODE_FILTER:
            cnes_to_municipality_map[cnes_code] = json_data.get('codigo_municipio')

        time.sleep(REQUEST_DELAY_S)

es_dataframe = dataframe[dataframe['CD_ESTABELECIMENTO'].isin(cnes_to_municipality_map.keys())].copy()

es_dataframe['cod_municipio'] = es_dataframe['CD_ESTABELECIMENTO'].map(cnes_to_municipality_map)

es_dataframe.to_csv(OUTPUT_CSV_PATH, index=False, encoding='utf-8-sig')
print(f'✅ Concluído! {len(es_dataframe)} estabelecimentos do ES salvos em:\n   {OUTPUT_CSV_PATH}')
