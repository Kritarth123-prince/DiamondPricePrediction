# Diamond Price Prediction System

A complete machine learning web application for predicting diamond prices based on the 4 C's (Carat, Cut, Color, Clarity) and physical dimensions using advanced ML algorithms.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6%2B-orange)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

## Features

- **Machine Learning Model**: Trained on comprehensive diamond dataset with multiple regression algorithms
- **Web Interface**: User-friendly Flask web application with responsive design
- **Real-time Predictions**: Instant price predictions for diamond specifications
- **Complete Pipeline**: End-to-end data processing and model training pipeline
- **Error Handling**: Robust error handling and comprehensive logging system
- **API Access**: REST API endpoint for programmatic integration
- **Responsive Design**: Works seamlessly across desktop and mobile devices

## Live Demo

**Successfully Tested Prediction:**
```
Input Specifications:
• Carat: 2.54
• Cut: Premium
• Color: D (Colorless)
• Clarity: VS1
• Depth: 75.0%
• Table: 70.0%
• Dimensions: 5.7mm × 6.87mm × 3.78mm

Predicted Price: $12,559.53
Price per Carat: $4,944.70
```

## Project Structure

```
DiamondPricePrediction/
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py           # Data loading and splitting
│   │   ├── data_transformation.py      # Feature engineering & preprocessing
│   │   └── model_trainer.py            # Model training & evaluation
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── train_pipeline.py           # Complete training pipeline
│   │   └── predict_pipeline.py         # Prediction pipeline
│   ├── __init__.py
│   ├── exception.py                    # Custom exception handling
│   ├── logger.py                       # Logging configuration
│   └── utils.py                        # Utility functions
├── templates/
│   ├── index.html                      # Landing page
│   └── home.html                       # Prediction interface
├── tests/
│   ├── __init__.py                     # Test package initialization
│   ├── test_pipeline.py                # Pipeline component tests
│   ├── test_api.py                     # API endpoint tests
│   └── test_integration.py             # End-to-end integration tests
├── artifacts/
│   ├── model.pkl                       # Trained ML model
│   ├── preprocessor.pkl                # Feature preprocessor
│   ├── train.csv                       # Training dataset
│   └── test.csv                        # Test dataset
├── notebooks/
│   └── Diamond_Price_Training.ipynb    # Model development notebook
├── logs/                               # Application logs directory
├── app.py                              # Flask web application
├── run_tests.py                        # Test runner script
├── requirements.txt                    # Project dependencies
├── setup.py                            # Package setup configuration
├── README.md                           # Project documentation
└── .gitignore                          # Git ignore rules
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Kritarth123-prince/DiamondPricePrediction.git
cd DiamondPricePrediction
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Open Browser
Navigate to: `http://localhost:5000`

## Model Performance

### Algorithms Tested
- **Linear Regression**: Baseline model
- **Random Forest**: Ensemble method for robust predictions
- **XGBoost**: Gradient boosting for high accuracy
- **Decision Tree**: Interpretable model
- **Support Vector Regression**: Non-linear relationships

### Key Metrics
- **R² Score**: High accuracy on test dataset
- **Mean Absolute Error**: Minimized prediction errors
- **Cross-validation**: Robust performance across data splits

### Features Used
1. **Carat**: Weight of the diamond (0.1 - 6.0)
2. **Cut**: Quality grade (Fair → Good → Very Good → Premium → Ideal)
3. **Color**: Color grade (D → E → F → G → H → I → J)
4. **Clarity**: Clarity grade (I1 → SI2 → SI1 → VS2 → VS1 → VVS2 → VVS1 → IF)
5. **Depth**: Depth percentage (50% - 80%)
6. **Table**: Table percentage (40% - 80%)
7. **X, Y, Z**: Physical dimensions in millimeters

## Usage Guide

### Web Interface
1. **Navigate** to the home page
2. **Enter diamond specifications**:
   - Carat weight (e.g., 1.5)
   - Cut quality from dropdown
   - Color grade from dropdown
   - Clarity grade from dropdown
   - Physical measurements
3. **Click** "Predict Price"
4. **View** instant price prediction

### API Usage
```python
import requests

# API endpoint
url = "http://localhost:5000/api/predict"

# Diamond specifications
diamond_data = {
    "carat": 1.5,
    "cut": "Premium",
    "color": "G",
    "clarity": "VS1",
    "depth": 61.5,
    "table": 57.0,
    "x": 7.3,
    "y": 7.35,
    "z": 4.5
}

# Make prediction request
response = requests.post(url, json=diamond_data)
result = response.json()

print(f"Predicted Price: ${result['predicted_price']:,.2f}")
print(f"Price per Carat: ${result['price_per_carat']:,.2f}")
```

### API Endpoints

