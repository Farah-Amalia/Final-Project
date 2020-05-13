import pandas as pd

def data_bankmarketing():
    df = pd.read_csv('bank-additional-full.csv', sep=';')
    return df.head(50)

def feature():
    df = pd.read_csv('feature_importance.csv')
    return df