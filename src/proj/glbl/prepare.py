import pandas as pd


def get_data(filepath):
    raw_data = pd.read_excel(filepath)
    return raw_data
