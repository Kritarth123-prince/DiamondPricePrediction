import requests
import json
import time

def test_api_predict():
    url = "http://localhost:5000/api/predict"
    test_diamond = {
        "carat": 2.54,
        "cut": "Premium",
        "color": "D",
        "clarity": "VS1",
        "depth": 75.0,
        "table": 70.0,
        "x": 5.7,
        "y": 6.87,
        "z": 3.78
    }
    
    try:
        response = requests.post(url, json=test_diamond, timeout=10)
        result = response.json()
        
        print("=== API Test Results ===")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(result, indent=2)}")
        
        if result.get('success'):
            print(f"API Test PASSED")
            print(f"Predicted Price: ${result['predicted_price']:,.2f}")
            print(f"Price per Carat: ${result['price_per_carat']:,.2f}")
            return True
        else:
            print(f"API Test FAILED: {result.get('error')}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("Connection Error: Make sure Flask app is running on localhost:5000")
        return False
    except Exception as e:
        print(f"API Test FAILED: {str(e)}")
        return False

def test_api_health():
    url = "http://localhost:5000/api/health"
    
    try:
        response = requests.get(url, timeout=5)
        result = response.json()
        
        print("\n=== Health Check Results ===")
        print(f"Status: {result.get('status')}")
        print(f"Service: {result.get('service')}")
        print(f"Timestamp: {result.get('timestamp')}")
        
        if result.get('status') == 'healthy':
            print("Health Check PASSED")
            return True
        else:
            print("Health Check FAILED")
            return False
            
    except Exception as e:
        print(f"Health Check FAILED: {str(e)}")
        return False

def test_api_validation():
    url = "http://localhost:5000/api/predict"
    
    incomplete_data = {
        "carat": 1.5,
        "cut": "Premium"
    }
    
    try:
        response = requests.post(url, json=incomplete_data, timeout=5)
        result = response.json()
        
        print("\n=== Validation Test Results ===")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(result, indent=2)}")
        
        if not result.get('success') and 'Missing required fields' in result.get('error', ''):
            print("Validation Test PASSED")
            return True
        else:
            print("Validation Test FAILED")
            return False
            
    except Exception as e:
        print(f"Validation Test FAILED: {str(e)}")
        return False

if __name__ == "__main__":
    print("Starting API Tests...")
    print("Make sure your Flask app is running: python app.py")
    time.sleep(2)
    
    # Run tests
    health_passed = test_api_health()
    predict_passed = test_api_predict()
    validation_passed = test_api_validation()
    
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"Health Check: {'PASSED' if health_passed else 'FAILED'}")
    print(f"API Prediction: {'PASSED' if predict_passed else 'FAILED'}")
    print(f"Input Validation: {'PASSED' if validation_passed else 'FAILED'}")
    
    if all([health_passed, predict_passed, validation_passed]):
        print("\nALL TESTS PASSED! Your API is working correctly.")
    else:
        print("\nSome tests failed. Check the errors above.")