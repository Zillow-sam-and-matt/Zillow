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

# function to get data for preparation, exploration, modeling
def get_zillow_data():
    """
    Function connects to the data science database and returns a data frame containing Zillow data for properties whose last transaction was in May through June 2017. This data will be used to find key drivers of property value and to create a model that predicts property value.
    """
    # SQL query string
    sql_query = "SELECT * FROM properties_2017 JOIN predictions_2017 on predictions_2017.parcelid = properties_2017.parcelid WHERE unitcnt = 1 AND transactiondate BETWEEN '2017-05-01' AND '2017-06-30'"
    
    # creates dataframe using data from DS database, Zillow table
    df = pd.read_sql(sql_query, get_connection('zillow'))
    
    # writes data to csv file for future use
    df.to_csv('zillow_df.csv')
    
    # returns data frame
    return df

# function to get data for county tax rate breakdown and property locations
def new_property_data():
    """
    Function returns data frame from data science database with Zillow data for properties whose last transaction was between May and June 2017. This data will be used to identify the state and county of each property as well as the tax rates of each county.
    """
    # SQL query string
    sql_query = "SELECT regionidzip, regionidcounty, taxamount, taxvaluedollarcnt FROM properties_2017 WHERE unitcnt = 1 AND transactiondate BETWEEN '2017-05-01' AND '2017-06-30';"
    
    # create dataframe using data from DS database, Zillow table
    df = pd.read_sql(sql_query, get_connection('zillow'))
    
    # writing data to csv for future use
    df.to_csv('property_df.csv')
    
    # return data frame
    return df