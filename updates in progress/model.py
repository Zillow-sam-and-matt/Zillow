import pandas as pd
import numpy as np
import prepare
import acquire
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.linear_model import LinearRegression, LassoLars
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.feature_selection import RFE

import warnings
warnings.filterwarnings("ignore")

def final_model_test():
    """
    Function fits, predicts, and evaluates the final model from our project (Model 1) on the test data set.
    """
    # acquiring data sets 
    train, y_train, y_validate, y_test, X_train_scaled, X_train, X_validate, X_test, X_validate_scaled, X_test_scaled = prepare.prep_zillow_data('taxvaluedollarcnt')
    
    # copying df to avoid changing original when we add predictions column
    y_train_m1 = y_train.copy()

    # creating linear regression object
    lm_1 = LinearRegression()

    # fitting model to data
    lm_1.fit(X_train_scaled, y_train_m1)
    
    # creating copy of y_test data set to avoid altering the original when we make our predictions column
    y_test_m1 = y_test.copy()

    # adding column to model 1 train that holds model 1 predictions of house value
    y_test_m1['model_1_prediction'] = lm_1.predict(X_test_scaled)

    # calculating RMSE value of model 1 on validate data
    RMSE_lm_m1_test = round(np.sqrt(mean_squared_error(y_test.tax_dollar_value, y_test_m1.model_1_prediction)))

    # printing results
    print(f'Model 1s RMSE value when predicting house values on the test data set is {RMSE_lm_m1_test}')