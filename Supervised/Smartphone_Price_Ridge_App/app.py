# app.py

from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# --- NEW: Define the currency conversion rate ---
USD_TO_INR_RATE = 87.72

# Load the trained model pipeline and the model columns
try:
    model = pickle.load(open('ridge_model.pkl', 'rb'))
    model_columns = pickle.load(open('model_columns.pkl', 'rb'))
except FileNotFoundError:
    print("Model or column files not found. Please run create_model.py first.")
    exit()

# Define the options for the dropdowns based on your features
brands = ['Apple', 'Samsung', 'Xiaomi', 'Realme', 'Vivo', 'OPPO', 'Motorola', 'Google', 'OnePlus', 'Nokia']
# Define the columns based on your CSV
original_numerical_cols = ['Model_Year', 'Screen_Size_Inches', 'RAM_GB', 'Storage_GB', 'Battery_mAh', 'Camera_MP', 'Weight_g']
original_categorical_cols = ['Brand']

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
            input_df_aligned = input_df_processed.reindex(columns=model_columns, fill_value=0)

            # Make a prediction in USD
            prediction_usd = model.predict(input_df_aligned)
            predicted_price_usd = prediction_usd[0]
            
            # --- NEW: Convert the predicted price to INR ---
            predicted_price_inr = predicted_price_usd * USD_TO_INR_RATE
            
            # Prepare the result for display in Rupees
            prediction_result = {
                "class": "positive",
                # --- CHANGED: Format the output string in Rupees ---
                "text": f"Predicted Price: ₹{predicted_price_inr:,.2f}"
            }

        except Exception as e:
            prediction_result = {
                "class": "negative",
                "text": f"Error: {e}. Please ensure all fields are filled correctly."
            }
            
    return render_template('index.html', prediction_result=prediction_result, brands=brands)

if __name__ == "__main__":
    app.run(debug=True)