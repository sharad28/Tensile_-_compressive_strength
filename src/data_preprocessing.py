from src.utils.logg import logging
import os



class preprocessing:
    def __init__(self):
        pass
    def separate_label_feature(self,data,label_column_name):
        """
                                Method Name: separate_label_feature
                        Description: This method separates the features and a Label Coulmns.
                        Output: Returns two separate Dataframes, one containing features and the other containing Labels .
                        On Failure: Raise Exception

                        Written By: Sarad Mishra
                        Version: 1.0

        """
        logging.info('Entered the separate_label_feature method of the Preprocessor class')
        try:
            self.X = data.drop(labels=label_column_name,
                               axis=1)  # drop the columns specified and separate the feature columns
            self.Y = data[label_column_name]  # Filter the Label columns
            logging.info('Label Separation Successful. Exited the separate_label_feature method of the Preprocessor class')
            return self.X, self.Y
        except Exception as e:
            logging.exception('Exception occured in separate_label_feature method of the Preprocessor class. Exception message:  '
                              + str(e))
            logging.exception('Label Separation Unsuccessful. Exited the separate_label_feature method of the Preprocessor class')
            raise Exception()

    def remove_features(self,data,columns):
        """
                                         Method Name: sremove_features
                        Description: This method removes the features from dataset.
                        Output: Returns one separate Dataframes, rest of features.
                        On Failure: Raise Exception

                        Written By: Sarad Mishra
                        Version: 1.0
        """
        try:
            return data.drop(columns=columns)
        except Exception as e:
            logging.exception('Exception occured in remove_feature method of the Preprocessor class. Exception message:  '
                              + str(e))
            logging.exception('Label Separation Unsuccessful. Exited the remove_feature method of the Preprocessor class')
            raise Exception()
