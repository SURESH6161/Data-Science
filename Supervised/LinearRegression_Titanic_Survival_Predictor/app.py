# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the new Linear Regression model
try:
    model = pickle.load(open('titanic_linear_model.pkl', 'rb'))
except FileNotFoundError:
    print("Model file 'titanic_linear_model.pkl' not found. Please run create_model.py first.")
    exit()

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    if request.method == 'POST':
        try:
            # Get user input from the form
            pclass = int(request.form['pclass'])
            age = float(request.form['age'])
            sibsp = int(request.form['sibsp'])
            parch = int(request.form['parch'])
            fare = float(request.form['fare'])
            sex = int(request.form['sex'])
            embarked = request.form['embarked']

            # Transform input to match model's training data
            passenger_id = 0
            embarked_q = 1 if embarked == 'Q' else 0
            embarked_s = 1 if embarked == 'S' else 0
            male = sex
            
            # Create the final feature array in the correct order
            final_features = np.array([[passenger_id, pclass, age, sibsp, parch, fare, male, embarked_q, embarked_s]])

            # --- Prediction Logic Changed for Linear Regression ---
            prediction_score = model.predict(final_features)[0]
            
            # Interpret the continuous score with a 0.5 threshold
            if prediction_score > 0.5:
                prediction_result = {
                    "class": "positive",
                    "text": f"Prediction: Survived (Score: {prediction_score:.2f})"
                }
            else:
                prediction_result = {
                    "class": "negative",
                    "text": f"Prediction: Did Not Survive (Score: {prediction_score:.2f})"
                }

        except Exception as e:
            prediction_result = {
                "class": "negative",
                "text": f"Error: {e}. Please enter valid data."
            }

    return render_template('index.html', prediction_result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)