import pandas as pd
from src.utils.logg import logging

class Data_Getter_Pred:
    """
    This class shall be used to obtain data from prediction
    """

    def __init__(self):
        self.path = 'artifacts/predict_data/inputfile.csv'


    def get_data_folder(self):
        """
        this method reads the data from source
        """

        logging.info('Entered the get_data method of the Data_Getter class')
        try:
            self.data = pd.read_csv(self.path)
            logging.info("Data Load sucessfully")
            return self.data
        except Exception as e:
            logging.exception({e})
            raise Exception()