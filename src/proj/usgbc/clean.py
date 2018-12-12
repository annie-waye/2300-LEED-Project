import pandas as pd


def convert_dates(dataframe):
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    return dataframe


def remove_duplicates(dataframe):
    dataframe = dataframe.drop_duplicates()
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def sort_dates(dataframe):
    dataframe = dataframe.sort_values('Date')
    dataframe = dataframe.reset_index(drop=True)
    return dataframe
