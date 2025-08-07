# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model pipeline and the model columns
try:
    model = pickle.load(open('loan_default_gb_model.pkl', 'rb'))
    model_columns = pickle.load(open('model_columns.pkl', 'rb'))
except FileNotFoundError:
    print("Model or column files not found. Please run create_model.py first.")
    exit()

# These original columns are needed to build the form and process input
# You may need to adjust these based on your actual CSV file
original_numerical_cols = ['loan_amount', 'interest_rate', 'term', 'income', 'credit_score', 'age', 'employment_length']
original_categorical_cols = ['home_ownership', 'purpose']

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    if request.method == 'POST':
        try:
            # Create a dictionary to hold user input
            input_data = {}
            for col in original_numerical_cols:
                input_data[col] = [float(request.form[col])]
            for col in original_categorical_cols:
                input_data[col] = [request.form[col]]

            # Create a pandas DataFrame from the user input
            input_df = pd.DataFrame.from_dict(input_data)
            
            # Perform one-hot encoding on the input DataFrame
            input_df_processed = pd.get_dummies(input_df, columns=original_categorical_cols, drop_first=True)
            
            # Align columns with the training data
            # This adds missing dummy columns (with value 0) and ensures order is the same
            input_df_aligned = input_df_processed.reindex(columns=model_columns, fill_value=0)

            # Make a prediction
            prediction = model.predict(input_df_aligned)
            probability = model.predict_proba(input_df_aligned)[0][1] # Probability of default
            
            # Prepare the result for display
            if prediction[0] == 1:
                prediction_result = {
                    "class": "positive",
                    "text": f"Prediction: High Risk of Default (Confidence: {probability*100:.2f}%)"
                }
            else:
                prediction_result = {
                    "class": "negative",
                    "text": f"Prediction: Likely to be Repaid (Default Risk: {probability*100:.2f}%)"
                }

        except Exception as e:
            prediction_result = {
                "class": "positive",
                "text": f"Error: {e}. Please ensure all fields are filled correctly."
            }
            
    return render_template('index.html', prediction_result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)