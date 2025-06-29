# 💎 Diamond Price Prediction System MLOp

A complete machine learning web application for predicting diamond prices based on the 4 C's (Carat, Cut, Color, Clarity) and physical dimensions using advanced ML algorithms.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6%2B-orange)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

## 🌟 Features

- **🤖 Machine Learning Model**: Trained on comprehensive diamond dataset with multiple regression algorithms
- **🌐 Web Interface**: User-friendly Flask web application with responsive design
- **⚡ Real-time Predictions**: Instant price predictions for diamond specifications
- **🔄 Complete Pipeline**: End-to-end data processing and model training pipeline
- **🛡️ Error Handling**: Robust error handling and comprehensive logging system
- **📊 API Access**: REST API endpoint for programmatic integration
- **📱 Responsive Design**: Works seamlessly across desktop and mobile devices

## 🚀 Live Demo

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

## 📁 Project Structure

```
DiamondPricePrediction/
├── 📁 src/
│   ├── 📁 components/
│   │   ├── 📄 data_ingestion.py       # Data loading and splitting
│   │   ├── 📄 data_transformation.py  # Feature engineering & preprocessing
│   │   └── 📄 model_trainer.py        # Model training & evaluation
│   ├── 📁 pipeline/
│   │   ├── 📄 train_pipeline.py       # Complete training pipeline
│   │   └── 📄 predict_pipeline.py     # Prediction pipeline
│   ├── 📄 exception.py                # Custom exception handling
│   ├── 📄 logger.py                   # Logging configuration
│   └── 📄 utils.py                    # Utility functions
├── 📁 templates/
│   ├── 📄 index.html                  # Landing page
│   └── 📄 home.html                   # Prediction interface
├── 📁 artifacts/
│   ├── 📄 model.pkl                   # Trained ML model
│   ├── 📄 preprocessor.pkl            # Feature preprocessor
│   ├── 📄 train.csv                   # Training dataset
│   └── 📄 test.csv                    # Test dataset
├── 📁 notebooks/
│   └── 📄 Diamond_Price_Training.ipynb # Model development notebook
├── 📄 app.py                          # Flask web application
├── 📄 requirements.txt                # Project dependencies
├── 📄 setup.py                        # Package setup configuration
├── 📄 README.md                       # Project documentation
└── 📄 .gitignore                      # Git ignore rules
```

## 🛠️ Installation & Setup

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

## 📊 Model Performance

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

## 🎯 Usage Guide

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

## 🔧 Development

### Project Setup for Development
```bash
# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/

# Start development server
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

## 📋 Requirements

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
```

## 🚀 Deployment Options

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

### Streamlit Cloud
```python
# Create streamlit_app.py for Streamlit deployment
import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.title("💎 Diamond Price Prediction")
# Add your Streamlit interface here
```

## 🧪 Testing

### Manual Testing
1. **Web Interface**: Test all form inputs and validations
2. **API Endpoints**: Use Postman or curl for API testing
3. **Edge Cases**: Test with extreme values and edge cases

### Automated Testing
```bash
# Run unit tests
python -m pytest tests/test_pipeline.py

# Test API endpoints
python tests/test_api.py

# Integration tests
python tests/test_integration.py
```

## 📈 Future Enhancements

- [ ] **Advanced Features**: Add fluorescence, symmetry, polish grades
- [ ] **Model Improvements**: Implement deep learning models (Neural Networks)
- [ ] **Real-time Updates**: Live market price integration
- [ ] **Mobile App**: Native mobile application development
- [ ] **User Authentication**: User accounts and prediction history
- [ ] **Advanced Analytics**: Price trend analysis and insights
- [ ] **Batch Predictions**: Upload CSV for bulk predictions
- [ ] **Model Monitoring**: Performance tracking and drift detection
- [ ] **A/B Testing**: Compare different model versions
- [ ] **Caching**: Redis integration for improved performance

## 🤝 Contributing

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

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Kritarth Ranjan**
- **GitHub**: [@Kritarth123-prince](https://github.com/Kritarth123-prince)
- **Email**: kritarthranjan5053@gmail.com
- **LinkedIn**: [Connect with me](https://linkedin.com/in/kritarth-ranjan)

## 🙏 Acknowledgments

- **Dataset**: Diamond dataset from Kaggle
- **ML Libraries**: Scikit-learn, XGBoost for machine learning capabilities
- **Web Framework**: Flask for web application development
- **UI/UX**: HTML5, CSS3 for responsive design
- **Community**: Open source community for inspiration and support

## 📞 Support

If you encounter any issues or have questions:

1. **Check** the [Issues](https://github.com/Kritarth123-prince/DiamondPricePrediction/issues) page
2. **Create** a new issue with detailed description
3. **Contact** me directly via email

## 🌟 Show Your Support

If this project helped you, please consider:
- ⭐ **Starring** the repository
- 🍴 **Forking** for your own use
- 📢 **Sharing** with others
- 💡 **Contributing** improvements

---

**Built with ❤️ by Kritarth Ranjan**

*Last Updated: June 29, 2025*

---

## 📊 Project Stats

![GitHub Stars](https://img.shields.io/github/stars/Kritarth123-prince/DiamondPricePrediction?style=social)
![GitHub Forks](https://img.shields.io/github/forks/Kritarth123-prince/DiamondPricePrediction?style=social)
![GitHub Issues](https://img.shields.io/github/issues/Kritarth123-prince/DiamondPricePrediction)
![GitHub Last Commit](https://img.shields.io/github/last-commit/Kritarth123-prince/DiamondPricePrediction)

**Ready to predict diamond prices like a pro! 💎✨**


Developed by
<mark> **Developer [Kritarth](https://github.com/Kritarth123-prince) & [Manish](https://github.com/Manish-Nailwal)** </mark> 
### Project of Machine Learning OOPs
