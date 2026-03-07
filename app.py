from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model, scaler, and column names
model = joblib.load('best_model.joblib')
scaler = joblib.load('scaler.joblib')
model_columns = joblib.load('model_columns.joblib')

# Identify ALL numerical columns the scaler expects (from the fitted scaler object)
all_numeric_cols = scaler.feature_names_in_.tolist()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    input_data = pd.DataFrame([data])

    # Convert all columns to numeric where applicable
    for col in input_data.columns:
        try:
            input_data[col] = pd.to_numeric(input_data[col])
        except ValueError:
            pass

    # Align columns with model_columns, filling missing with 0
    input_data_processed = pd.DataFrame(0, index=[0], columns=model_columns)
    for col in input_data.columns:
        if col in model_columns:
            input_data_processed[col] = input_data[col]

    # Handle categorical encoding (one-hot logic)
    # Note: This app assumes the form names match the categorical column names before dummying
    # or that the user provides values for the dummied columns. 
    # In a production app, you'd map 'policy_csl' to 'policy_csl_250/500' etc.
    # For this implementation, we ensure dummied columns are updated based on form values.
    for col in model_columns:
        if '_' in col:
            prefix = col.rsplit('_', 1)[0]
            val = col.rsplit('_', 1)[1]
            if prefix in data and str(data[prefix]) == val:
                input_data_processed[col] = 1

    # Apply scaler to ALL numerical columns
    input_data_processed[all_numeric_cols] = scaler.transform(
        input_data_processed[all_numeric_cols]
    )
    
    # Make prediction
    prediction = model.predict(input_data_processed)
    result = 'Fraud' if prediction[0] == 'Y' else 'No Fraud'
    
    return render_template('index.html', prediction_text=f'The insurance claim is predicted to be: {result}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
