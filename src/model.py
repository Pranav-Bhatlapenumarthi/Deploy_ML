import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('../f1_dnf.csv')
print(data.head())

print(data.columns)

print(data.count())
print(data['target_finish'].value_counts()[0])

null_columns = data.isnull().any()
print(null_columns)


