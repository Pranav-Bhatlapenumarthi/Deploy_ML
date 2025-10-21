# Deploy_ML
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Render](https://img.shields.io/badge/Deployed%20on-Render-brightgreen)

A web-based Machine Learning API built with Flask that serves real-time predictions from a trained model. The API is containerized with Docker and deployed on [Render](https://render.com), making it accessible for integration with frontend applications or other services.

---

## Features

- **Serve ML predictions:** Host a trained model and provide predictions via a RESTful API.  
- **JSON-based endpoints:** Accepts feature inputs in JSON format.  
- **Error handling:** Returns informative error messages for invalid requests.  
- **CORS enabled:** Supports frontend integration from other domains.  
- **Dockerized:** Ensures environment consistency and easy deployment.  

---
## Project Structure

```
Deploy_ML/
│
├── app/
│   ├── main.py         # Flask application
│   ├── model.py        # Model loading and prediction
│
├── models/
│   └── model.joblib    # Trained ML model
│
├── src/
│   └── main_model.py   # Script for data preprocessing and model training
|
├── f1_dnf.csv          # Dataset to train the model
├── test.py             # Mini-test script for predictions
├── requirements.txt    # Required libraries 
├── Dockerfile
└── README.md
```

---

## Installation (Local)

### 1. Clone the repository:
```
git clone https://github.com/Pranav-Bhatlapenumarthi/Deploy_ML.git
cd Deploy_ML
```
### 2. Create a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies:
```
pip install -r requirements.txt
```
### 4. Run the app:
```
python app/main.py
```

## Docker

### 1. Build the Docker image:
``` docker build -t ml-flask . ```

### 2. Run the Docker container:
``` docker run -p 8000:8000 ml-flask ```

---


## Endpoints

### 1. Home (GET /)

**Response:**
```json
{
  "message": "Flask ML API is running"
}

```

### 2. Predict (POST /predict)

**Request:**
```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

**Response:**
```json
{
  "prediction": 0,
  "probability": 0.7
}
```
---
