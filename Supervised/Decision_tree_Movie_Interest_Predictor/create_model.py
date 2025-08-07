# create_model.py

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load the dataset
df = pd.read_csv('Movie Interests.csv')

# Prepare the data
X = df[['Age', 'Gender']]
y = df['Interest']

# Initialize and train the Decision Tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the trained model to a file
with open('movie_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as movie_model.pkl")