# Customer Churn Prediction - AndesLink S.A.

## Descripción del proyecto
Este proyecto implementa un pipeline de Machine Learning orientado a la predicción de churn (abandono) de clientes en un contexto de telecomunicaciones para la empresa AndesLink Servicios Digitales S.A.

El objetivo consiste en identificar clientes con probabilidad de abandonar el servicio utilizando técnicas de clasificación binaria supervisada. El desarrollo integra las prácticas de MLOps requeridas para el entrenamiento, la serialización, el despliegue local en contenedores y la automatización de pruebas unitarias.

---

## Problema de negocio
La pérdida de clientes representa un problema relevante para empresas de servicios por sus costos asociados de adquisición y retención.

El objetivo del modelo es predecir si un cliente abandonará el servicio (`churn = 1`) o permanecerá activo (`churn = 0`) a partir de variables relacionadas con:
- Antigüedad en meses.
- Facturación y cargos mensuales/totales.
- Comportamiento de uso y consumo de datos.
- Interacciones con soporte técnico y pagos atrasados.
- Productos contratados y características del servicio.

---

## Dataset
El dataset utilizado corresponde a un conjunto sintético de churn ubicado en la ruta:
`data/raw/churn_sintetico.csv`

---

## Segunda Entrega - Despliegue Local con Docker

### Requisitos previos
* Docker Desktop instalado y en ejecución.

### Instrucciones para ejecutar la aplicación
1. Clone el repositorio y sitúese en la raíz del proyecto.
2. Ejecute el siguiente comando en la terminal para compilar las imágenes e iniciar los servicios en simultáneo (FastAPI y Streamlit):
   ```bash
   docker-compose up --build