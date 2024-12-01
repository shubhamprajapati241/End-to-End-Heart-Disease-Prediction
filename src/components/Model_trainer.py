import pandas as pd
import numpy as np
import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.utils.utils import save_object, evaluate_model
from sklearn.linear_model import LinearRegression, Ridge,Lasso,ElasticNet

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initate_model_training(self,train_array,test_array):
        pass 