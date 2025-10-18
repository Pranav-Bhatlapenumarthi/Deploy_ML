from flask import Flask, jsonify, request
from model import model

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask ML API is runninng"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "Missing 'features' key"}), 400
    
    features = data["features"]
    try:
        prediction, probability = model.predict(features)
        return jsonify({
            "prediction": prediction,
            "probability": probability
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)