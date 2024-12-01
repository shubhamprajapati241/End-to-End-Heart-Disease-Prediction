import os 
import sys 
import pandas as pd 
import numpy as np 

from dataclasses import dataclass 
from src.logger import logging
from src.exception import CustomException 

from sklearn.compose import ColumnTransformer 
from sklearn.impute import SimpleImputer 
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import OrdinalEncoder, StandardScaler 
from src.utils.utils import save_object 

from src.components.Data_ingestion import DataIngestion 
from src.components.Model_trainer import ModelTrainer
from src.components.Model_evaluation import ModelEvaluation

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("Artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_tranformation(self):
        pass 

    def initialize_data_transformation(self, train_path, test_path):
        pass 

if __name__ == "__main__":
    pass