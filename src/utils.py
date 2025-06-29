import os
import sys
import pickle
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Try joblib first (better for sklearn objects)
        if file_path.endswith('.joblib'):
            joblib.dump(obj, file_path)
        else:
            with open(file_path, 'wb') as file_obj:
                pickle.dump(obj, file_obj, protocol=4)  # Use protocol 4 for compatibility

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        # Try different loading methods
        if file_path.endswith('.joblib'):
            return joblib.load(file_path)
        
        # Try different pickle protocols
        try:
            with open(file_path, 'rb') as file_obj:
                return pickle.load(file_obj)
        except Exception as e1:
            # Try with different unpickler
            try:
                import dill
                with open(file_path, 'rb') as file_obj:
                    return dill.load(file_obj)
            except Exception as e2:
                raise CustomException(f"Failed to load with both pickle and dill: {e1}, {e2}", sys)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for model_name, model in models.items():
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
            report[model_name] = test_model_score
        return report
        
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(true, predicted):
    try:
        mae = mean_absolute_error(true, predicted)
        mse = mean_squared_error(true, predicted)
        rmse = np.sqrt(mse)
        r2_square = r2_score(true, predicted)
        return mae, mse, rmse, r2_square
    
    except Exception as e:
        raise CustomException(e, sys)