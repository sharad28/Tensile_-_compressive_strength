import pandas as pd

import os
from src.utils.logg import logging
from src.utils.common import create_dir
from src.utils.common import config_data
from src.file_methods import file_operation
from src.best_model_finder import Model_finder
from src.data_preprocessing import preprocessing
from src.utils.data_loader.data_loader_prediction import Data_Getter_Pred





class prediction:

    def __init__(self):
        pass

    def predictionFromModel(self):

        try:
            logging.info("Start of Prediction")
            obj_data = Data_Getter_Pred()
            data = obj_data.get_data_folder()
            obj_file_loader = file_operation()

            model_comp = obj_file_loader.load_model("artifacts/Models/Compressive strengthfcu,t(MPa)/Compressive strengthfcu,t(MPa).sav")
            model_tensile = obj_file_loader.load_model("artifacts/Models/Splitting tensile strengthfst,t(MPa)/Splitting tensile strengthfst,t(MPa).sav")

            return model_comp,model_tensile
        except Exception as e:
            logging.exception(f"exception occur during prediction from model in PredictFromModel.py file\n{e}")