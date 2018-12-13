import src.data.prepare as prep
import os
import math
import pathlib as plib
import pandas as pd

cwd = os.getcwd()
pars = plib.Path(cwd).parents
root = pars[1]
grads = os.path.join(root, 'data', 'raw', 'mass_hs_grads.xlsx')

spread = prep.read_data_spreadsheet(grads)
spread.drop([0, 18, 19, 20, 21, 22, 23, 24], inplace=True)
spread.reset_index(drop=True, inplace=True)
spread = spread.T.reset_index(drop=True).T

spread.loc[0, 0] = 'Year'
for x in range(2, 19):
    if x % 2 == 0:
        spread.loc[0, x] = spread.loc[0, x - 1]

spread.drop([5, 7, 8], inplace=True)
spread.reset_index(drop=True, inplace=True)

years = []
students = []
for x in range(1, 19):
    if x % 2 != 0:
        years.append(spread.loc[0, x])

        val = spread.loc[2, x] * spread.loc[2, x + 1] / 100
        val = math.floor(val)
        students.append(val)


college_data = pd.DataFrame({'Years': years, 'Students': students})

print(college_data)