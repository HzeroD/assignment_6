import pydantic
import joblib
import dill
import pandas as pd
from fastapi import FastAPI
import numpy as np

app = FastAPI()

# '{"SeniorCitizen": 0,
#  "tenure": 9,
#  "MonthlyCharges": 55.60,
#  "TotalCharges": 1000,
#  "MultipleLines": "Yes",
#  "InternetService": "Yes",
#  "OnlineSecurity": "Yes",
#  "OnlineBackup": "No",
#  "DeviceProtection": "Yes",
#  "TechSupport": "No",
#  "StreamingTV": "No",
#  "StreamingMovies": "Yes",
#  "Contract": "One year"
#  "PaymentMethod": "Mailed check"}'

class ChurnFeatures(pydantic.BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    gender: str
    Partner: str
    Dependents: str
    PhoneService: str
    MultipleLines: object
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str


model = joblib.load('./data/rfc_best_model.pkl')
ohe = 0

with open('./data/encoder_ohe.pkl', 'rb') as encoder:
    ohe = dill.load(encoder)




@app.get("/")
def home():
    return {"WELCOME TO OUR CHURN PREDICTION APPLICATION ENDPOINT"}

@app.get("/health")
def health_check():
    return {"200 OK"}


@app.post('/predict')
def predict(features: ChurnFeatures):
    print("Checking entry")
    
    df = pd.DataFrame([features.model_dump()])

    df_object = df.select_dtypes(include='object')
    
    object_features = df_object.columns.tolist()
    df_num = df.select_dtypes(include='number')
    
    encoded_arr = ohe.transform(df_object).toarray()
 
    df_encoded = pd.DataFrame(encoded_arr, columns=[f"{col}" for col in ohe.get_feature_names_out()])
    print(df_encoded.iloc[:, 18:24])
    
    prediction = model.predict(pd.concat([df_num, df_encoded], axis=1))
    proba = model.predict_proba(pd.concat([df_num, df_encoded], axis=1))
    
    return {f"Prediction: {prediction}  Probability: {proba}"}



@app.post('/predict_batch')
def predict_batch(batch: list[ChurnFeatures]):
    predictions = []

    for item in batch:
        df = pd.DataFrame([item.model_dump()])

        df_object = df.select_dtypes(include='object')
        df_num = df.select_dtypes(include='number')

        encoded_arr = ohe.transform(df_object).toarray()

        df_encoded = pd.DataFrame(encoded_arr, columns=[col for col in ohe.get_feature_names_out()])

        X = pd.concat([df_num, df_encoded], axis=1)
        prediction = model.predict(X)
        proba = model.predict_proba(X)[0][0] if prediction == "No" else model.predict_proba(X)[0][1]

        predictions.append([prediction[0], proba])
    
    return predictions





