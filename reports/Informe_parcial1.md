###Características principales:

5000 registros
clasificación binaria
variables numéricas y categóricas
variable objetivo: churn

El dataset incluye información relacionada con:

antigüedad del cliente,
facturación,
tickets de soporte,
método de pago,
productos contratados.
3. Análisis exploratorio

Se realizó un análisis exploratorio mediante Jupyter Notebook.

Principales observaciones:

no se detectaron valores faltantes,
existe desbalance moderado de clases,
clientes con menor antigüedad presentan mayor churn,
tickets de soporte y pagos atrasados muestran relación positiva con abandono.
4. Preparación de datos

Se implementó un pipeline de preprocessing utilizando scikit-learn.

Las tareas realizadas fueron:

separación de variables predictoras y target,
codificación de variables categóricas,
escalado de variables numéricas,
división train/test utilizando estratificación.
5. Modelo entrenado

Se entrenó un modelo de clasificación binaria utilizando:

RandomForestClassifier

El pipeline completo fue integrado mediante Pipeline de scikit-learn.

6. Evaluación

Resultados obtenidos:

Métrica	Resultado
Accuracy	0.7090
Precision	0.5953
Recall	0.4500
F1-score	0.5126
ROC-AUC	0.7313

Se utilizaron múltiples métricas debido al desbalance presente en el problema de churn.

7. Serialización y reproducibilidad

El modelo final fue serializado utilizando joblib:

models/churn_model.pkl

También se incorporaron herramientas de reproducibilidad:

Git
DVC
MLflow
environment.yml

Se verificó correctamente la carga del modelo desde un script independiente.

8. Conclusión

Se desarrolló correctamente un pipeline inicial de Machine Learning para predicción de churn incluyendo:

análisis exploratorio,
preprocessing,
entrenamiento,
evaluación,
serialización,
reproducibilidad básica.

El modelo quedó preparado para futuras etapas de despliegue mediante API.###