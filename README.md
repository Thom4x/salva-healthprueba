# ECG SalvaHealth

## Descripción

Este proyecto desarrolla un pipeline de preparación de datos, análisis exploratorio y modelado para la clasificación de registros de electrocardiogramas (ECG) en las categorías **Normal** y **Anormal**.

El desarrollo fue realizado como solución a una prueba técnica, siguiendo buenas prácticas de organización del proyecto, calidad de datos, versionamiento y reproducibilidad.

---

## Objetivo

Construir un modelo baseline de clasificación que permita identificar registros de ECG normales y anormales, documentando todo el proceso desde la exploración inicial de los datos hasta la evaluación del modelo.

---

## Estructura del proyecto

```
.
├── data
│   ├── raw-data
│   ├── clean-data
│   ├── model-data
│   └── DATA_VERSIONS.md
│
├── notebooks
│   ├── 01_calidad_datos.ipynb
│   ├── 02_limpieza_datos.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_modelo.ipynb
│   ├── 05_cloud.ipynb
│   └── 06_reingenieria.ipynb
│
├── src
│   ├── limpieza_datos.py
│   └── modeling.py
│
├── README.md
├── SCIENTIFIC_THINKING.md
├── requirements.txt
└── reporte_tecnico.pdf
```

---

## Flujo del proyecto

El proyecto se desarrolló siguiendo las siguientes etapas:

1. Exploración inicial del dataset.
2. Identificación de problemas de calidad.
3. Limpieza y preparación de los datos.
4. Análisis exploratorio de datos (EDA).
5. Entrenamiento y evaluación de un modelo baseline.
6. Consumo remoto desde Azure Blob Storage.
7. Ingeniería de características (propuesta).


---

## Calidad de datos

Durante la exploración se identificaron los siguientes problemas:

- Valores faltantes.
- Registros duplicados por paciente.
- Edades fuera del rango fisiológico.
- Formatos de fecha inconsistentes.
- Variables sin capacidad predictiva.

Cada decisión de limpieza fue documentada y justificada en los notebooks correspondientes.

---

## Modelo desarrollado

Se implementó un modelo baseline utilizando **Regresión Logística**, elegido por su simplicidad, interpretabilidad y facilidad para establecer una línea base de comparación.

Las métricas utilizadas fueron:

- Accuracy
- Precision
- Recall
- F1-score

Adicionalmente, se comparó el desempeño del modelo entrenado con un dataset de preparación mínima frente al dataset completamente limpio.

---

## Versionamiento de datos

Se mantienen tres versiones del conjunto de datos:

- Dataset original (`data/raw-data`)
- Dataset limpio (`data/clean-data`)
- Dataset listo para modelar (`data/model-data`)

La trazabilidad de cada transformación se encuentra documentada en `DATA_VERSIONS.md`.

---

## Consumo desde Azure

Como parte de la prueba técnica, el dataset preparado para modelado fue publicado en **Azure Blob Storage** y consumido mediante lectura remota utilizando `pandas`.

Esto permite desacoplar el análisis del almacenamiento local y representa un flujo de trabajo común en proyectos modernos de datos.

---

## Tecnologías utilizadas

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Azure Blob Storage
- Jupyter Notebook

---

## Herramientas de IA utilizadas

Durante el desarrollo se utilizó **ChatGPT (OpenAI)** como herramienta de apoyo para:

- revisión de decisiones de diseño;
- discusión de estrategias de limpieza de datos;
- mejora de la documentación;
- revisión de código y buenas prácticas.

---

## Variables de entorno

El proyecto utiliza un archivo `.env` para almacenar la configuración del origen remoto de datos.

Ejemplo:

```env
AZURE_BLOB_URL=https://<storage-account>.blob.core.windows.net/<container>/pacientes_model.csv
```

En un entorno productivo este valor podría corresponder a una URL con autenticación mediante SAS Token o gestionarse mediante Azure Key Vault.

## Cómo ejecutar el proyecto

1. Clonar el repositorio.

```bash
git clone <url-del-repositorio>
```

2. Instalar dependencias.

```bash
pip install -r requirements.txt
```

3. Ejecutar los notebooks en orden:

1. calidad_datos.ipynb
2. limpieza_datos.ipynb
3. eda.ipynb
4. modelo.ipynb
5. cloud.ipynb
6. reingenieria.ipynb

---

## Autor

Tomas Holguin Serna
Ingeniero de Software
