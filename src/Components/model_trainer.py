import os
import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from src.logger import logging
from src.exception import CustomException

from src.utils import save_object, evalute_object
from dataclasses import dataclass


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_traning(self, train_array, test_array):
        try:
            logging.info('Spliting Dependent and Independante Variable from train array')

            X_train, y_train, X_test, y_test = (
                train_array[:,:,-1],
                train_array[:,-1],
                test_array[:,:,-1],
                test_array[:,-1]
            )

            models = {
                'Linear Regression' : LinearRegression(),
                'Lasso' : Lasso(),
                'Ridge' : Ridge(),
                'ElasticNet' : ElasticNet(),
                'Dicision Tree' : DecisionTreeRegressor()

            }


            model_report:dict = evalute_model(X_train,y_train,X_test,y_test, models)
            print(model_report)
            print('\n==============================================================================')
            logging.info(f'Model Report : {model_report}')

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            print(f'Best Model Found , Model Name : {best_model_name}, R2 Score : {best_model_score}')
            print('\n=================================================================================')
            logging.info(f'Best Model Found , Model Name : {best_model_name}, R2 Score : {best_model_score}')
            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )

        except Exception as e:
            logging.info("Exception occurred during training")
            raise CustomException(e,sys)


