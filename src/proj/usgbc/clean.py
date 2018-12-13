import pandas as pd


def convert_dates(dataframe):
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    return dataframe


def remove_duplicates(dataframe):
    df = dataframe.drop_duplicates()
    df = df.reset_index(drop=True)
    return df


def remove_na(dataframe):
    df = dataframe.dropna()
    df = df.reset_index(drop=True)
    return df


def sort_dates(dataframe):
    df = dataframe.sort_values('Date')
    df = df.reset_index(drop=True)
    return df


def sort_counts(dataframe):
    df = dataframe.sort_values('Count')
    df = df.reset_index(drop=True)
    return df