from pandas import DataFrame

def treat_columns(df: DataFrame):
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

    return df

def treat_inconsistent_data(df: DataFrame):
    df.loc[3, 'ano_de_fabricacao'] = 2020
    df.loc[6, 'preco'] = 19000

    return df

def drop_irrelevant_data(df: DataFrame):
    df = df.drop_duplicates()
    df = df.dropna()

    return df

def transform_data(df: DataFrame):
    try:
        df_treated_columns = treat_columns(df)
        df_consistent_data = treat_inconsistent_data(df_treated_columns)
        transformed_data = drop_irrelevant_data(df_consistent_data)

        return transformed_data
    except Exception as e:
        print(f"Algo deu errado: {e}")
