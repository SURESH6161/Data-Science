# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model pipeline
try:
    model = pickle.load(open('student_success_knn_model.pkl', 'rb'))
except FileNotFoundError:
    print("Model file 'student_success_knn_model.pkl' not found. Please run create_model.py first.")
    exit()

# Get the feature names from the dataset to build the form dynamically
target_column_name = pd.read_csv('knn_student_success_data.csv').columns[-1]
df_cols = pd.read_csv('knn_student_success_data.csv').drop(target_column_name, axis=1).columns.tolist()


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
            
            # Prepare the result for display
            if prediction[0] == 1:
                prediction_result = {
                    "class": "positive",
                    "text": "Predicted Outcome: Likely to Succeed"
                }
            else:
                prediction_result = {
                    "class": "negative",
                    "text": "Predicted Outcome: Unlikely to Succeed"
                }

        except Exception as e:
            prediction_result = {
                "class": "negative",
                "text": f"Error: {e}. Please ensure all fields have valid numerical data."
            }

    # Pass the column names to the template to dynamically generate the form
    return render_template('index.html', prediction_result=prediction_result, columns=df_cols)

if __name__ == "__main__":
    app.run(debug=True)