# create_classifier_model.py

import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Load the dataset
try:
    dataset = pd.read_csv('Mall_Customers.csv')
except FileNotFoundError:
    print("Error: 'Mall_Customers.csv' not found. Please place the dataset in the project folder.")
    exit()

# Select the features for clustering
X = dataset.iloc[:, [3, 4]].values

# --- Step 1: Perform Hierarchical Clustering to create labels ---
# We create 5 clusters as determined in the notebook
hc = AgglomerativeClustering(n_clusters=5, metric='euclidean', linkage='ward')
cluster_labels = hc.fit_predict(X)

# `cluster_labels` is now our target (y) for the supervised model.

# --- Step 2: Train a classifier on the cluster labels ---
# This classifier learns to map features (X) to a cluster label (y)
print("Training a K-Nearest Neighbors classifier...")
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X, cluster_labels)

# --- Step 3: Save the trained classifier model ---
with open('customer_cluster_model.pkl', 'wb') as file:
    pickle.dump(classifier, file)

print("Classifier model trained and saved as customer_cluster_model.pkl")