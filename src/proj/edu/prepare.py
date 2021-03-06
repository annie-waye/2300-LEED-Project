
def add_year(dataframe):
    dataframe.loc[0, 0] = 'Year'
    pass


def check_years(dataframe):
    for x in range(2, 19):
        if x % 2 == 0:
            dataframe.loc[0, x] = dataframe.loc[0, x - 1]
    pass


def arrange_cols(dataframe):
    df = dataframe.drop([0, 18, 19, 20, 21, 22, 23, 24])
    df.reset_index(drop=True, inplace=True)
    df = df.T.reset_index(drop=True).T
    return df
