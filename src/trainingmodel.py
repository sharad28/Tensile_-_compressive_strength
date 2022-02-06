"""
This is the Entry point for Training the Machine Learning Model.
Written By: Sarad Mishra
Version: 1.0
"""

import logging
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from src.best_model_finder import Model_finder
from src.data_preprocessing import preprocessing
from src.utils.common import create_dir
from src.utils.common import config_data
from src.file_methods import file_operation
from src.utils.logg import logging


class trainModel:

    def __init__(self):
        pass

    def trainingModel(self):
        logging.info("Start of training")

        try:
            #Reading data from EDA_prepared_data
            self.configdata = config_data()
            self.artifacts = self.configdata['artifacts']

            __prepared_data_dir = os.path.join(self.artifacts['ARTIFACTS_DIR'],
                                             self.artifacts['PREPARED_DATA'],
                                             self.artifacts['PREPARED_DATA_FILE_NAME'])
            logging.info("Data started loading from prepared_data")
            __df = pd.read_csv(__prepared_data_dir,index_col=False)
            logging.info("Data loading are completed for training")
            logging.info("reading data from config for params is started")
            self.params = self.configdata['params']
            self.target_lable = self.params['TARGET']
            logging.info("reading data from config for params is completed")

            pre_process = preprocessing()
            self.X, self.y=pre_process.separate_label_feature(data=__df,label_column_name=self.target_lable)

            self.X = pre_process.remove_features(data=self.X,columns=self.params['FEATURES_NOT_FOR_TRIANING'])

            self.test_train_split = self.params['test_train_split']
            x_train, x_test, y_train, y_test = train_test_split(self.X, self.y, test_size=self.test_train_split['test_size'] , random_state=self.test_train_split['random_state'])

            model_obj = Model_finder()
            xgr_model_after_tuning = model_obj.get_params_tune_for_xgboost(x_train, y_train, x_test, y_test)

            #Saving the best model to the directory
            file_op=file_operation()
            file_op.save_model(xgr_model_after_tuning,self.target_lable)
            logging.info('Successful End of Training')

        except Exception as e:
            logging.exception(f'Exception occur during training of model {e}')
            raise Exception

trainModelObj = trainModel()
trainModelObj.trainingModel()