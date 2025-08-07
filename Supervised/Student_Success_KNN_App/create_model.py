# create_model.py

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pickle

print("Starting model training process...")

# Load the dataset
try:
    df = pd.read_csv('knn_student_success_data.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'knn_student_success_data.csv' not found. Please place it in the project folder.")
    exit()

# --- AUTOMATIC TARGET DETECTION ---
# This script assumes the LAST column in your CSV is the target variable.
target_column_name = df.columns[-1]
print(f"Automatically identified '{target_column_name}' as the target column.")
# ---------------------------------

# Prepare the data using the automatically detected target column
X = df.drop(target_column_name, axis=1)
y = df[target_column_name]

# Create a pipeline that first scales the data, then trains the KNN classifier.
print("Defining the model pipeline (Scaler + KNN)...")
pipeline = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5) # Using 5 neighbors as a standard default
)

# Train the model pipeline on the entire dataset
print("Training the model...")
pipeline.fit(X, y)

# Save the entire pipeline (scaler + model) to a file
with open('student_success_knn_model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("\nModel training complete!")
print("Pipeline saved as 'student_success_knn_model.pkl'")