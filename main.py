from extract import extract_data
from transform import transform_data
from load import load_data

sheet_id = '1glmIpCXwkUP7r7hQ_oeG99Jv8UhDU_FvbLSHK8V5ZPk'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=0'

raw_data = extract_data(url)
transformed_data = transform_data(raw_data)
load_data(transformed_data)
