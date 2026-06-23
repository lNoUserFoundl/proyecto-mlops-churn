from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API funcionando correctamente"}

def test_predict_endpoint():
    payload = {
        "tenure_months": 12,
        "monthly_charge": 59.9,
        "total_charges": 718.8,
        "support_tickets": 2,
        "late_payments": 1,
        "avg_monthly_usage_gb": 120.5,
        "contract_type": "Monthly",
        "payment_method": "Credit Card",
        "internet_service": "Fiber",
        "has_streaming": 1,
        "has_security_pack": 0,
        "num_products": 2,
        "region": "North",
        "customer_age": 35,
        "is_promo": 0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "churn_probability" in response.json()