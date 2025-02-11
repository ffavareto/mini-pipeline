import gspread
from gspread_dataframe import set_with_dataframe
from pandas import DataFrame


def load_data(clean_data: DataFrame):
    if clean_data.empty:
        raise ValueError("O DataFrame está vazio.")

    try:
        row_count, col_count = clean_data.shape
        google_client = gspread.service_account(filename='g_sheets_credentials.json')
        spreadsheet = google_client.open('carros')
        sheet_title = 'dados_limpos'

        try:
            worksheet = spreadsheet.worksheet(sheet_title)
        except gspread.exceptions.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(title=sheet_title, rows=row_count, cols=col_count)

        set_with_dataframe(worksheet, clean_data)
        print("Dados carregados com sucesso.")

    except FileNotFoundError:
        print("Erro: arquivo de credenciais não encontrado. Verifique o caminho do JSON de credenciais.")
    except gspread.exceptions.APIError as api_error:
        print("Erro na API do Google Sheets:", api_error)
    except Exception as ex:
        print("Ocorreu um erro inesperado:", ex)
