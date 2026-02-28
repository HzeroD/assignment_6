from pydantic import BaseModel
import logging
import pandas as pd
import joblib
import datetime
from fastapi import FastAPI

app = FastAPI()

class CarFeatures(BaseModel):
    Mileage_km: float
    Year: int
    Fuel_Consumption_l: float
    Gears: int
    Power_hp: int
    Engine_Size_cc: int
    Cylinders: int
    Seats: int
    Doors: int
    Previous_Owners: int

try:
    model = joblib.load(r'../../data/random_forest_model.pkl')
except:
    raise ImportError(f"Model was not loaded")

@app.post('/predict')
def predict(features):

    X = pd.DataFrame(features)
    prediction = model(X)

    return prediction

@app.get('/')
def landing():
    return {"message": "Welcome to the Car Price Prediction Application"}
    


