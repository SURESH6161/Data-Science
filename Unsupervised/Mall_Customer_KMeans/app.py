# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained K-Means model
try:
    model = pickle.load(open('kmeans_model.pkl', 'rb'))
except FileNotFoundError:
    print("Model file 'kmeans_model.pkl' not found. Please run create_model.py first.")
    exit()

# Define meaningful names for the clusters.
# The cluster numbers (0-4) are assigned by the algorithm. We map them to descriptive names.
# NOTE: The cluster number for each group might change if the training data changes.
# For the standard dataset with random_state=42, this mapping is consistent.
cluster_names = {
    0: 'Standard Customers (Average Income, Average Spend)',
    1: 'Target Customers (High Income, High Spend)',
    2: 'Sensible Spenders (Low Income, Low Spend)',
    3: 'Careless Spenders (Low Income, High Spend)',
    4: 'Careful Spenders (High Income, Low Spend)',
}

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    if request.method == 'POST':
        try:
            # Get user input from the form
            annual_income = int(request.form['annual_income'])
            spending_score = int(request.form['spending_score'])

            # Prepare the features for prediction
            final_features = np.array([[annual_income, spending_score]])

            # Make a prediction (predict the cluster number)
            prediction = model.predict(final_features)
            predicted_cluster_num = prediction[0]
            
            # Get the meaningful cluster name
            predicted_cluster_name = cluster_names.get(predicted_cluster_num, "Unknown Cluster")
            
            # Prepare the result for display
            prediction_result = {
                "class": f"cluster-{predicted_cluster_num}",
                "text": f"Prediction: Belongs to '{predicted_cluster_name}' group."
            }

        except Exception as e:
            prediction_result = {
                "class": "error",
                "text": f"Error: {e}. Please enter valid integer data."
            }

    return render_template('index.html', prediction_result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)