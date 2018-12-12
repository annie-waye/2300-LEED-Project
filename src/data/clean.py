import pandas as pd


def convert_dates(dataframe):
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    return dataframe


def remove_duplicates(dataframe):
    """

    :param dataframe: desired data set
    :return: dataframe without duplicates, re-indexed
    """
    dataframe = dataframe.drop_duplicates()
    dataframe = dataframe.reset_index(drop=True)
    return dataframe
