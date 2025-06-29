from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from datetime import datetime
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Store prediction history (optional)
prediction_history = []

## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                carat=float(request.form.get('carat')),
                cut=request.form.get('cut'),
                color=request.form.get('color'),
                clarity=request.form.get('clarity'),
                depth=float(request.form.get('depth')),
                table=float(request.form.get('table')),
                x=float(request.form.get('x')),
                y=float(request.form.get('y')),
                z=float(request.form.get('z'))
            )
            
            pred_df = data.get_data_as_data_frame()
            print("Input data:")
            print(pred_df)
            
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            # Store prediction in history (optional)
            prediction_record = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'input': pred_df.to_dict('records')[0],
                'predicted_price': float(results[0])
            }
            prediction_history.append(prediction_record)
            
            return render_template('home.html', results=f"${results[0]:,.2f}")
        
        except Exception as e:
            print(f"Error in prediction: {str(e)}")
            return render_template('home.html', results=f"Error: {str(e)}")

## API Endpoint for Programmatic Access
@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        if not request.is_json:
            return jsonify({
                'success': False,
                'error': 'Content-Type must be application/json'
            }), 400
        
        json_data = request.get_json()
        
        # Validate required fields
        required_fields = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']
        missing_fields = [field for field in required_fields if field not in json_data]
        
        if missing_fields:
            return jsonify({
                'success': False,
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        # Create CustomData object
        data = CustomData(
            carat=float(json_data['carat']),
            cut=str(json_data['cut']),
            color=str(json_data['color']),
            clarity=str(json_data['clarity']),
            depth=float(json_data['depth']),
            table=float(json_data['table']),
            x=float(json_data['x']),
            y=float(json_data['y']),
            z=float(json_data['z'])
        )
        
        # Convert to DataFrame and make prediction
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        # Calculate price per carat
        price_per_carat = float(results[0]) / float(json_data['carat'])
        
        # Store prediction in history
        prediction_record = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'input': json_data,
            'predicted_price': float(results[0])
        }
        prediction_history.append(prediction_record)
        
        return jsonify({
            'success': True,
            'predicted_price': round(float(results[0]), 2),
            'price_per_carat': round(price_per_carat, 2),
            'input_data': json_data,
            'timestamp': prediction_record['timestamp']
        })
        
    except ValueError as ve:
        return jsonify({
            'success': False,
            'error': f'Invalid data type: {str(ve)}'
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Prediction failed: {str(e)}'
        }), 500

## API endpoint to get prediction history
@app.route('/api/history', methods=['GET'])
def api_history():
    return jsonify({
        'success': True,
        'total_predictions': len(prediction_history),
        'history': prediction_history[-10:]  # Return last 10 predictions
    })

## Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'Diamond Price Prediction API',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'version': '1.0.0'
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)