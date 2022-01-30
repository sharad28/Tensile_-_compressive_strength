import pandas as pd
from docx import Document
from src.utils.logg import App_Logger


class Rawdata:
    def __init__(self, path):
        self.file_object = open("artifacts/log/Rawdata.txt", 'a+')
        self.log_writer = App_Logger()

    def read_docx(self, path, num: int = 0):
        """
        This method will read the MS document for table content.
        return in dataframe format

        Note: it will consider first row as header of table

        :param path: location of document file
        :param num: #no. of table in the document. by default it will take the first table
        :return: Return the table content in pandas dataframe format
        """
        try:
            self.log_writer(self.file_object,"Starting extraction of dataset")
            #creating object for document
            document = Document(path)

            #selection of table in document
            table = document.tables[num]

            #reading cell
            data = [[cell.text for cell in row.cells] for row in table.rows]

            #coverting to pandas dataframe
            df = pd.DataFrame(data)

            #Convert first index to header
            df = df.rename(columns=pd.Series([i.replace('\n', "") for i in df.iloc[0]]))
            df = df.drop(index=0)
        except Exception as e:
            self.log_writer(self.file_object,"Exception error during Docx to csv to raw folder ")
        #method to convert df to csv
        self.DataFrame_to_csv(df)



    def DataFrame_to_csv(self,df):

        df.to_csv('Read_data\data_read.csv',index=False)

