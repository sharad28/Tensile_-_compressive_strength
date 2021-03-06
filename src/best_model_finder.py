from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor
from sklearn.metrics import roc_auc_score,accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import numpy as np
from src.utils.common import config_data
import logging
import os
import pandas as pd
from src.utils.logg import logging

class Model_finder:
    """
    This model will do model tuning
    """
    def __init__(self):
        pass

    def get_params_tune_for_xgboost(self, train_x:pd.DataFrame,train_y:pd.DataFrame,test_x:pd.DataFrame,test_y:pd.DataFrame):

        """
                           Method Name: get_best_params_for_xgboost
                                        Description: get the parameters for XGBoost Algorithm which give the best accuracy.
                                                     Use Hyper Parameter Tuning.
                                        Output: The model with the best parameters
                                        On Failure: Raise Exception

                                        Written By: Sarad Mishra
                                        Version: 1.0

        """
        logging.info("Entered the get_best_params_for_xgboost method of the Model_Finder class")
        try:
            config = config_data()
            self.param_grid_xgboost =config['params']['XGBOOST_PARAMS']

            #creating object of XGBoost regressor
            self.xgr = XGBRegressor(objective='reg:squarederror')
            self.grid = GridSearchCV(self.xgr,self.param_grid_xgboost,verbose=3,cv=5)
            # finding the best parameters
            self.grid.fit(train_x,train_y)

            # extracting the best parameters
            logging.info(f"Best_params for xgboost regressor is {self.grid.best_params_}")

            # extracting the best parameters
            self.learning_rate = self.grid.best_params_['learning_rate']
            self.max_depth = self.grid.best_params_['max_depth']
            self.n_estimators = self.grid.best_params_['n_estimators']

            #new model based with best parameters is created
            self.xgr = XGBRegressor(learning_rate=self.learning_rate, max_depth=self.max_depth,
                                    n_estimators=self.n_estimators)

            # self.xgr = XGBRegressor(self.grid.best_params_)

            self.xgr.fit(train_x, train_y)

            logging.info("New model is created based on best parameters which are tune using grid search cv")

            #Calculating RMSE & r-square error for test dataset
            y_test_pred  = self.xgr.predict(test_x)
            self.rmse = round(np.sqrt(mean_squared_error(test_y,y_test_pred)),2)
            self.r2 = round(r2_score(test_y,y_test_pred),2)
            logging.info("**"*20)
            logging.info(f"RMSE for xgboost best model is {self.rmse}\nr2_score for xgboost is {self.r2}")
            logging.info("**" * 20)


            return self.xgr
        except Exception as e:
            logging.exception(f"Exception occured in get_best_params_for_xgboost method of the Model_Finder class. Exception message:  \n {e}")
            logging.info('XGBoost Parameter tuning  failed. Exited the get_best_params_for_xgboost method of the Model_Finder class')

