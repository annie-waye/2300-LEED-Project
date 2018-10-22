import pandas as pd

def read_data_spreadsheet(filename):
    """
    Reads excel...
    :param filename:
    :return: pd.DataFrame of all file contents
    """
    contents = pd.read_excel(filename)

    return contents