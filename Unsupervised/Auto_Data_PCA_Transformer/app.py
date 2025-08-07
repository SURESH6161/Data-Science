# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained PCA pipeline and the feature list
try:
    model = pickle.load(open('auto_pca_model.pkl', 'rb'))
    original_features = pickle.load(open('model_features.pkl', 'rb'))
    numerical_cols = original_features['numerical']
except FileNotFoundError:
    print("Model or feature files not found. Please run create_pca_model.py first.")
    exit()

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    if request.method == 'POST':
        try:
            # Collect all numerical features from the form
            input_data = {col: [float(request.form[col])] for col in numerical_cols}

            # Create a pandas DataFrame from the user input
            input_df = pd.DataFrame.from_dict(input_data)
            
            # Use the pipeline to TRANSFORM the data (not predict)
            transformed_data = model.transform(input_df)
            
            pc1 = transformed_data[0][0]
            pc2 = transformed_data[0][1]
            
            # Prepare the result for display
            prediction_result = {
                "class": "positive",
                "text": f"Transformed Coordinates => PC1: {pc1:.4f}, PC2: {pc2:.4f}"
            }

        except Exception as e:
            prediction_result = {
                "class": "negative",
                "text": f"Error: {e}. Please ensure all fields are filled correctly."
            }
            
    return render_template('index.html', prediction_result=prediction_result, columns=numerical_cols)

if __name__ == "__main__":
    app.run(debug=True)