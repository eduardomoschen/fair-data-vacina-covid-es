import pandas as pd
import requests


dataframe = pd.read_csv(
    'dm_estabelecimentos_es.csv',
    dtype={'CD_ESTABELECIMENTO': str, 'CD_MUNICIPIO': str}
)


def get_postal_code_from_cnes(cnes_code: str) -> str | None:
    api_url = f'https://apidadosabertos.saude.gov.br/cnes/estabelecimentos/{cnes_code}'
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        json_data = response.json()
        raw_postal_code = json_data.get('codigo_cep_estabelecimento') or json_data.get('estabelecimento', {}).get('cep')
        if not raw_postal_code:
            print(f"⚠️ CEP não encontrado para CNES {cnes_code}")
            return None
        return ''.join(filter(str.isdigit, raw_postal_code))
    except requests.exceptions.HTTPError as e:
        print(f"❌ Erro HTTP para CNES {cnes_code}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de requisição para CNES {cnes_code}: {e}")
    return None


def get_municipality_code_from_postal_code(postal_code: str) -> str | None:
    """Calls the ViaCEP API and returns the IBGE municipality code for the given postal code."""
    api_url = f'https://viacep.com.br/ws/{postal_code}/json/'
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        json_data = response.json()
        municipality_code = json_data.get('ibge')
        if not municipality_code:
            print(f"⚠️ Código IBGE não encontrado para CEP {postal_code}")
        return municipality_code
    except requests.exceptions.HTTPError as e:
        print(f"❌ Erro HTTP para CEP {postal_code}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de requisição para CEP {postal_code}: {e}")
    return None


for index, row in dataframe.iterrows():
    cnes_code = row['CD_ESTABELECIMENTO']
    postal_code = get_postal_code_from_cnes(cnes_code)
    if postal_code:
        municipality_code = get_municipality_code_from_postal_code(postal_code)
        if municipality_code:
            dataframe.at[index, 'CD_MUNICIPIO'] = municipality_code

dataframe.to_csv('dm_estabelecimentos_es_corrigido.csv', index=False)
print("Processo concluído – CSV salvo como 'dm_estabelecimentos_es_corrigido.csv'.")
