# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
try:
    model = pickle.load(open('movie_model.pkl', 'rb'))
except FileNotFoundError:
    print("Model file not found. Please run create_model.py first.")
    exit()

# Define the main route for the web page
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = ''
    if request.method == 'POST':
        try:
            # Get user input from the form
            age = int(request.form['age'])
            gender = int(request.form['gender'])

            # Prepare the features for prediction
            final_features = np.array([[age, gender]])

            # Make a prediction
            prediction = model.predict(final_features)
            output = prediction[0]

            # Create the result text
            prediction_text = f'Predicted Movie Genre: {output}'

        except Exception as e:
            prediction_text = f'Error: {e}. Please enter valid data.'

    # Render the web page
    return render_template('index.html', prediction_text=prediction_text)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)