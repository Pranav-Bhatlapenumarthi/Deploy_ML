import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('../f1_dnf.csv')
print(data.head())

print(data.columns)

print(data.count())
print(data['target_finish'].value_counts()[0])

null_columns = data.isnull().any()
print(null_columns)
print(null_columns.value_counts())

# Convert date columns: 'dob' (date of birth) and 'date' (race date) into datetime objects
data['dob'] = pd.to_datetime(data['dob'], errors='coerce')
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Convert other string representations into numeric or timedelta where appropriate
data['milliseconds'] = pd.to_numeric(data['milliseconds'], errors='coerce')
data['fastestLap'] = pd.to_numeric(data['fastestLap'], errors='coerce')
data['fastestLapSpeed'] = pd.to_numeric(data['fastestLapSpeed'], errors='coerce')

# Convert fastestLapTime to a timedelta; note that incorrect formats will be set as NaT
data['fastestLapTime'] = pd.to_timedelta(data['fastestLapTime'], errors='coerce')

# Display information about the dataframe to verify changes
# data.info()

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



