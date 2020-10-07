import pandas as pd
import numpy as np
import sklearn
from acquire import get_zillow_data
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def prep_zillow_data(target):
    # acquire zillow data
    df = get_zillow_data()
    # filter columns down to the target variable (taxvaluedollarcnt) and the final four columns from prep
    df = df[['calculatedfinishedsquarefeet', 'bedroomcnt', 'bathroomcnt', 'lotsizesquarefeet', 'taxvaluedollarcnt']]
    
    # drop na values
    df.dropna(inplace=True)

    # splitting data
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

    # specifying which columns to keep in outputted dataframe
    # x = features | y = target variable
    X_train = train.drop(columns=[target])
    y_train = train[[target]]
    
    X_validate = validate.drop(columns=[target])
    y_validate = validate[[target]]
    
    X_test = test.drop(columns=[target])
    y_test = test[[target]]
    
    # importing scaler
    scaler = sklearn.preprocessing.MinMaxScaler()

    # fitting scaler
    scaler.fit(X_train)

    # scaling data in dataframes
    X_train_scaled = pd.DataFrame(scaler.transform(X_train))
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate))
    X_test_scaled = pd.DataFrame(scaler.transform(X_test))

    # renaming data frame columns 
    train.rename(columns = {'taxvaluedollarcnt': 'tax_dollar_value','calculatedfinishedsquarefeet' : 'unit_sq_feet',	'bedroomcnt' : 'bedroom_count',	'bathroomcnt' : 'bathroom_count', 'lotsizesquarefeet' : 'lot_size_sq_feet' }, inplace=True)

    X_train_scaled.rename(columns = {0: 'unit_sq_feet', 1: 'bedroom_count', 2: 'bathroom_count', 3: 'lot_size_sq_feet' }, inplace=True)
    X_validate_scaled.rename(columns = {0: 'unit_sq_feet', 1: 'bedroom_count', 2: 'bathroom_count',  3: 'lot_size_sq_feet'}, inplace=True)
    X_test_scaled.rename(columns = {0: 'unit_sq_feet', 1: 'bedroom_count', 2: 'bathroom_count',  3: 'lot_size_sq_feet'}, inplace=True)
    
    X_train.rename(columns = {'calculatedfinishedsquarefeet' : 'unit_sq_feet',	'bedroomcnt' : 'bedroom_count',	'bathroomcnt' : 'bathroom_count', 'lotsizesquarefeet' : 'lot_size_sq_feet' }, inplace=True)
    X_validate.rename(columns = {'calculatedfinishedsquarefeet' : 'unit_sq_feet',	'bedroomcnt' : 'bedroom_count',	'bathroomcnt' : 'bathroom_count', 'lotsizesquarefeet' : 'lot_size_sq_feet' }, inplace=True)
    X_test.rename(columns = {'calculatedfinishedsquarefeet' : 'unit_sq_feet',	'bedroomcnt' : 'bedroom_count',	'bathroomcnt' : 'bathroom_count', 'lotsizesquarefeet' : 'lot_size_sq_feet' }, inplace=True)
    
    y_train.rename(columns = {'taxvaluedollarcnt': 'tax_dollar_value'}, inplace=True)
    y_validate.rename(columns = {'taxvaluedollarcnt': 'tax_dollar_value'}, inplace=True)
    y_test.rename(columns = {'taxvaluedollarcnt': 'tax_dollar_value'}, inplace=True)
    
    # returning data frames
    return train, y_train, y_validate, y_test, X_train_scaled, X_train, X_validate, X_test, X_validate_scaled, X_test_scaled
    


