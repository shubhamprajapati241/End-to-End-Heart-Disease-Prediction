import sys 
from src.logger import logging

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _,_, exec_tb = error_details.exc_info()
        self.line_no = exec_tb.tb_lineno
        self.file_name = exec_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name, self.line_no, str(self.error_message))
    
if __name__ == "__main__":
    # try: 
    #     a = 1/0
    # except Exception as e:
    #     logging.error("Division by zero")
    #     raise CustomException(e, sys)
    pass