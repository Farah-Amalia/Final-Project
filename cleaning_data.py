import pandas as pd
from sqlalchemy import create_engine

def data_bankmarketing():
    engine = create_engine("mysql+mysqlconnector://root:Farah210795@localhost/bank_marketing?host=localhost?port=3306")
    conn = engine.connect()
    result = conn.execute('SELECT * from bank_marketing.bank1').fetchall()
    df = pd.DataFrame(result, columns=result[0].keys())
    # df = pd.read_csv('bank-additional-full.csv')
    return df

def feature():
    df = pd.read_csv('feature_importance.csv')
    return df