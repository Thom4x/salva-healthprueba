"""
Funciones de preparación y evaluación para el modelado.
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

def preparar_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina columnas que no aportan información al modelo.
    """
    return df.drop(
        columns=[
            "id_paciente",
            "fecha_registro",
            "frecuencia_muestreo_hz",
            "derivacion_ecg"
        ]
    )

def codificar_variables(df: pd.DataFrame, columnas: list = None) -> tuple[pd.DataFrame, dict]:
    """
    Codifica las variables categóricas mediante LabelEncoder.

    Retorna el DataFrame transformado y los codificadores utilizados.
    """
    df = df.copy()
    encoders = {}

    if columnas is None:
        columnas = ["sexo", "etiqueta"]

    for col in columnas:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])
        encoders[col] = encoder

    return df, encoders


def separar_xy(
    df: pd.DataFrame,
    target: str = "etiqueta"
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Separa variables predictoras y variable objetivo.
    """
    X = df.drop(columns=[target])
    y = df[target]

    return X, y


def dividir_dataset(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 42
):
    """
    Divide el conjunto de datos en entrenamiento y prueba,
    preservando la distribución de la variable objetivo.
    """
    return train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state
    )


def evaluar_modelo(y_true, y_pred) -> dict:
    """
    Calcula las métricas principales de clasificación.
    """
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred)
    }