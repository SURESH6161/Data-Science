# create_model.py

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pickle

print("Starting model training process...")

# Load the dataset
try:
    df = pd.read_csv('loan_default_prediction_dataset.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'loan_default_prediction_dataset.csv' not found. Please place it in the project folder.")
    exit()

# --- Data Preprocessing ---
# Identify categorical and numerical features
categorical_features = df.select_dtypes(include=['object']).columns
numerical_features = df.select_dtypes(include=['number']).columns

# Assume the last column is the target
target_column = numerical_features[-1]
numerical_features = numerical_features[:-1] # Remove target from numerical features

print(f"Identified Target Column: {target_column}")
print(f"Identified Categorical Features: {list(categorical_features)}")
print(f"Identified Numerical Features: {list(numerical_features)}")

# Apply one-hot encoding to categorical features
df_processed = pd.get_dummies(df, columns=categorical_features, drop_first=True)

# Separate features (X) and target (y)
y = df_processed[target_column]
X = df_processed.drop(target_column, axis=1)

# Save the column order after one-hot encoding
model_columns = X.columns
with open('model_columns.pkl', 'wb') as file:
    pickle.dump(model_columns, file)

print("Processed feature columns saved to model_columns.pkl")


# --- Model Training ---
# Create a pipeline that first scales the data, then trains the Gradient Boosting classifier.
pipeline = make_pipeline(
    StandardScaler(),
    GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
)

print("Training the Gradient Boosting model... This may take a moment.")
pipeline.fit(X, y)

# Save the entire pipeline (scaler + model) to a file
with open('loan_default_gb_model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("\nModel training complete!")
print("Pipeline saved as 'loan_default_gb_model.pkl'")