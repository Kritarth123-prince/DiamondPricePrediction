import subprocess
import sys
import time
import requests

def check_server_running():
    try:
        response = requests.get("http://localhost:5000/api/health", timeout=2)
        return response.status_code == 200
    except:
        return False

def run_command(command, description):
    print(f"\n{'='*50}")
    print(f"{description}")
    print('='*50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=False, text=True)
        if result.returncode == 0:
            print(f"{description} completed successfully")
            return True
        else:
            print(f"{description} failed")
            return False
    except Exception as e:
        print(f"{description} failed with error: {e}")
        return False

def main():
    print("Diamond Price Prediction - Test Suite")
    print("="*60)
    
    # Check if server is running
    if not check_server_running():
        print("Flask server not detected on localhost:5000")
        print("Please start the server first: python app.py")
        print("Then run this test suite again.")
        return
    
    print("Flask server detected and running")
    
    # Run tests
    results = []
    
    # Test 1: Pipeline tests
    results.append(run_command("python tests/test_pipeline.py", "Pipeline Tests"))
    
    # Test 2: API tests  
    results.append(run_command("python tests/test_api.py", "API Tests"))
    
    # Test 3: Integration tests
    results.append(run_command("python tests/test_integration.py", "Integration Tests"))
    
    # Summary
    print("\n" + "="*60)
    print("FINAL TEST SUMMARY")
    print("="*60)
    
    passed = sum(results)
    total = len(results)
    
    test_names = ["Pipeline Tests", "API Tests", "Integration Tests"]
    for i, (name, passed) in enumerate(zip(test_names, results)):
        status = "PASSED" if passed else "FAILED"
        print(f"{status} - {name}")
    
    print(f"\nOverall: {passed}/{total} test suites passed")
    
    if passed == total:
        print("ALL TESTS PASSED! Your application is working correctly.")
    else:
        print("Some tests failed. Check the output above for details.")

if __name__ == "__main__":
    main()