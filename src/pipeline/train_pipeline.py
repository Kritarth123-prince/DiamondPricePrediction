import os
import sys
import pandas as pd
import numpy as np
import logging

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from exception import CustomException
from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainer

if __name__ == '__main__':
    logging.info("Training pipeline started")
    
    try:
        # Step 1: Data Ingestion
        obj = DataIngestion()
        train_data_path, test_data_path = obj.initiate_data_ingestion()
        print(f"Train data path: {train_data_path}")
        print(f"Test data path: {test_data_path}")

        # Step 2: Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        print("Data transformation completed")

        # Step 3: Model Training
        model_trainer = ModelTrainer()
        score = model_trainer.initiate_model_training(train_arr, test_arr)  # Fixed method name
        print(f"Model training completed. Best score: {score}")
        
        logging.info("Training pipeline completed successfully")
        
    except Exception as e:
        logging.error("Error in training pipeline")
        raise CustomException(e, sys)