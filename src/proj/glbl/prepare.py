import pandas as pd


def get_data(filepath, ext):
    if ext == 'xlsx':
        return pd.read_excel(filepath)
    elif ext == 'csv':
        return pd.read_csv(filepath)
    return None