#### 1. Health Check
```bash
GET /api/health
```
Response:
```json
{
    "status": "healthy",
    "service": "Diamond Price Prediction API",
    "timestamp": "2025-06-29 21:12:32",
    "version": "1.0.0"
}
```

#### 2. Predict Diamond Price
```bash
POST /api/predict
Content-Type: application/json
```
Request Body:
```json
{
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
```
Response:
```json
{
    "success": true,
    "predicted_price": 12559.53,
    "price_per_carat": 4944.70,
    "input_data": {...},
    "timestamp": "2025-06-29 21:12:32"
}
```

#### 3. Prediction History
```bash
GET /api/history
```
Response:
```json
{
    "success": true,
    "total_predictions": 15,
    "history": [...]
}
```

### Command Line Interface
```python
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Create diamond data
diamond = CustomData(
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

# Make prediction
pipeline = PredictPipeline()
price = pipeline.predict(diamond.get_data_as_data_frame())
print(f"Predicted Price: ${price[0]:,.2f}")
```

## Testing

### Test Structure
```
tests/
├── __init__.py                         # Test package initialization
├── test_pipeline.py                    # Unit tests for ML pipeline components
├── test_api.py                         # Integration tests for API endpoints
└── test_integration.py                 # End-to-end integration tests
```

### Prerequisites for Testing
Make sure your Flask application is running before executing tests:
```bash
python app.py
```

### Available Test Suites

#### 1. Pipeline Tests
Tests the core ML pipeline components including data processing, model loading, and prediction functionality:
```bash
python tests/test_pipeline.py
```

**Test Coverage:**
- CustomData object creation and validation
- DataFrame conversion and structure verification
- Model loading and prediction accuracy
- Error handling for invalid inputs

**Expected Output:**
```
Starting Pipeline Tests...
✓ CustomData creation test passed
✓ DataFrame conversion test passed
✓ Prediction test passed: $7,234.56
All pipeline tests passed!
```

#### 2. API Tests
Tests all REST API endpoints including validation, error handling, and response formats:
```bash
python tests/test_api.py
```

**Test Coverage:**
- Health check endpoint functionality
- Prediction endpoint with valid data
- Input validation and error responses
- Response format and data types
- Authentication and request handling

**Expected Output:**
```
Starting API Tests...
=== Health Check Results ===
Status: healthy
Service: Diamond Price Prediction API
✓ Health Check PASSED

=== API Test Results ===
Status Code: 200
Predicted Price: $12,559.53
Price per Carat: $4,944.70
✓ API Test PASSED

=== Validation Test Results ===
✓ Validation Test PASSED

ALL TESTS PASSED! Your API is working correctly.
```

#### 3. Integration Tests
Tests end-to-end functionality comparing direct pipeline predictions with API responses:
```bash
python tests/test_integration.py
```

**Test Coverage:**
- Direct ML pipeline execution
- API endpoint integration
- Result consistency verification
- Multiple test scenarios with different diamond types
- Performance and accuracy validation

**Expected Output:**
```
Starting Integration Tests...

--- Testing: Premium Large Diamond ---
Direct Pipeline: $12,559.53
API Prediction: $12,559.53
Integration test passed (diff: $0.00)

--- Testing: Small Good Diamond ---
Direct Pipeline: $1,847.23
API Prediction: $1,847.23
Integration test passed (diff: $0.00)

INTEGRATION TEST SUMMARY
[PASS] Premium Large Diamond: PASSED
   Direct: $12,559.53
   API: $12,559.53
[PASS] Small Good Diamond: PASSED
   Direct: $1,847.23
   API: $1,847.23

ALL 2 INTEGRATION TESTS PASSED!
```

#### 4. Complete Test Suite
Execute all tests in sequence with comprehensive reporting:
```bash
python run_tests.py
```

**Features:**
- Automatic server detection
- Sequential test execution
- Comprehensive result reporting
- Error tracking and debugging information
- Performance metrics

**Expected Output:**
```
Diamond Price Prediction - Test Suite
Flask server detected and running

Pipeline Tests
Pipeline Tests completed successfully

API Tests  
API Tests completed successfully

Integration Tests
Integration Tests completed successfully

FINAL TEST SUMMARY
PASSED - Pipeline Tests
PASSED - API Tests
PASSED - Integration Tests

Overall: 3/3 test suites passed
ALL TESTS PASSED! Your application is working correctly.
```

### Manual Testing

#### Browser Testing
1. Open `http://localhost:5000`
2. Navigate through the web interface
3. Test form validation and error handling
4. Verify prediction accuracy and response times

#### API Testing with cURL
```bash
# Test health endpoint
curl http://localhost:5000/api/health

# Test prediction endpoint
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "carat": 1.5,
    "cut": "Premium", 
    "color": "G",
    "clarity": "VS1",
    "depth": 61.5,
    "table": 57.0,
    "x": 7.3,
    "y": 7.35,
    "z": 4.5
  }'

# Test validation with missing fields
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "carat": 1.5,
    "cut": "Premium"
  }'
```

