# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained classifier pipeline
try:
    model = pickle.load(open('customer_dbscan_model.pkl', 'rb'))
except FileNotFoundError:
    print("Model file 'customer_dbscan_model.pkl' not found. Please run create_classifier_model.py first.")
    exit()

# Get the feature names from the dataset to build the form dynamically
try:
    df = pd.read_csv('Fresh-Milk-Grocery-Frozen-DetergentsPaper-Delicassen (1).csv')
    df_cols = df.drop(['Channel', 'Region'], axis=1).columns.tolist()
except (FileNotFoundError, KeyError):
    # Fallback if file is missing or doesn't have Channel/Region
    df_cols = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    if request.method == 'POST':
        try:
            # Collect all features from the form in the correct order
            input_features = [float(request.form[col]) for col in df_cols]
            final_features = np.array([input_features])

            # Make a prediction. The pipeline handles scaling automatically.
            prediction = model.predict(final_features)
            predicted_cluster_num = prediction[0]
            
            # Prepare the result for display
            if predicted_cluster_num == -1:
                 prediction_text = "Prediction: Outlier / Unclassified Customer"
            else:
                 prediction_text = f"Prediction: Belongs to Customer Segment #{predicted_cluster_num + 1}"
            
            prediction_result = {
                "class": f"cluster-{predicted_cluster_num}",
                "text": prediction_text
            }

        except Exception as e:
            prediction_result = {
                "class": "error",
                "text": f"Error: {e}. Please ensure all fields have valid numerical data."
            }
            
    return render_template('index.html', prediction_result=prediction_result, columns=df_cols)

if __name__ == "__main__":
    app.run(debug=True)