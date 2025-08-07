# create_model.py

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

print("Starting model training process...")

# Load the dataset
try:
    sms = pd.read_csv('spam.csv', encoding='latin-1')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'spam.csv' not found. Please place the dataset in the project folder.")
    exit()

# --- Data Cleaning ---
# Drop unnecessary columns
if 'Unnamed: 2' in sms.columns:
    sms.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)

# Rename columns for clarity
sms.rename(columns={'v1': 'label', 'v2': 'message'}, inplace=True)

# Map labels to numerical values (0 for ham, 1 for spam)
sms['label'] = sms['label'].map({'ham': 0, 'spam': 1})

print("Data cleaning complete.")

# --- Model Training ---
# Define features (X) and target (y)
X = sms['message']
y = sms['label']

# Create a pipeline that first creates a bag-of-words representation of the text,
# then trains the Naive Bayes classifier.
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the model pipeline on the entire dataset
print("Training the model pipeline...")
pipeline.fit(X, y)

# Save the entire pipeline to a file
with open('spam_model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("\nModel training complete!")
print("Pipeline (Vectorizer + Classifier) saved as 'spam_model.pkl'")