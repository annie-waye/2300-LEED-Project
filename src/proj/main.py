import pandas as pd
import argparse
import os
import pathlib as plib

from src.proj.usgbc import fetch as ufetch
from src.proj.usgbc import process as uproc
from src.proj.usgbc import plot as uplot
from src.proj.usgbc import table as utab
from src.proj.usgbc import regress as ureg
from src.proj.edu import fetch as efetch
from src.proj.edu import plot as eplot
from src.proj.map import find as mfind
from src.proj.map import heat as mheat

# TODO Add docstrings
# TODO Add move plot to visualization module
# TODO fix any formatting issues (e.g., font size) and add as optional parameters to method (default set as plt default)
# TODO Add argparse to script files

if __name__ == '__main__':
    cwd = os.getcwd()
    proj = plib.Path(cwd).parents[1]
    dpath = os.path.join(proj, 'data')

    parser = argparse.ArgumentParser(description='Text Analysis through TFIDF computation',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-sub', '--subset', type=str, default='boston_projects.xlsx', help='')
    parser.add_argument('-sup', '--superset', type=str, default='mass_projects.csv', help='')
    parser.add_argument('-s', '--students', type=str, default='mass_hs_grads.xlsx')
    parser.add_argument('-d', '--datadir', type=str, help='Root directory containing data',
                        default=dpath)
    args = parser.parse_args()

    # Get Data
    data_dir = args.datadir
    boston_data_file = os.path.join(data_dir, 'raw', args.subset)
    mass_data_file = os.path.join(data_dir, 'raw', args.superset)
    student_data_file = os.path.join(data_dir, 'raw', args.students)

    boston_data = ufetch.get_boston_data(boston_data_file)
    mass_data = ufetch.get_mass_data(mass_data_file)

    mass_proc = uproc.fit_encode(mass_data)
    mass_cities = uproc.analyze_by_city(mass_proc)

    #city_vals = mass_cities['City'].values
    #mfind.get_coords(city_vals, 'Massachusetts')

    #coords = mfind.get_coords(mass_cities['City'].values, 'Massachusetts')

    #boston_proc = uproc.fit_encode(boston_data)
    #mass_proc = uproc.fit_encode(mass_data)
    #mheat.show()
    #print(mass_cities[['City', 'Count']])
    #utab.show(mass_cities[['City', 'Count']])