from flask import Flask, jsonify, request, render_template
from model import model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    
    if request.method == 'GET':
        return jsonify({
            "message": "Use POST method with JSON body to get at prediction",
            "example": {
                "features": [4.9, 5.1, 0.2, 1.4]
            }
        })
        
    elif request.method == 'POST':
            if request.is_json:  # Handles json requests
                data = request.get_json()
                features = data.get("features", [])
            else:  # Handles browser form submissions
                features = [float(v) for v in request.form.values()]

            try:
                prediction, probability = model.predict(features)
                # If request was from form, show in browser
                if not request.is_json:
                    return render_template('index.html', prediction_text=f'Prediction: {prediction}, Confidence: {probability:.2f}')
                # If request was API, return JSON
                return jsonify({"prediction": prediction, "probability": probability})
            except Exception as e:
                return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)