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
    train_data_path : str = os.path.join("Artifacts", "train_data.csv")
    test_data_path : str = os.path.join("Artifacts", "test_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started...")
        try:
            data = pd.read_csv("data/heart.csv")
            logging.info("Read the data from the csv file")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok = True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Created the raws data file")

            logging.info("Splitting the data into train and test")
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            logging.info("Data splitting is completed")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Created the train and test data files")
            logging.info("Data ingestion completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error("Exception occured while ingesting the data")
            raise CustomException(e,sys) 

if __name__ == "__main__":
    object = DataIngestion()
    object.initiate_data_ingestion()
    pass 