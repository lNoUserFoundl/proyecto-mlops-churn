import os
import joblib
import mlflow
import mlflow.sklearn

from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

from preprocess import (
    load_data,
    split_features_target,
    build_preprocessor,
    split_data
)


DATA_PATH = "data/raw/churn_sintetico.csv"


def main():

    df = load_data(DATA_PATH)

    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    preprocessor = build_preprocessor(X)

    model_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(random_state=42))
        ]
    )

    mlflow.set_experiment("churn_prediction")

    with mlflow.start_run():

        model_pipeline.fit(X_train, y_train)

        y_pred = model_pipeline.predict(X_test)

        y_proba = model_pipeline.predict_proba(X_test)[:, 1]

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_proba)

        print(f"Accuracy: {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1-score: {f1:.4f}")
        print(f"ROC-AUC: {roc_auc:.4f}")

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)
        mlflow.log_metric("roc_auc", roc_auc)

        os.makedirs("models", exist_ok=True)

        joblib.dump(model_pipeline, "models/churn_model.pkl")

        mlflow.sklearn.log_model(
            model_pipeline,
            artifact_path="random_forest_model"
        )

        print("Model saved successfully.")


if __name__ == "__main__":
    main()