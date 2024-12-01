import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.utils.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass 

    def predict(self, feature):
        pass 


class CustomData:
    def __init__(self, 
            carat : float, 
            cut : str):
        self.carat = carat
        self.cut = cut 

    def get_data_as_dataframe(self):
        pass 