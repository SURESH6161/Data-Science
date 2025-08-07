# app.py

from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model pipeline
try:
    model = pickle.load(open('spam_model.pkl', 'rb'))
except FileNotFoundError:
    print("Model file 'spam_model.pkl' not found. Please run create_model.py first.")
    exit()

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_result = None
    if request.method == 'POST':
        try:
            # Get the message from the form
            message = request.form['message']

            # The model expects a list of strings, so we pass the message in a list
            data = [message]

            # Make a prediction. The pipeline handles vectorizing and classifying.
            prediction = model.predict(data)
            
            # Prepare the result for display
            if prediction[0] == 1:
                prediction_result = {
                    "class": "positive",
                    "text": "Prediction: This message is SPAM."
                }
            else:
                prediction_result = {
                    "class": "negative",
                    "text": "Prediction: This message is NOT SPAM (Ham)."
                }

        except Exception as e:
            prediction_result = {
                "class": "positive",
                "text": f"Error: {e}. Please enter valid text."
            }

    return render_template('index.html', prediction_result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)