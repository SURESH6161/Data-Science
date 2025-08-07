# create_model.py

import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pickle

print("Starting model training process...")

# Define the filename
filename = 'Year-Mileagein1000s-EngineSizeL-Horsepower-NumberofDoors-FuelType0Gas1Diesel-Price.csv'

# Load the dataset
try:
    df = pd.read_csv(filename)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: '{filename}' not found. Please place it in the project folder.")
    exit()

# --- Data Preprocessing ---
# Drop rows with any missing values for simplicity
df.dropna(inplace=True)

# Assume the last column is the target variable (Price) and the rest are features
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

print(f"Using '{df.columns[-1]}' as the target and the other {len(X.columns)} columns as features.")


# --- Model Training ---
# Create a pipeline that first scales the data, then trains the ElasticNet model.
pipeline = make_pipeline(
    StandardScaler(),
    ElasticNet(alpha=1.0, l1_ratio=0.5, random_state=42)
)

print("Training the Elastic Net Regression model...")
pipeline.fit(X, y)

# Save the entire pipeline (scaler + model) to a file
with open('elasticnet_car_price_model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("\nModel training complete!")
print("Pipeline saved as 'elasticnet_car_price_model.pkl'")