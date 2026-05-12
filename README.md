# Customer Churn Prediction

## Descripción del proyecto

Este proyecto implementa un pipeline básico de Machine Learning orientado a la predicción de churn de clientes en un contexto de telecomunicaciones.

El objetivo consiste en identificar clientes con probabilidad de abandonar el servicio utilizando técnicas de clasificación binaria supervisada.

El proyecto fue desarrollado como parte de una primera entrega orientada a entrenamiento, reproducibilidad y serialización de modelos dentro de un flujo MLOps inicial.

---

# Problema de negocio

La pérdida de clientes (customer churn) representa un problema relevante para empresas de servicios por sus costos asociados de adquisición y retención.

El objetivo del modelo es predecir si un cliente abandonará el servicio (`churn = 1`) o permanecerá activo (`churn = 0`) a partir de variables relacionadas con:
- antigüedad,
- facturación,
- comportamiento de uso,
- soporte técnico,
- productos contratados,
- características del servicio.

---

# Dataset

El dataset utilizado corresponde a un conjunto sintético de churn ubicado en:

```text
data/raw/churn_sintetico.csv
