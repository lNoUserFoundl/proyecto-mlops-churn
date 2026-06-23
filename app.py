import streamlit as st
import requests

st.title("Customer Churn Prediction")

st.write("Ingrese los datos del cliente para obtener una predicción.")

payload = {
    "tenure_months": st.number_input("Tenure (meses)", min_value=0, value=12),
    "monthly_charge": st.number_input("Cargo mensual", value=59.9),
    "total_charges": st.number_input("Cargo total", value=718.8),
    "support_tickets": st.number_input("Tickets de soporte", min_value=0, value=2),
    "late_payments": st.number_input("Pagos atrasados", min_value=0, value=1),
    "avg_monthly_usage_gb": st.number_input("Uso promedio (GB)", value=120.5),
    "contract_type": st.text_input("Tipo de contrato", value="Monthly"),
    "payment_method": st.text_input("Método de pago", value="Credit Card"),
    "internet_service": st.text_input("Servicio de internet", value="Fiber"),
    "has_streaming": st.number_input("Streaming (0/1)", min_value=0, max_value=1, value=1),
    "has_security_pack": st.number_input("Security Pack (0/1)", min_value=0, max_value=1, value=0),
    "num_products": st.number_input("Cantidad de productos", min_value=1, value=2),
    "region": st.text_input("Región", value="North"),
    "customer_age": st.number_input("Edad", min_value=18, value=35),
    "is_promo": st.number_input("Promoción (0/1)", min_value=0, max_value=1, value=0),
}

if st.button("Predecir"):
    response = requests.post(
        "http://churn-api:8000/predict",  # Asegúrate de que diga 'churn-api'
        json=payload,
        timeout=10,
    )

    if response.status_code == 200:
        result = response.json()
        st.success("Predicción realizada correctamente")
        st.write(f"**Predicción:** {result['prediction']}")
        st.write(f"**Probabilidad de churn:** {result['churn_probability']:.2%}")
    else:
        st.error(f"Error en la API: {response.text}")