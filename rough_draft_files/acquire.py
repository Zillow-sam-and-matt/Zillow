from env import host, user, password

import pandas as pd
import numpy as np
import os

# creates url for connection to data science database
def get_connection(db, user=user, host=host, password=password):
    """
    Function creates a URL that can be used to connect to the data science database.
    """
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_zillow_data():
    """
    Function connects to the data science database and returns a data frame containing Zillow data for houses whose last transaction was in May through June 2017.
    """
    # SQL query string
    sql_query = "SELECT * FROM properties_2017 JOIN predictions_2017 on predictions_2017.parcelid = properties_2017.parcelid WHERE unitcnt = 1 AND transactiondate BETWEEN '2017-05-01' AND '2017-06-30'"
    # creates dataframe using data from DS database
    df = pd.read_sql(sql_query, get_connection('zillow'))
    # writes data to csv file
    df.to_csv('zillow_df.csv')
    # returns DF 
    return df