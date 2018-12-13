import pandas as pd
import argparse
import os
import pathlib as plib

from src.proj.usgbc import fetch as ufetch
from src.proj.usgbc import process as uproc
from src.proj.usgbc import plot as uplot
from src.proj.usgbc import regress as ureg
from src.proj.edu import fetch as efetch
from src.proj.edu import plot as eplot

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
    parser.add_argument('-l', '--leeds', type=str, default='boston_projects.xlsx', help='')
    parser.add_argument('-s', '--students', type=str, default='mass_hs_grads.xlsx')
    parser.add_argument('-d', '--datadir', type=str, help='Root directory containing data',
                        default=dpath)
    args = parser.parse_args()

    # Get Data
    data_dir = args.datadir
    leeds_data_file = os.path.join(data_dir, 'raw', args.leeds)
    student_data_file = os.path.join(data_dir, 'raw', args.students)

    leeds_data = ufetch.get_data(leeds_data_file)
    leeds_proc_data = uproc.fit_encode(leeds_data)
    leeds_proc_dates = uproc.analyze_by_date(leeds_proc_data)

    student_data = efetch.get_data(student_data_file)

    #eplot.show(student_data)
    uplot.show(leeds_proc_dates)
    #ureg.lin_reg(leeds_proc_data, 'Validation')