# create_model.py

import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pickle

print("Starting model training process...")

# Load the dataset
try:
    df = pd.read_csv('credit_fraud_data.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'credit_fraud_data.csv' not found. Please place it in the project folder.")
    exit()

# --- AUTOMATIC TARGET DETECTION ---
# This script assumes the LAST column in your CSV is the target variable.
target_column_name = df.columns[-1] 
print(f"Automatically identified '{target_column_name}' as the target column.")
# ---------------------------------

# Prepare the data using the automatically detected target column
X = df.drop(target_column_name, axis=1)
y = df[target_column_name]

# Create a pipeline that first scales the data, then trains the SVM.
print("Defining the model pipeline (Scaler + SVM)...")
pipeline = make_pipeline(
    StandardScaler(),
    SVC(kernel='linear', class_weight='balanced', random_state=42, probability=True)
)

# Train the model pipeline on the entire dataset
print("Training the model... This may take several minutes depending on dataset size.")
pipeline.fit(X, y)

# Save the entire pipeline (scaler + model) to a file
with open('fraud_svm_model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("\nModel training complete!")
print("Pipeline saved as 'fraud_svm_model.pkl'")