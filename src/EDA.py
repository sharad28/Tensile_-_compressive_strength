import numpy as np
import pandas as pd
import logging
# from pandas_profiling import ProfileReport
import time

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

class EDA:
    def __ini__(self):
        pass
    def read_csv(self,path):
        return pd.read_csv(path)

    # def generate_report(self,df,name):
    #     self.profile = ProfileReport(df, title="Pandas Profiling Report")
    #
    #     self.profile.to_file("your_report.html")

    def missing_val_handling_by_removal(self,df : np.DataFrame):
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

    def missing_val_handling_by_mean(self,df : np.DataFrame):
        """
        This funciton replace all null values with mean of its columns

        :param df: Data in numpy.DataFrame format
        :return: Dataframe with replaceing nan with mean
        """
        
