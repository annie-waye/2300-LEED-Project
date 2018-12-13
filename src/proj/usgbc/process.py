from . import clean as uclean
import sklearn.preprocessing as skp


def fit_encode(dataframe):
    """

    :param dataframe:
    :return:
    """
    processed = dataframe.copy()
    l_enc = skp.LabelEncoder()
    processed['Construction'] = l_enc.fit_transform(processed['Construction'])
    processed['Validation'] = processed['Validation'].map({
        'v1.0 pilot': 0,
        'v2.0': 1,
        'v2.1': 2,
        'v2.2': 3,
        'v2007': 4,
        'v2008': 5,
        'v2009': 6,
        'v4': 7
    })
    processed['Certification'] = processed['Certification'].map({
        'Certified': 0,
        'Silver': 1,
        'Gold': 2,
        'Platinum': 3
    })
    processed.drop(['Name'], axis=1, inplace=True)
    return processed


def analyze_by_date(dataframe):
    df = dataframe.groupby(dataframe['Date'].dt.year).mean()
    df.reset_index(inplace=True)
    return df


def analyze_by_city(dataframe):
    df_means = dataframe.groupby('City').mean()
    df_counts = dataframe.groupby('City').count()
    df = df_means.join(df_counts['Date'])
    df = df.rename(index=str, columns={'Date': 'Count'})
    df.reset_index(inplace=True)
    df = df.drop(18).reset_index(drop=True) # Removed extra Boston MA Record
    #df = uclean.sort_counts(df)

    return df
