import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('../f1_dnf.csv')
print(data.head())

print(data.columns) # to view all the features

print(data.count()) # to view number of data points in each feature

 # To count how many cars do not finish the race 
print("\n\nNumber of cars which didn't finish the race:", data['target_finish'].value_counts()[0])

null_columns = data.isnull().any()
print(null_columns) # to check the features with null values

# Predictive Modelling
features = ["grid", "positionOrder", "points", "laps"]

data_model = data.dropna(subset=features + ["target_finish"])
X = data_model[features]
y = data_model["target_finish"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

joblib.dump(classifier, "../models/model.joblib")
print("Model saved successfully!")



