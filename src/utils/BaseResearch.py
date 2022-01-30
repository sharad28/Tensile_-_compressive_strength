import pandas as pd
from docx import Document
import argparse
import os
from src.utils.logg import App_Logger
from src.utils.common import read_yaml
from src.utils.common import create_dir

class Rawdata:
    def __init__(self,config_content):
        self.config_content = config_content
        __artifact = config_content['artifacts']
        __dir = os.path.join(__artifact['ARTIFACTS_DIR'],__artifact['LOG_DIR'])

        file_path = os.path.join(__dir,'Rawdata.txt')
        self.file_object = open(file_path, 'a+')
        self.log_writer = App_Logger()
        self.log_writer.log(self.file_object, "file logger started ")

    def read_docx(self, num: int = 0):
        """
        This method will read the MS document for table content.
        return in dataframe format

        Note: it will consider first row as header of table


        :param num: #no. of table in the document. by default it will take the first table
        :return: Return the table content in pandas dataframe format
        """
        try:
            __artifact_dir = self.config_content['artifacts']['ARTIFACTS_DIR']
            __raw_path = self.config_content['artifacts']['RAW_DATA']
            __path = self.config_content['artifacts']['RAW_FILE']
            path = os.path.join(__artifact_dir,__raw_path,__path)
            self.log_writer.log(self.file_object,"Starting extraction of dataset")
            #creating object for document
            __document = Document(path)

            #selection of table in document
            __table = __document.tables[num]

            #reading cell
            __data = [[cell.text for cell in row.cells] for row in __table.rows]

            #coverting to pandas dataframe
            __df = pd.DataFrame(__data)

            #Convert first index to header
            __df = __df.rename(columns=pd.Series([i.replace('\n', "") for i in __df.iloc[0]]))
            __df = __df.drop(index=0)
        except Exception as e:
            self.log_writer.log(self.file_object,"Exception error during Docx to csv to raw folder ")
        #method to convert df to csv
        self.DataFrame_to_csv(__df)



    def DataFrame_to_csv(self,df):
        __artifact_dir = self.config_content['artifacts']['ARTIFACTS_DIR']
        __init_data_dir = self.config_content['artifacts']['INITIAL_PREPARED_DATA']
        dir = os.path.join(__artifact_dir,__init_data_dir)
        create_dir(dir)
        file_csv= os.path.join(dir,'init_data.csv')
        df.to_csv(file_csv,index=False)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    # args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        Gen_log=App_Logger()
        Gen_log.Gen_log("\n********************")
        Gen_log.Gen_log(f">>>>> Preprocessing of data is started <<<<<")
        config_path = parsed_args.config
        config_content = read_yaml(config_path)
        # rw_path = content['artifacts']['RAW_DATA']
        rw=Rawdata(config_content)
        rw.read_docx()

        Gen_log.Gen_log(f">>>>> Raw_data is extracted from DOCX to CSV format<<<<<\n")
    except Exception as e:
        Gen_log.Gen_log(f" exception :  {e}")
        raise e