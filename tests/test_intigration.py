import requests
import json
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def test_end_to_end_integration():
    print("Running End-to-End Integration Test...")
    
    test_cases = [
        {
            "name": "Premium Large Diamond",
            "data": {
                "carat": 2.54,
                "cut": "Premium",
                "color": "D",
                "clarity": "VS1",
                "depth": 75.0,
                "table": 70.0,
                "x": 5.7,
                "y": 6.87,
                "z": 3.78
            },
            "expected_range": (10000, 15000)
        },
        {
            "name": "Small Good Diamond", 
            "data": {
                "carat": 0.5,
                "cut": "Good",
                "color": "G",
                "clarity": "SI1",
                "depth": 60.0,
                "table": 55.0,
                "x": 5.0,
                "y": 5.0,
                "z": 3.0
            },
            "expected_range": (1000, 3000)
        }
    ]
    
    results = []
    
    for test_case in test_cases:
        print(f"\n--- Testing: {test_case['name']} ---")
        
        try:
            custom_data = CustomData(**test_case['data'])
            df = custom_data.get_data_as_data_frame()
            pipeline = PredictPipeline()
            direct_prediction = pipeline.predict(df)[0]
            print(f"Direct Pipeline: ${direct_prediction:,.2f}")
        except Exception as e:
            print(f"Direct pipeline failed: {e}")
            direct_prediction = None
        
        try:
            url = "http://localhost:5000/api/predict"
            response = requests.post(url, json=test_case['data'], timeout=10)
            api_result = response.json()
            
            if api_result.get('success'):
                api_prediction = api_result['predicted_price']
                print(f"API Prediction: ${api_prediction:,.2f}")
            else:
                print(f"API failed: {api_result.get('error')}")
                api_prediction = None
        except Exception as e:
            print(f"API request failed: {e}")
            api_prediction = None
        
        if direct_prediction and api_prediction:
            difference = abs(direct_prediction - api_prediction)
            if difference < 1.0:
                print(f"Integration test passed (diff: ${difference:.2f})")
                status = "PASSED"
            else:
                print(f"Integration test failed (diff: ${difference:.2f})")
                status = "FAILED"
        else:
            status = "FAILED"
        
        results.append({
            "test_name": test_case['name'],
            "direct_prediction": direct_prediction,
            "api_prediction": api_prediction,
            "status": status
        })
    
    return results

if __name__ == "__main__":
    print("Starting Integration Tests...")
    print("Make sure your Flask app is running: python app.py")
    time.sleep(2)
    
    results = test_end_to_end_integration()
    
    print("\n" + "="*60)
    print("INTEGRATION TEST SUMMARY")
    print("="*60)
    
    for result in results:
        status_symbol = "PASS" if result['status'] == "PASSED" else "FAIL"
        print(f"[{status_symbol}] {result['test_name']}: {result['status']}")
        if result['direct_prediction']:
            print(f"   Direct: ${result['direct_prediction']:,.2f}")
        if result['api_prediction']:
            print(f"   API: ${result['api_prediction']:,.2f}")
    
    passed_tests = sum(1 for r in results if r['status'] == "PASSED")
    total_tests = len(results)
    
    if passed_tests == total_tests:
        print(f"\nALL {total_tests} INTEGRATION TESTS PASSED!")
    else:
        print(f"\n{passed_tests}/{total_tests} integration tests passed.")