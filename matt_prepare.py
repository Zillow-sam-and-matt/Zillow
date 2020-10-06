import pandas as pd
import numpy as np
import sklearn
import matt_acquire
from matt_acquire import get_zillow_data
from sklearn.preprocessing import MinMaxScaler


from sklearn.model_selection import train_test_split




def prep_zillow_data(target):
    df = get_zillow_data()
    df = df[['calculatedfinishedsquarefeet', 'bedroomcnt', 'bathroomcnt', 'taxvaluedollarcnt' ]]
    df.dropna(inplace=True)

    train_validate, test = train_test_split(df, test_size=.2, random_state=123)

    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    scaler = sklearn.preprocessing.MinMaxScaler()

    scaler.fit(X_train)

    X_train_scaled = pd.DataFrame(scaler.transform(X_train))
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate))
    X_test_scaled = pd.DataFrame(scaler.transform(X_test))


    X_train_scaled.rename(columns={0: 'Unit_Sq_ft', 1: 'Bedroom_Count', 2: 'Bathroom_Count'}, inplace=True)
    X_validate_scaled.rename(columns={0: 'Unit_Sq_ft', 1: 'Bedroom_Count', 2: 'Bathroom_Count'}, inplace=True)
    X_test_scaled.rename(columns={0: 'Unit_Sq_ft', 1: 'Bedroom_Count', 2: 'Bathroom_Count'}, inplace=True)

    return y_train, y_validate, y_test, X_train_scaled, X_validate_scaled, X_test_scaled
    



# def train_validate_test(df, target):
   
#     train_validate, test = train_test_split(df, test_size=.2, random_state=123)

#     train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

#     X_train = train.drop(columns=[target])
#     y_train = train[target]
    
#     X_validate = validate.drop(columns=[target])
#     y_validate = validate[target]
    
#     X_test = test.drop(columns=[target])
#     y_test = test[target]
    
#     return X_train, y_train, X_validate, y_validate, X_test, y_test

# def min_max_scale(X_train, X_validate, X_test, ):
    
#     scaler = sklearn.preprocessing.MinMaxScaler()

#     scaler.fit(X_train)

#     x_train_scaled = scaler.transform(X_train)
#     x_validate_scaled = scaler.transform(X_validate)
#     x_test_scaled = scaler.transform(X_test)
