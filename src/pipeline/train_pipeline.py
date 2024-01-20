import os
import sys
import pandas as pd
import logger
from src.logger import logging
from src.exception import CustomException 
from src.components.data_ingestion import DataIngestion

if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    print(train_data_path, test_data_path)
