import pandas as pd


def read_data_spreadsheet(filename):
    """
    Reads excel...
    :param filename: file path of desired data
    :return: pd.DataFrame of all file contents
    """
    contents = pd.read_excel(filename)

    return contents


def fetch_data(filepath):
    """
    Gets file in readable format
    :param filepath: file path of desired data
    :return: returns the spreadsheet in a readable format
    """
    raw_data = read_data_spreadsheet(filepath)
    return raw_data


def pre_arrange_cols(dataframe):
    """

    :param dataframe: uses data in dataframe format
    :return: arranged dataframe
    """
    col_name = dataframe.columns.values[0]
    dataframe.loc[-1] = col_name
    dataframe.index = dataframe.index + 1
    dataframe = dataframe.sort_index()
    dataframe = dataframe.rename(index=str, columns={col_name: 'all'})
    return dataframe


def check_certification(cert):
    """

    :param cert:
    :return:
    """
    return cert in ['Silver', 'Gold', 'Platinum', 'Certified']


def check_version(ver):
    return ver.startswith('v')


def valid_index_range(start, end):
    return end - start == 8


def get_valid_frames(dataframe):
    """
    :param dataframe: arranged data set
    :return: clean indicies, eliminates invalid frames (i.e. cell contains URL)
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
    """

    :param dataframe: desired data set
    :param indices: prepared/valid indicies
    :return: cleaned dataframe
    """
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


def check_city(dataframe):
    dataframe['City'] = dataframe['City'].str.upper()
    pass


def strip_cols(dataframe):
    df = dataframe.drop(['Path'], axis=1)
    return df


def rename_cols(dataframe):
    df = dataframe.rename(index=str, columns={'Certification date': 'Date',
                                              'Unnamed: 0': 'Name',
                                              'Rating system': 'Construction',
                                              'Version': 'Validation',
                                              'Certification level': 'Certification'})
    check_city(df)
    return df
