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
    Function connects to the data science database and returns a data frame containing Zillow data for propertys whose last transaction was in May through June 2017.
    """
    # SQL query string
    sql_query = "SELECT properties_2017.id, properties_2017.parcelid, airconditioningtypeid, architecturalstyletypeid, basementsqft, bathroomcnt, bedroomcnt, buildingclasstypeid,buildingqualitytypeid, calculatedbathnbr, decktypeid,finishedfloor1squarefeet, calculatedfinishedsquarefeet,finishedsquarefeet12, finishedsquarefeet13, finishedsquarefeet15,finishedsquarefeet50, finishedsquarefeet6, fips, fireplacecnt,fullbathcnt, garagecarcnt, garagetotalsqft, hashottuborspa,heatingorsystemtypeid, latitude, longitude, lotsizesquarefeet,poolcnt, poolsizesum, pooltypeid10, pooltypeid2, pooltypeid7,propertycountylandusecode, propertylandusetypeid,propertyzoningdesc, rawcensustractandblock, regionidcity,regionidcounty, regionidneighborhood, regionidzip, roomcnt,storytypeid, threequarterbathnbr, typeconstructiontypeid,unitcnt, yardbuildingsqft17, yardbuildingsqft26, yearbuilt,numberofstories, fireplaceflag, structuretaxvaluedollarcnt,taxvaluedollarcnt, assessmentyear, landtaxvaluedollarcnt,taxamount, taxdelinquencyflag, taxdelinquencyyear,censustractandblock, predictions_2017.id, predictions_2017.parcelid, logerror, transactiondate FROM properties_2017 JOIN predictions_2017 on predictions_2017.parcelid = properties_2017.parcelid WHERE unitcnt = 1 AND transactiondate BETWEEN '2017-05-01' AND '2017-06-30'"
    
    # creates dataframe using data from DS database
    df = pd.read_sql(sql_query, get_connection('zillow'))
    
    # returns DF 
    return df