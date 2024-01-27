import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
sys.path.append('src/logger.py')
sys.path.append('src')
sys.path.append('src/exception.py')
sys.path.append('src/Components/data_transformation.py')
#from src.logger import logging

# initialize the data ingestion configuration (required parameters for ingestion class)
@dataclass
class DataIngestionconfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

# create a data ingestion class (read, train test split)
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Method Started")

        try:
            df = pd.read_csv(os.path.join('notebooks/data', 'stud.csv'))
            logging.info("Dataset read as pandas data frame")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Train data split ")
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.exception("Error Occurred in data ingestion")
            # You might want to raise an exception or handle the error accordingly.

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)