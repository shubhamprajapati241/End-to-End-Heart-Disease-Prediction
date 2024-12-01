import os 
import sys 
import pandas as pd
from src.logger import logging 
from src.exception import CustomException 
from sklearn.model_selection import train_test_split 
from dataclasses import dataclass 

@dataclass 
class DataIngestionConfig:
    raw_data_path : str = os.path.join("Artifacts", "raw_data.csv")
    training_data_path : str = os.path.join("Artifacts", "train_data.csv")
    test_data_path : str = os.path.join("Artifacts", "test_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        pass 

if __name__ == "__main__":
    # object = DataIngestion()
    # object.initiate_data_ingestion()
    pass 