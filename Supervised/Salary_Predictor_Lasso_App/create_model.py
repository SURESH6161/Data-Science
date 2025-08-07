# create_model.py

import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pickle

print("Starting model training process...")

# Load the dataset
try:
    df = pd.read_csv('experience_salary.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'experience_salary.csv' not found. Please place it in the project folder.")
    exit()

# --- Data Preprocessing ---
# Assuming the first column is the feature (YearsExperience) and the second is the target (Salary)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

print(f"Using '{df.columns[0]}' as the feature and '{df.columns[-1]}' as the target.")

# --- Model Training ---
# Create a pipeline that first scales the data, then trains the Lasso model.
pipeline = make_pipeline(
    StandardScaler(),
    Lasso(alpha=1.0, random_state=42)
)

print("Training the Lasso Regression model...")
pipeline.fit(X, y)

# Save the entire pipeline (scaler + model) to a file
with open('lasso_salary_model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("\nModel training complete!")
print("Pipeline saved as 'lasso_salary_model.pkl'")