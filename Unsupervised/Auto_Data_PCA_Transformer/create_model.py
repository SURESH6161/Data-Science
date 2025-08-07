# create_pca_model.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
import pickle

print("Starting PCA model creation process...")

# Load the dataset
try:
    # The dataset uses '?' for missing values, so we specify that
    df = pd.read_csv('auoto_data.csv', na_values='?')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'auoto_data.csv' not found. Please place it in the project folder.")
    exit()

# --- Data Preprocessing ---
print("Cleaning and preprocessing data...")

# FIX: Check if 'car name' column exists before trying to drop it
if 'car name' in df.columns:
    df = df.drop(['car name'], axis=1)
    print("Dropped 'car name' column.")
else:
    print("'car name' column not found, skipping drop.")

# Handle missing values by filling with the median of each column
for col in df.columns:
    if df[col].isnull().any():
        median = df[col].median()
        df[col] = df[col].fillna(median)

# Use all remaining columns as features for PCA
X = df

# Save the original column order for the app
original_features = {
    'numerical': X.select_dtypes(include=np.number).columns.tolist(),
}
with open('model_features.pkl', 'wb') as file:
    pickle.dump(original_features, file)
print("Original feature list saved to model_features.pkl")


# --- PCA Model Training ---
# Create a pipeline that first scales the data, then applies PCA.
pipeline = make_pipeline(
    StandardScaler(),
    PCA(n_components=2, random_state=42)
)

print("Fitting the PCA pipeline...")
pipeline.fit(X)

# Save the entire pipeline (scaler + PCA model) to a file
with open('auto_pca_model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("\nPCA model creation complete!")
print("Pipeline saved as 'auto_pca_model.pkl'")