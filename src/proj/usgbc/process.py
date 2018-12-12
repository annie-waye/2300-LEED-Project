import pandas as pd
import sklearn.preprocessing as skp


def fit_encode(dataframe):
    """

    :param dataframe:
    :return:
    """
    processed = dataframe.copy()
    l_enc = skp.LabelEncoder()
    processed['Construction'] = l_enc.fit_transform(processed['Construction'])
    processed['Validation'] = l_enc.fit_transform(processed['Validation'])
    processed['Certification'] = l_enc.fit_transform(processed['Certification'])
    processed = processed.drop(['Name'], axis=1)
    return processed


def analyze_by_date(dataframe):
    df = dataframe.groupby(dataframe['Date'].dt.year).mean()
    df.reset_index(inplace=True)
    return df
