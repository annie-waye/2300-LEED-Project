import pandas as pd


def pre_arrange_cols(dataframe):
    """

    :param dataframe: desired data
    :return: arranged data frame
    """
    col_name = dataframe.columns.values[0]
    dataframe.loc[-1] = col_name
    dataframe.index = dataframe.index + 1
    dataframe = dataframe.sort_index()
    dataframe = dataframe.rename(index=str, columns={col_name: 'all'})
    return dataframe


def check_certification(cert):
    """

    :param cert: cert cell value
    :return: verified value
    """
    return cert in ['Silver', 'Gold', 'Platinum', 'Certified']


def check_version(ver):
    """

    :param ver: version cell value
    :return: verified value
    """
    return ver.startswith('v')


def valid_index_range(start, end):
    """

    :param start: first index
    :param end: last index
    :return: boolean check for index
    """
    return end - start == 8


def get_valid_frames(dataframe):
    """

    :param dataframe: desired data
    :return: correct indicies
    """
    start_index = 0
    end_index = 0
    indices = []
    for index, row in dataframe.iterrows():
        val = row['all']
        if 'http' in val:
            indices.append((start_index, end_index))
            start_index = int(index) - 1
        if check_version(val):
            end_index = int(index)
        if check_certification(val):
            end_index = int(index)
    valid_indices = []
    for frame in indices:
        if valid_index_range(frame[0], frame[1]):
            valid_indices.append(frame)
    return valid_indices


def arrange_cols(dataframe, indices):
    df = pd.DataFrame(columns=['Name', 'Date', 'City',
                               'State', 'Country', 'Construction',
                               'Validation', 'Certification'])
    for frame in indices:
        start = frame[0]
        end = frame[1] + 1
        section = dataframe.iloc[start:end]
        col_vals = section['all'].values
        df_section = pd.DataFrame({'Name': [col_vals[0]],
                                   'Date': [col_vals[2]],
                                   'City': [col_vals[3]],
                                   'State': [col_vals[4]],
                                   'Country': [col_vals[5]],
                                   'Construction': [col_vals[6]],
                                   'Validation': [col_vals[7]],
                                   'Certification': [col_vals[8]]})
        df = df.append(df_section)
    return df
