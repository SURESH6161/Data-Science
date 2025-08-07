# create_classifier_model.py

import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
import pickle

print("Starting model creation process...")

# Load the dataset
try:
    df = pd.read_csv('Fresh-Milk-Grocery-Frozen-DetergentsPaper-Delicassen (1).csv')
    # Assuming the first two columns 'Channel' and 'Region' are not part of the spending features
    # If they are meant to be features, this line should be adjusted.
    X = df.drop(['Channel', 'Region'], axis=1)
    print("Dataset loaded and prepared successfully.")
except FileNotFoundError:
    print("Error: 'Fresh-Milk-Grocery-Frozen-DetergentsPaper-Delicassen (1).csv' not found.")
    exit()
except KeyError:
    print("Warning: 'Channel' or 'Region' columns not found. Using all columns as features.")
    X = df

# --- Step 1: Scale the data and apply DBSCAN to get cluster labels ---
print("Scaling data and running DBSCAN to find clusters...")
# Scaling is crucial for distance-based algorithms like DBSCAN
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# DBSCAN parameters - these may need tuning for different datasets
# eps is the max distance between two samples for one to be considered as in the neighborhood of the other
# min_samples is the number of samples in a neighborhood for a point to be considered as a core point
dbscan = DBSCAN(eps=1.5, min_samples=5)
cluster_labels = dbscan.fit_predict(X_scaled)
df['cluster'] = cluster_labels

print(f"DBSCAN found {len(set(cluster_labels)) - 1} clusters and an outlier group.")
print(f"Cluster distribution:\n{df['cluster'].value_counts()}")

# --- Step 2: Train a classifier on the generated cluster labels ---
# This classifier will predict the cluster for new data points.
# We use the original (unscaled) X data to train the final pipeline.
print("Training a K-Nearest Neighbors classifier on the DBSCAN clusters...")

final_pipeline = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

# Train the pipeline on the original features and the DBSCAN-generated labels
final_pipeline.fit(X, cluster_labels)

# --- Step 3: Save the trained classifier pipeline ---
with open('customer_dbscan_model.pkl', 'wb') as file:
    pickle.dump(final_pipeline, file)

print("\nClassifier pipeline trained and saved as 'customer_dbscan_model.pkl'")