# Assignment: Dockerized Inference API for Customer Churn

## 🏢 The Scenario
You have just been hired as a Junior Machine Learning Engineer at *StreamConnect*, a telecom provider. The data science team has been exploring why customers are canceling their subscriptions (churning). They have a clean dataset, but they need you to build the bridge between their raw data and the software engineering team. 

Your task is to train a baseline machine learning model, wrap it in a REST API, and containerize the entire application using Docker so the software team can easily deploy it to their servers.

## 🎯 Learning Objectives
By completing this assignment, you will be able to:
1. Serialize and save a trained machine learning model.
2. Build a REST API for model inference using FastAPI (or Flask).
3. Write a `Dockerfile` to containerize a Python application.
4. Document the process for running and testing a Dockerized microservice.

## 📊 The Dataset
**Dataset:** [Telco Customer Churn (Kaggle/IBM)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
* **Target Variable:** `Churn` (Yes/No)
* **Features:** Customer account information (tenure, contract type, payment method, monthly charges) and demographic info.

## 📋 Assignment Requirements

### Part 1: Model Training & Serialization
*Note: The focus of this assignment is on engineering, not model accuracy. But, a Acceptable accuracy is desired*
1. Load the Telco Customer Churn dataset.
2. Perform basic preprocessing (e.g., handle missing values, encode categorical variables like `Contract` and `PaymentMethod`).
3. Train a simple binary classification model (e.g., Logistic Regression, Random Forest, or XGBoost) to predict the `Churn` column.
4. Save the trained model and any necessary preprocessors (like scalers or encoders) to disk using `joblib` or `pickle`.

### Part 2: API Development
1. Create a Python script (`app.py` or `main.py`) using **FastAPI** (recommended) or **Flask**.
2. Load your serialized model and preprocessors when the application starts.
3. Create a `POST /predict` endpoint that accepts a JSON payload containing a single customer's data. 
4. The endpoint should preprocess the incoming JSON data, pass it through the model, and return a JSON response with the prediction.
    * *Example Response:* `{"churn_prediction": "Yes", "probability": 0.82}`

### Part 3: Containerization (Docker)
1. Create a `requirements.txt` file listing all necessary Python packages.
2. Write a `Dockerfile` to containerize your API. Your Dockerfile must:
    * Use an official, lightweight Python base image (e.g., `python:3.9-slim`).
    * Set a working directory.
    * Copy the requirements file and install dependencies.
    * Copy the application code and model artifacts.
    * Expose the port your API runs on (e.g., port 8000).
    * Define the command to run the application server (e.g., using `uvicorn` or `gunicorn`).

### Part 4: Documentation
Write a `README.md` file that includes:
1. A brief description of the project.
2. Step-by-step instructions on how to build the Docker image using the `docker build` command.
3. Instructions on how to run the Docker container locally using `docker run`.
4. A sample `curl` command (or Python `requests` snippet) demonstrating how to send data to the running container and get a prediction.

## 🚀 Stretch Goals (Optional)
If you finish early and want to challenge yourself, try adding:
* **Input Validation:** Use Pydantic models (if using FastAPI) to ensure the incoming JSON payload has the correct data types before passing it to the model.
* **Batch Inference:** Add a `/predict_batch` endpoint that accepts a list of customers and returns predictions for all of them.
* **Health Check:** Add a simple `GET /health` endpoint that returns a `200 OK` status to verify the API is running.

## 📦 What to Submit
Please submit a link to a public GitHub repository containing:
* `train.ipynb` or `train.py` (your training script).
* `app.py` (your API script).
* Your serialized model file(s) (e.g., `model.joblib`).
* `requirements.txt`
* `Dockerfile`
* `README.md`
