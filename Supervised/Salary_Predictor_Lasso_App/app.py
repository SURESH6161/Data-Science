# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model pipeline
try:
    model = pickle.load(open('lasso_salary_model.pkl', 'rb'))
except FileNotFoundError:
    print("Model file 'lasso_salary_model.pkl' not found. Please run create_model.py first.")
    exit()

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    if request.method == 'POST':
        try:
            # Get user input from the form
            experience = float(request.form['experience'])

            # Prepare the feature for prediction (must be a 2D array)
            final_features = np.array([[experience]])

            # Make a prediction. The pipeline handles scaling automatically.
            prediction = model.predict(final_features)
            predicted_salary = prediction[0]
            
            # Prepare the result for display
            prediction_result = {
                "class": "positive",
                "text": f"Predicted Salary: ${predicted_salary:,.2f} per year"
            }

        except Exception as e:
            prediction_result = {
                "class": "negative",
                "text": f"Error: {e}. Please enter a valid number."
            }
            
    return render_template('index.html', prediction_result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)