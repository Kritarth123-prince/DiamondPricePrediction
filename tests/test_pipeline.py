import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

class TestPredictionPipeline(unittest.TestCase):
    
    def setUp(self):
        self.pipeline = PredictPipeline()
        self.sample_data = CustomData(
            carat=1.5,
            cut="Premium",
            color="G",
            clarity="VS1",
            depth=61.5,
            table=57.0,
            x=7.3,
            y=7.35,
            z=4.5
        )
    
    def test_custom_data_creation(self):
        self.assertEqual(self.sample_data.carat, 1.5)
        self.assertEqual(self.sample_data.cut, "Premium")
        self.assertEqual(self.sample_data.color, "G")
        print("CustomData creation test passed")
    
    def test_dataframe_conversion(self):
        df = self.sample_data.get_data_as_data_frame()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 1)
        self.assertEqual(len(df.columns), 9)
        print("DataFrame conversion test passed")
    
    def test_prediction(self):
        try:
            df = self.sample_data.get_data_as_data_frame()
            prediction = self.pipeline.predict(df)
            
            self.assertIsInstance(prediction, (list, tuple))
            self.assertTrue(len(prediction) > 0)
            self.assertTrue(prediction[0] > 0)  # Price should be positive
            
            print(f"Prediction test passed: ${prediction[0]:,.2f}")
            return True
        except Exception as e:
            print(f"Prediction test failed: {str(e)}")
            return False

def run_pipeline_tests():
    print("Starting Pipeline Tests...")
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPredictionPipeline)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("All pipeline tests passed!")
    else:
        print("Some pipeline tests failed.")

if __name__ == "__main__":
    run_pipeline_tests()