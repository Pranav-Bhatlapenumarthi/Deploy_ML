# Deploy_ML
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Render](https://img.shields.io/badge/Deployed%20on-Render-brightgreen)

A web-based Machine Learning API built with Flask that serves real-time predictions from a trained model. The API is containerised with Docker and deployed on [Render](https://render.com), making it accessible for integration with frontend applications or other services.

For a step-by-step description of the application, check out this hands-on demonstration: https://medium.com/@hello.gradientthoughts/building-and-hosting-a-machine-learning-model-with-flask-and-docker-1cd4f89cf256

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
### 2. Install dependencies:
```
pip install -r requirements.txt
```
### 3. Run the app:
```
python app/main.py
```

## Docker

### 1. Build the Docker image:
``` docker build -t ml-flask . ```

### 2. Run the Docker container:
``` docker run -p 8000:8000 ml-flask ```

---
