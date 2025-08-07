# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    model = pickle.load(open('diabetes_model.pkl', 'rb'))
except FileNotFoundError:
    print("Model file 'diabetes_model.pkl' not found. Please run create_model.py first.")
    exit()

# Define the main route for the web page
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    if request.method == 'POST':
        try:
            # Get user input from the form
            features = [
                int(request.form['pregnancies']),
                int(request.form['glucose']),
                int(request.form['blood_pressure']),
                int(request.form['skin_thickness']),
                int(request.form['insulin']),
                float(request.form['bmi']),
                float(request.form['diabetes_pedigree']),
                int(request.form['age'])
            ]
            final_features = np.array([features])

            # Make a prediction
            prediction = model.predict(final_features)
            
            # Prepare the result for display
            if prediction[0] == 1:
                prediction_result = {
                    "class": "positive",
                    "text": "Prediction: High probability of Diabetes."
                }
            else:
                prediction_result = {
                    "class": "negative",
                    "text": "Prediction: Low probability of Diabetes."
                }

        except Exception as e:
            prediction_result = {
                "class": "positive",
                "text": f"Error: {e}. Please enter valid data for all fields."
            }

    # Render the web page with the prediction result
    return render_template('index.html', prediction_result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)