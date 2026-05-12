import joblib
import pandas as pd

model = joblib.load("models/churn_model.pkl")

sample = pd.read_csv("data/raw/churn_sintetico.csv")

sample = sample.drop(columns=["churn"]).head(5)

predictions = model.predict(sample)

print(predictions)