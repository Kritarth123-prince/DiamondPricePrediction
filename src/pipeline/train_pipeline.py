import os
import sys
import pandas as pd
import logging
# from src.logger import logging
# from src.exception import CustomException 
sys.path.append('src/logger.py')
sys.path.append('src/exception.py')
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    print(train_data_path, test_data_path)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_data_path, test_data_path)