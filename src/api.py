from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

model = joblib.load("models/churn_model.pkl")

app = FastAPI(
    title="Churn Prediction API",
    description="API para predicción de abandono de clientes",
    version="1.0"
)


class CustomerData(BaseModel):
    tenure_months: int
    monthly_charge: float
    total_charges: float
    support_tickets: int
    late_payments: int
    avg_monthly_usage_gb: float
    contract_type: str
    payment_method: str
    internet_service: str
    has_streaming: int
    has_security_pack: int
    num_products: int
    region: str
    customer_age: int
    is_promo: int
    


@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}


@app.post("/predict")
def predict(data: CustomerData):
    df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "churn_probability": float(probability)
    }