import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os


def run_dbscan(csv_path, eps=0.8, min_samples=4):
    # Load dataset
    df = pd.read_csv(csv_path)

    # Features to cluster on
    features = df.columns.tolist()  # Use all columns from your CSV
    X = df[features].values

    # Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Run DBSCAN
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(X_scaled)
    df['Cluster'] = labels

    # Save updated CSV
    output_csv = "clustered_customers.csv"
    df.to_csv(output_csv, index=False)

    # Create PCA plot
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    plt.figure(figsize=(8, 6))

    unique_labels = np.unique(labels)
    for lbl in unique_labels:
        mask = labels == lbl
        if lbl == -1:
            plt.scatter(X_pca[mask, 0], X_pca[mask, 1], label="Noise", marker='x')
        else:
            plt.scatter(X_pca[mask, 0], X_pca[mask, 1], label=f"Cluster {lbl}")

    plt.title("DBSCAN Clusters (PCA Projection)")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.legend()
    plot_path = os.path.join("static", "clusters.png")
    plt.savefig(plot_path, bbox_inches="tight")
    plt.close()

    return df, plot_path
