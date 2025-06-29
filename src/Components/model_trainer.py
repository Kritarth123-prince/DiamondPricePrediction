import os
import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import logging
from dataclasses import dataclass

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exception import CustomException
from utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):  # Fixed method name
        try:
            logging.info('Splitting Dependent and Independent Variables from train array')

            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],  # Fixed slicing
                train_array[:, -1],
                test_array[:, :-1],   # Fixed slicing
                test_array[:, -1]
            )

            models = {
                'Linear Regression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet(),
                'Decision Tree': DecisionTreeRegressor(),  # Fixed typo
                'Random Forest': RandomForestRegressor(),
                'Gradient Boosting': GradientBoostingRegressor()
            }

            model_report: dict = evaluate_models(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print('\n==============================================================================')
            logging.info(f'Model Report: {model_report}')

            # Get the best model score from dict
            best_model_score = max(sorted(model_report.values()))
            
            # Get the best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            
            print(f'Best Model Found, Model Name: {best_model_name}, R2 Score: {best_model_score}')
            print('\n=================================================================================')
            logging.info(f'Best Model Found, Model Name: {best_model_name}, R2 Score: {best_model_score}')
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            return best_model_score

        except Exception as e:
            logging.error("Exception occurred during model training")
            raise CustomException(e, sys)