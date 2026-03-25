## Overview
    The goal of the work in this folder is to build a basic machine learning pipeline that spans from data ingestion, preprocessing and model training to a containerized docker application which gives a prediction based on sent data. The dataset used was the Telco Customer Churn (Kaggle/IBM) data set "https://www.kaggle.com/datasets/blastchar/telco-customer-churn", and the target feature is 'Churn', which is a binary feature with "Yes" and "No" values. 

**The Data**
    Shape: 7043 rows and 20 columns(including 'Churn')
    NA Values: There were no missing values in the dataset
    Column Types: There were 16 categorical features(including 'Churn') and four numeric type features
    Preprocessing: scikit-learn's OneHotEncoder() was used to encode the categorical features

**The Models**
    Four scikit-learn models were used to predict churn rates:
      - LogisticRegressionClassifier()
      - DecisionTreeClassifier()
      - RandomForestClassifier()
      - GradientBoostingClassifier()

    The metric used to evaluate model performance was accuracy using the  ```accuracy_score``` function. The models all scored in between 78% - 83% accuracy, with LogisticRegressionClassifier scoring the highest at 
    81.97%

**Serialization**

    joblib was used to serialize the best performing model, LogisticRegressionClassifier. This model, like the others, was fitted to data preprocessed with OneHotEncoder(), and so the encoder was also serialized using joblib.

    OneHotEncoder() --> ./data/encoder_ohe.pkl
    model --> ./data/best_model.pkl

**The App**

    The application is called 'main.py' in the project folder, and uses the REST API FastAPI. We use joblib to load both the encoder fitted with the training data and the model fitted with the preprocessed training data. The app exposes two endpoints that return churn predictions of sent data: '/predict' and '/predict_batch'. The first receives a single customer datapoint with all features used to fit both model and encoder, and returns the model's prediction whether or not that customer will churn along with the probability of its prediction. The second endpoint takes a list of customer datapoints and returns the same as the previous endpoint for each customer, and does so in a list of lists.

**Docker Container**

    The Docker container used to run our app uses lightweight python base image python:3.13-slim. We install all dependencies used in the project from the pyproject.toml file, and copy main.py, and the serialized objects into the image. The container exposes port 8000 and runs the app using uvicorn

**Docker Instructions**
    Build Dockerfile: docker build -t <image_name> .
        -NOTE: the -t flag allows us to name the image built using the build command
    
    Run Container Locally: docker run -p 8000:8000 <image_name>
        - the -p flag maps a host machine port to the container port:
           docker run -p <host port>:<container port>  <image_name>

    