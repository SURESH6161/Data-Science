import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib


data = pd.read_csv('student_performance.csv')


pass_names = data['Pass'].unique() 

pass_map = {} 
for i in range(len(pass_names)):
    pass_map[pass_names[i]] = i 
data['Pass_encoded'] = data['Pass'].map(pass_map)


X = data[['Hours_Studied','Attendance','Assignments_Completed','Sleep_Hours']] 
y = data['Pass_encoded']  


model = RandomForestClassifier()
model.fit(X, y)


joblib.dump(model, 'model.pkl')
joblib.dump(pass_map, 'pass_map.pkl')

print('Model and mapping saved successfully.')
