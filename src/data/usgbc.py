import data.prepare as prep
import data.process as proc
import data.clean as cl
import data.plot as pl
import data.regress as rg

import argparse
import os
import pathlib as plib

# TODO Add move plot to visualization module
# TODO fix any formatting issues (e.g., font size) and add as optional parameters to method (default set as plt default)
# TODO Add argparse to script files

if __name__ == '__main__':
    cwd = os.getcwd()
    proj = plib.Path(cwd).parents[1]
    dpath = os.path.join(proj, 'data')
    xlsx = os.path.join(dpath, 'raw', 'boston_projects.xlsx')

    parser = argparse.ArgumentParser(description='Text Analysis through TFIDF computation',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', type=str, default='boston_projects.xlsx', help='')
    parser.add_argument('-d', '--datadir', type=str, help='Root directory containing data',
                        default=dpath)
    args = parser.parse_args()

    # Get Data
    data_dir = args.datadir
    data_file = os.path.join(data_dir, 'raw', args.input)

    raw_data = prep.fetch_data(data_file)

    # Arrange Data in Columns
    pre_data = prep.pre_arrange_cols(raw_data)
    valid_frames = prep.get_valid_frames(pre_data)
    real_data = prep.arrange_cols(pre_data, valid_frames)

    # Clean/Format Data
    real_data = cl.remove_duplicates(real_data)
    real_data = cl.convert_dates(real_data)

    # Start Analyzing Data
    proc_data = proc.fit_encode(real_data)
    proc_date_data = proc.analyze_by_date(proc_data)

    # Start Plotting Data
    #pl.primary_plot(proc_date_data, 'Certification')
    #pl.primary_plot(proc_date_data, 'Construction')
    #print(proc_data)

    # Linear Regression - We'll put this in a separate module later
    sort_data = proc_data.sort_values('Date')
    sort_data = sort_data.reset_index(drop=True)

    # Certification
    csort_data = sort_data[['Certification']]
    ctrain_data = csort_data[csort_data.index % 5 == 0]
    ctest_data = csort_data[csort_data.index % 5 != 0]

    ctrain_x = ctrain_data.index.values.reshape(-1, 1)
    ctest_x = ctest_data.index.values.reshape(-1, 1)
    ctrain_y = ctrain_data['Certification'].values.reshape(-1, 1)
    ctest_y = ctest_data['Certification'].values.reshape(-1, 1)

    # Validation
    vsort_data = sort_data[['Validation']]
    vtrain_data = vsort_data[vsort_data.index % 5 == 0]
    vtest_data = vsort_data[vsort_data.index % 5 != 0]

    vtrain_x = vtrain_data.index.values.reshape(-1, 1)
    vtest_x = vtest_data.index.values.reshape(-1, 1)
    vtrain_y = vtrain_data['Validation'].values.reshape(-1, 1)
    vtest_y = vtest_data['Validation'].values.reshape(-1, 1)

    #rg.lin_reg(ctrain_x, ctest_x, ctrain_y, ctest_y)   # regression on Certification
    rg.lin_reg(vtrain_x, vtest_x, vtrain_y, vtest_y)    # regression on Validation