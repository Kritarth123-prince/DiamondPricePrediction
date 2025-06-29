import os
import sys
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from exception import CustomException
from utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # Try different file paths and formats
            model_paths = [
                "artifacts/model.joblib",
                "artifacts/model_v4.pkl", 
                "artifacts/model.pkl"
            ]
            
            preprocessor_paths = [
                "artifacts/preprocessor.joblib",
                "artifacts/preprocessor_v4.pkl",
                "artifacts/preprocessor.pkl"
            ]
            
            # Load model
            model = None
            for path in model_paths:
                if os.path.exists(path):
                    try:
                        print(f"Trying to load model from: {path}")
                        model = load_object(file_path=path)
                        print(f"Successfully loaded model from: {path}")
                        break
                    except Exception as e:
                        print(f"Failed to load from {path}: {e}")
                        continue
            
            if model is None:
                raise Exception("Could not load model from any path")
            
            # Load preprocessor
            preprocessor = None
            for path in preprocessor_paths:
                if os.path.exists(path):
                    try:
                        print(f"Trying to load preprocessor from: {path}")
                        preprocessor = load_object(file_path=path)
                        print(f"Successfully loaded preprocessor from: {path}")
                        break
                    except Exception as e:
                        print(f"Failed to load from {path}: {e}")
                        continue
            
            if preprocessor is None:
                raise Exception("Could not load preprocessor from any path")
            
            print("Both model and preprocessor loaded successfully")
            
            # Transform and predict
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 carat: float,
                 cut: str,
                 color: str,
                 clarity: str,
                 depth: float,
                 table: float,
                 x: float,
                 y: float,
                 z: float):

        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "carat": [self.carat],
                "cut": [self.cut],
                "color": [self.color],
                "clarity": [self.clarity],
                "depth": [self.depth],
                "table": [self.table],
                "x": [self.x],
                "y": [self.y],
                "z": [self.z],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

# Test the prediction pipeline
if __name__ == '__main__':
    try:
        # Create sample diamond data for testing
        sample_data = CustomData(
            carat=1.0,
            cut='Premium',
            color='E',
            clarity='VS1',
            depth=61.5,
            table=57.0,
            x=6.3,
            y=6.3,
            z=3.9
        )
        
        pred_df = sample_data.get_data_as_data_frame()
        print("Sample data:")
        print(pred_df)
        
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        print(f"Predicted price: ${results[0]:,.2f}")
        
    except Exception as e:
        print(f"Error: {e}")