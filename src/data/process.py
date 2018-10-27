import pandas as pd
import sklearn.preprocessing as skp


def fit_encode(dataframe):
    processed = dataframe.copy()
    l_enc = skp.LabelEncoder()
    processed['Construction'] = l_enc.fit_transform(processed['Construction'])
    processed['Validation'] = l_enc.fit_transform(processed['Validation'])
    processed['Certification'] = l_enc.fit_transform(processed['Certification'])
    processed = processed.drop(['Name'], axis=1)
    return processed


def analyze_by_date(dataframe):
    df = dataframe.copy()
    df = df.groupby(pd.Grouper(key='Date', freq='1Y', axis=0)).mean()
    return df