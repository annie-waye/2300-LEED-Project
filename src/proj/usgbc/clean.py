import pandas as pd


def convert_dates(dataframe):
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    return dataframe


def remove_duplicates(dataframe):
<<<<<<< HEAD
    """

    :param dataframe: desired data set
    :return: dataframe without duplicates, re-indexed
    """
    dataframe = dataframe.drop_duplicates()
    dataframe = dataframe.reset_index(drop=True)
    return dataframe
=======
    df = dataframe.drop_duplicates()
    df = df.reset_index(drop=True)
    return df


def remove_na(dataframe):
    df = dataframe.dropna()
    df = df.reset_index(drop=True)
    return df
>>>>>>> pr/5


def sort_dates(dataframe):
    df = dataframe.sort_values('Date')
    df = df.reset_index(drop=True)
    return df


def sort_counts(dataframe):
    df = dataframe.sort_values('Count')
    df = df.reset_index(drop=True)
    return df