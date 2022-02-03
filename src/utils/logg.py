from datetime import datetime
import os
from src.utils.common import create_dir

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

class App_Logger:
    def __init__(self):

        create_dir("artifacts/log")


    def log(self, file_object, log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message +"\n")

    # def Gen_log(self, log_message):
    #     __file = open("artifacts/log/Gen.txt", 'a+')
    #     self.now = datetime.now()
    #     self.date = self.now.date()
    #     self.current_time = self.now.strftime("%H:%M:%S")
    #     __file.write(
    #         str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message + "\n")
