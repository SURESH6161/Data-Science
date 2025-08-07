# create_model.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load the dataset
try:
    df = pd.read_csv('diabetes.csv')
except FileNotFoundError:
    print("Error: 'diabetes.csv' not found. Please place the dataset in the project folder.")
    exit()

# Prepare the data
X = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = df['outcome']

# Initialize and train the Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save the trained model to a file
with open('diabetes_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as diabetes_model.pkl")