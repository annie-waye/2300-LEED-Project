import math
import pandas as pd


def remove_empties(dataframe):
    dataframe.drop([5, 7, 8], inplace=True)
    dataframe.reset_index(drop=True, inplace=True)
    pass


def parse_data(dataframe):
    years = []
    students = []

    for x in range(1, 19):
        if x % 2 != 0:
            years.append(dataframe.loc[0, x])

            val = dataframe.loc[2, x] * dataframe.loc[2, x + 1] / 100
            val = math.floor(val)

            students.append(val)

    percents = []

    for x in range(1, 9):
        percents.append(round(
            (students[x] - students[x - 1]) / students[x] * 100, 2))

    college_data = pd.DataFrame({'Years': years[1:], 'Students': students[1:],
                                 'Percentage': percents})
    return college_data
