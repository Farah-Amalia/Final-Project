import pandas as pd

def data_bankmarketing():
    df = pd.read_csv('bank-additional-full.csv', sep=';')
    return df
