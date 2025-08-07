# create_model.py

import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pickle

# --- CONFIGURATION ---
# This section is now updated with your exact column names.
features_to_use = ['Brand', 'Model_Year', 'Screen_Size_Inches', 'RAM_GB', 'Storage_GB', 'Battery_mAh', 'Camera_MP', 'Weight_g']
target_column = 'Price_USD'
categorical_features = ['Brand'] # Only 'Brand' is categorical in your list
# ---------------------


print("Starting model training process...")

# Load the dataset
try:
    df = pd.read_csv('smartphone_sales.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'smartphone_sales.csv' not found. Please place it in the project folder.")
    exit()

# --- Data Preprocessing ---
print("Cleaning and preprocessing data...")
try:
    # Select only the columns we need
    df = df[features_to_use + [target_column]]
except KeyError:
    print("A column in the CONFIGURATION section was not found in the CSV. Please ensure they match exactly.")
    exit()

# Drop rows with any missing values
df.dropna(inplace=True)

# Apply one-hot encoding to categorical features
df_processed = pd.get_dummies(df, columns=categorical_features, drop_first=True)

# Separate features (X) and target (y)
y = df_processed[target_column]
X = df_processed.drop(target_column, axis=1)

# Save the column order
model_columns = X.columns
with open('model_columns.pkl', 'wb') as file:
    pickle.dump(model_columns, file)
print(f"Processed feature columns saved to model_columns.pkl")


# --- Model Training ---
pipeline = make_pipeline(
    StandardScaler(),
    Ridge(alpha=1.0, random_state=42)
)

print("Training the Ridge Regression model...")
pipeline.fit(X, y)

# Save the entire pipeline
with open('ridge_model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("\nModel training complete!")
print("Pipeline saved as 'ridge_model.pkl'")