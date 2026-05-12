import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def load_data(path):
    return pd.read_csv(path)


def split_features_target(df, target_column="churn"):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y


def build_preprocessor(X):

    categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

    numerical_features = X.select_dtypes(exclude=["object"]).columns.tolist()

    numeric_transformer = Pipeline(
        steps=[
            ("scaler", StandardScaler())
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numerical_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )

    return preprocessor


def split_data(X, y, test_size=0.2, random_state=42):

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )
