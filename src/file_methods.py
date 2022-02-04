import pickle
import os
import shutil
import logging
from src.utils.common import config_data

class file_operation:
    """
    this class will operate on model file.
    To: 1. Save
        2. load
    """
    config = config_data()
    def __init__(self):
        pass

    def save_model(self,model,filename):
        """
        :param model: To save model file using pickle and remove the existing model file

        :param filename:
        :return:
        """
        logging.info("Entered the save_model method of the File_Operation class")
        try:
            self.config = config_data()
            artifact = self.config['artifacts']
            artifact_dir = artifact['ARTIFACTS_DIR']
            model_dir = artifact['MODEL_DIR']
            target_dir = self.config['params']['TARGET']
            self.model_directory = os.path.join(artifact_dir,model_dir,target_dir)
            if os.path.isdir(self.model_directory):
                shutil.rmtree(os.path.join(artifact_dir,model_dir))
                os.makedirs(os.path.join(artifact_dir,model_dir),exist_ok = True)
                os.makedirs(self.model_directory,exist_ok = True)
            else:
                os.makedirs(os.path.join(artifact_dir, model_dir), exist_ok=True)
                os.makedirs(self.model_directory, exist_ok=True)
            with open(self.model_directory+"/"+filename+".sav","wb") as f:
                pickle.dump(model, f) #save the model to file
            logging.info(f"Model File {filename} saved \nin \n{self.model_directory}\nExited the save_model method of the Model_Finder class")
        except Exception as e:
            logging.exception(f'Exception occured in save_model method of the Model_Finder class. Exception message:  {e}')
            logging.exception(f"Model File '{filename}' could not be saved. Exited the save_model method of the Model_Finder class")
            raise Exception()

    def load_model(self,filename):
        """
                            Method Name: load_model
                    Description: load the model file to memory
                    Output: The Model file loaded in memory
                    On Failure: Raise Exception
        """
        logging.info('Entered the load_model method of the File_Operation class')
        try:
            with open(self.model_directory + '/' + filename + '.sav',
                      'rb') as f:
                logging(f'Model File {filename} loaded. Exited the load_model method of the Model_Finder class')
                return pickle.load(f)
        except Exception as e:
            logging.exception(f'Exception occured in load_model method of the Model_Finder class. Exception message:{e}')
            logging.info(f'Model File {filename} could not be saved. Exited the load_model method of the Model_Finder class')
            raise Exception()
