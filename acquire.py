from env import host, user, password

import pandas as pd
import numpy as np
import os

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def new_zillow_data():
    
    sql_query = "SELECT * FROM properties_2017 JOIN predictions_2017 on predictions_2017.parcelid = properties_2017.parcelid WHERE unitcnt = 1 AND transactiondate BETWEEN '2017-05-01' AND '2017-06-30'"
    df = pd.read_sql(sql_query, get_connection('zillow'))
    df.to_csv('zillow_df.csv')
    return df

def get_zillow_data(cached=False):
    
    if cached or os.path.isfile('zillow_df.csv') == False:
        df = new_zillow_data()
    else:
        df = pd.read_csv('zillow_df.csv', index_col=0)
    return df