import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException


# initialize the data ingestion configuration (required parameters for ingestion class)

@dataclass
class DataIngestionconfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')


# create a data ingestion class (read, train test split)
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestion()
    
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Method Started")

        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info("Dataset read as pandas data frame")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Train data split ")
            train_set,test_set = train_test_split(df, test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False, header = True)

            logging.info("Ingestion of data is completed successfully")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        
        except Exception as e:
            logging.info("Error Occur in data ingestion config")