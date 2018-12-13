import pandas as pd


def get_data(filepath):
    """
    get raw data
    :param filepath: desired file path
    :return: raw data
    """
    raw_data = pd.read_excel(filepath)
    return raw_data