#### Performance Testing
```bash
# Test multiple concurrent requests
for i in {1..10}; do
  curl -X POST http://localhost:5000/api/predict \
    -H "Content-Type: application/json" \
    -d '{"carat":1.5,"cut":"Premium","color":"G","clarity":"VS1","depth":61.5,"table":57.0,"x":7.3,"y":7.35,"z":4.5}' &
done
wait
```

### Test Data Examples

#### Valid Test Cases
```python
test_cases = [
    {
        "name": "High-end Diamond",
        "data": {
            "carat": 3.0,
            "cut": "Ideal",
            "color": "D",
            "clarity": "IF",
            "depth": 62.0,
            "table": 57.0,
            "x": 9.1,
            "y": 9.1,
            "z": 5.6
        }
    },
    {
        "name": "Budget Diamond",
        "data": {
            "carat": 0.3,
            "cut": "Fair",
            "color": "J",
            "clarity": "I1",
            "depth": 65.0,
            "table": 60.0,
            "x": 4.2,
            "y": 4.1,
            "z": 2.7
        }
    }
]
```

#### Error Test Cases
```python
invalid_cases = [
    {"carat": -1.0},                    # Negative carat
    {"cut": "Invalid"},                 # Invalid cut grade
    {"color": "Z"},                     # Invalid color grade
    {"clarity": "Invalid"},             # Invalid clarity grade
    {"depth": 0},                       # Invalid depth
    {},                                 # Missing required fields
    {"carat": "not_a_number"}          # Invalid data type
]
```

## Development

### Project Setup for Development
```bash
# Install in development mode
pip install -e .

# Set up pre-commit hooks
pip install pre-commit
pre-commit install

# Start development server with debug mode
export FLASK_ENV=development  # Linux/macOS
set FLASK_ENV=development     # Windows
python app.py
```

### Model Training
```bash
# Train new model with your data
python src/pipeline/train_pipeline.py

# Evaluate model performance
python -c "from src.components.model_trainer import ModelTrainer; ModelTrainer().evaluate_model()"
```

### Code Quality
```bash
# Run code formatting
black src/ tests/

# Run linting
flake8 src/ tests/

# Type checking
mypy src/
```

## Requirements

```txt
pandas>=1.5.0
numpy>=1.21.0
scikit-learn>=1.6.0
xgboost>=2.0.0
flask>=2.0.0
matplotlib>=3.5.0
seaborn>=0.11.0
joblib>=1.3.0
dill>=0.3.6
requests>=2.28.0
```

## Deployment Options

### Local Development
```bash
python app.py
# Access at: http://localhost:5000
```

### Heroku Deployment
```bash
# Create Procfile
echo "web: python app.py" > Procfile

# Deploy to Heroku
heroku create diamond-price-predictor
git push heroku main
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
```

### Cloud Deployment
- **AWS**: Deploy using Elastic Beanstalk or EC2
- **Google Cloud**: Use App Engine or Cloud Run
- **Azure**: Deploy with App Service or Container Instances

## Contributing

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add unit tests for new features
- Update documentation for API changes
- Ensure backward compatibility
- Test thoroughly before submitting

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Kritarth Ranjan**
- **GitHub**: [@Kritarth123-prince](https://github.com/Kritarth123-prince)
- **Email**: kritarthranjan5053@gmail.com

## Acknowledgments

- **Dataset**: Diamond dataset from Kaggle
- **ML Libraries**: Scikit-learn, XGBoost for machine learning capabilities
- **Web Framework**: Flask for web application development
- **UI/UX**: HTML5, CSS3 for responsive design
- **Community**: Open source community for inspiration and support

## Support

If you encounter any issues or have questions:

1. **Check** the [Issues](https://github.com/Kritarth123-prince/DiamondPricePrediction/issues) page
2. **Create** a new issue with detailed description
3. **Contact** me directly via email

## Project Stats

![GitHub Stars](https://img.shields.io/github/stars/Kritarth123-prince/DiamondPricePrediction?style=social)
![GitHub Forks](https://img.shields.io/github/forks/Kritarth123-prince/DiamondPricePrediction?style=social)
![GitHub Issues](https://img.shields.io/github/issues/Kritarth123-prince/DiamondPricePrediction)
![GitHub Last Commit](https://img.shields.io/github/last-commit/Kritarth123-prince/DiamondPricePrediction)

**Ready to predict diamond prices like a pro! 💎✨**


Developed by
<mark> **Developer [Kritarth](https://github.com/Kritarth123-prince) & [Manish](https://github.com/Manish-Nailwal)** </mark> 
### Project of Machine Learning OOPs
