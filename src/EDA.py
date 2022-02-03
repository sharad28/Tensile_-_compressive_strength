import numpy as np
import pandas as pd
import logging
import matplotlib.pyplot as plt
import argparse
import os
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer,SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import time

from src.utils.common import read_yaml
from src.utils.common import create_dir
from src.utils.common import config_data

logging.basicConfig(
    filename=os.path.join('artifacts',"logs", 'running_logs.log'),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

class EDA:
    def __ini__(self,):
        pass
    def read_csv(self,path):
        try:
            logging.info("Start reading csv files for EDA")
            return pd.read_csv(path)
            logging.info("Completed reading csv files for EDA")
        except Exception as e:
            logging.exception(f"Exception: \n {e} \n occur during reading csv file")

    # def generate_report(self,df,name):
    #     self.profile = ProfileReport(df, title="Pandas Profiling Report")
    #
    #     self.profile.to_file("your_report.html")

    def missing_val_handling_by_removal(self,df: pd.DataFrame):
        """
        This funciton removes all the data from datafame contain
        any missing value
        :param df: Data in numpy.DataFrame format
        :return: Dataframe with no nan or value
        """
        __a = len(df)
        __nw_df = df.dropna(axis=0, how="any") # remove all rows with missing value
        __b = len(__nw_df)
        if __b/__a*100<95:
            logging.info("\n********************")
            logging.warning(f"No. of rows are removed is more than 5%. Where features/columns is/are {df.columns}")
        else:
            logging.info("\n********************")
            logging.info(f"No. of rows are removed is more than 5% Where features/columns is/are {df.columns}" )

        return __nw_df

    def missing_val_handling_by_KNN(self,df : pd.DataFrame):
        """
        This will fit the KNN_Imputer to training dataset

        :param df: Data in numpy.DataFrame format
        (value input should be in numeric format only)
        :return: return imputed dataset
        """
        try:
            config_content=config_data()
            __K = config_content['artifacts']['KNN_N_NEIGHBORS']
            __weights = config_content['artifacts']['KNN_WEIGHTS']
            ##object of knnimputer is created
            __KNN = KNNImputer(n_neighbors=__K,weights=__weights)
            # __KNN.fit_transform(df)
            df_transform = pd.DataFrame(__KNN.fit_transform(df), columns=df.columns)
            artifacts = config_content["artifacts"]
            artifacts_dir = artifacts['ARTIFACTS_DIR']
            prepared_data = artifacts['PREPARED_DATA']
            __path = os.path.join(artifacts_dir,prepared_data)
            create_dir(__path)
            df_transform.to_csv(os.path.join(__path,"KNN_df.csv"),index=False)
            logging.info("Knn imputation is completed")
        except Exception as e:
            logging.exception(f"Exception: \n {e} \noccur during KNN imputation")



if __name__ == '__main__':


    try:
        logging.info("EDA file is started running")

        eda = EDA()
        df = eda.read_csv('artifacts/initial_prepared_data/Updated_init_data.csv')
        eda.missing_val_handling_by_KNN(df)
        logging.info("EDA.py run is completed")
    except Exception as e:
        logging.warning(f" exception :  {e}")
        raise e
    finally:
        logging.info("Exist of EDA.py is completed")