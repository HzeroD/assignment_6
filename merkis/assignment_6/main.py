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
    SeniorCitizen: int
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaymentMethod: str


model = joblib.load('./data/rfc_best_model.pkl')
encoder_ohe = 0

with open('./data/encoder_ohe.pkl', 'rb') as encoder:
    ohe = dill.load(encoder)




@app.get("/")
def home():
    return {"WELCOME TO OUR CHURN PREDICTION APPLICATION ENDPOINT"}

@app.post('/predict')
def predict(features: ChurnFeatures):
    print("Checking entry")
    
    df = pd.DataFrame([features.model_dump()])

    df_object = df.select_dtypes(include='object')
    print
    object_features = df_object.columns.tolist()
    df_num = df.select_dtypes(include='number')

    encoded_arr = ohe.transform(df_object).toarray()
    temp = ohe.categories_[-1]
    labels = np.array(ohe.categories_[:-1]).ravel()
    # labels = np.array(ohe.categories_).ravel()
    feature_labels = np.concatenate((labels, temp))
    df_encoded = pd.DataFrame(encoded_arr, columns=[f"{col}_encoded" for col in feature_labels])
    print(df_encoded.iloc[:, 18:24])
    prediction = model.predict(pd.concat([df_num, df_encoded], axis=1))
    
    return {f"Prediction: {prediction}"}


