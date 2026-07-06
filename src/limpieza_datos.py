"""
Funciones de detección y tratamiento de calidad de datos
"""
import pandas as pd
import numpy as np
import re


def detectar_duplicados_exactos(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna las filas que son 100% idénticas en todas las columnas."""
    return df[df.duplicated(keep=False)]


def detectar_ids_duplicados(df: pd.DataFrame, id_col: str = "id_paciente") -> pd.DataFrame:
    """Retorna todas las filas cuyo id se repite (idénticas o no)."""
    return df[df[id_col].duplicated(keep=False)].sort_values(id_col)


def resolver_duplicados_por_id(df: pd.DataFrame, id_col: str = "id_paciente") -> pd.DataFrame:
    """
    Para cada id_paciente duplicado, se queda con la fila más completa
    (menor cantidad de nulos). Si hay empate, se queda con la última
    ocurrencia donde se asume registro más reciente/corregido.

    Justificacion: no hay forma de saber cuál medición es la correcta
    cuando solo cambia un valor numérico como ej: peso, así que se prioriza
    completitud de datos sobre orden de aparicion.
    """
    df = df.copy()
    df["_n_nulos"] = df.isnull().sum(axis=1)
    df = df.sort_values(["_n_nulos"]).drop_duplicates(subset=id_col, keep="first")
    return df.drop(columns="_n_nulos").sort_index()


def corregir_edades_imposibles(df: pd.DataFrame, col: str = "edad_paciente",
                              min_val: float = 0, max_val: float = 120) -> pd.DataFrame:
    """
    Convierte a NaN los valores fuera del rango fisiológico posible de edad humana
    [0, 120]. Se marcan como nulo (no se eliminan las filas) porque el
    resto de la información del paciente (peso, altura, ECG, etiqueta)
    sigue siendo válida y aprovechable.
    """
    df = df.copy()
    mask = (df[col] < min_val) | (df[col] > max_val)
    df.loc[mask, col] = np.nan
    return df


def normalizar_fechas(df: pd.DataFrame, col: str = "fecha_registro") -> pd.DataFrame:
    """
    Normaliza la columna de fechas a formato datetime.
    Maneja automáticamente DD/MM/YYYY y Month DD, YYYY.
    """
    df[col] = pd.to_datetime(df[col], format='mixed', errors='coerce', dayfirst=True)
    
    return df


def imputar_numericas_con_mediana(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Imputa nulos de columnas numéricas con la mediana de la columna."""
    df = df.copy()
    for col in cols:
        mediana = df[col].median()
        df[col] = df[col].fillna(mediana)
    return df


def imputar_categorica_con_moda(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Imputa nulos de una columna categórica con la moda"""
    df = df.copy()
    moda = df[col].mode(dropna=True)[0]
    df[col] = df[col].fillna(moda)
    return df

