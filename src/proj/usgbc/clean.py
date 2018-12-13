import pandas as pd


def convert_dates(dataframe):
    """

    :param dataframe: desired data
    :return: new data frame
    """
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    return dataframe


def remove_duplicates(dataframe):
    """

    :param dataframe: desired data
    :return: data without duplicates
    """
    dataframe = dataframe.drop_duplicates()
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def sort_dates(dataframe):
    """

    :param dataframe: desired data
    :return: data sorted by date
    """
    dataframe = dataframe.sort_values('Date')
    dataframe = dataframe.reset_index(drop=True)
    return dataframe
