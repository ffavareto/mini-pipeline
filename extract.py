import pandas as pd

def extract_data(url):
    try:
        raw_data = pd.read_csv(url)
        return raw_data
    except FileNotFoundError:
        print(f"A URL '{url}' não foi encontrada")
    except Exception as e:
        print(f"Ocorreu um erro desconhecido: {e}")