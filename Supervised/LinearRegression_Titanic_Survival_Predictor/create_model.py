# create_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression # Changed from LogisticRegression
import pickle
import requests
import io

# URL for the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

def fetch_and_process_data(url):
    print("Downloading dataset...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Dataset downloaded successfully.")
        
        df = pd.read_csv(io.StringIO(response.text))
        
        print("Processing data...")
        df.drop('Cabin', axis=1, inplace=True)
        df.dropna(inplace=True)
        
        sex = pd.get_dummies(df['Sex'], drop_first=True, dtype=int)
        embark = pd.get_dummies(df['Embarked'], drop_first=True, dtype=int)
        
        df.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)
        df = pd.concat([df, sex, embark], axis=1)
        
        print("Data processing complete.")
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading dataset: {e}")
        return None

def train_and_save_model(df):
    if df is None:
        print("Cannot train model due to data fetching issues.")
        return
        
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    
    # Initialize and train the Linear Regression model
    model = LinearRegression() # Changed to LinearRegression
    model.fit(X, y)
    
    # Save the trained model to a new file
    with open('titanic_linear_model.pkl', 'wb') as file:
        pickle.dump(model, file)
        
    print("Linear Regression model trained and saved as titanic_linear_model.pkl")
    print("Model expects the following features in this order:")
    print(X.columns.tolist())

# Main execution
if __name__ == "__main__":
    processed_df = fetch_and_process_data(url)
    train_and_save_model(processed_df)