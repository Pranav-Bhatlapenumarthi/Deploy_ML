import numpy as np
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "model.joblib"

class Model:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        print("Model loaded successfully")
        
    def predict(self, features):
        features = np.array(features).reshape(1, -1)
        
        prediction = int(self.model.predict(features)[0])
        probability =  float(max(self.model.predict_proba(features)[0]))
        
        return prediction, probability
    
model = Model()
        