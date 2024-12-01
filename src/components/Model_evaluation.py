import os
import mlflow
import numpy as np
import mlflow.sklearn
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.utils.utils import load_object

class ModelEvaluation:
    def __init__(self):
        pass
    
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))# here is RMSE
        mae = mean_absolute_error(actual, pred)# here is MAE
        r2 = r2_score(actual, pred)# here is r3 value
        return rmse, mae, r2
    
    def initiate_model_evaluation(self,test_array):
        pass 