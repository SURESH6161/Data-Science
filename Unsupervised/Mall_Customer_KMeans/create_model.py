# create_model.py

import pandas as pd
from sklearn.cluster import KMeans
import pickle

# Load the dataset
try:
    dataset = pd.read_csv('Mall_Customers.csv')
except FileNotFoundError:
    print("Error: 'Mall_Customers.csv' not found. Please place the dataset in the project folder.")
    exit()

# Select the features for clustering: Annual Income and Spending Score
X = dataset.iloc[:, [3, 4]].values

# Initialize and train the K-Means model with 5 clusters
# Using parameters from your notebook for consistency (init='k-means++', random_state=42)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
kmeans.fit(X)

# The fitted `kmeans` object (which contains the cluster centers) is saved.
# The .predict() method will find the nearest center for new data.
with open('kmeans_model.pkl', 'wb') as file:
    pickle.dump(kmeans, file)

print("K-Means model trained and saved as kmeans_model.pkl")