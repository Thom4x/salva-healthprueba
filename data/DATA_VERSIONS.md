# Versionado de datos

Este documento describe la evolución del conjunto de datos durante el desarrollo del proyecto.

---

## Versión 1 - Dataset original

**Ubicación**

```
data/raw/pacientes.csv
```

Corresponde al conjunto de datos entregado para la prueba técnica sin ningún tipo de modificación.

Características:

- Contiene registros duplicados.
- Presenta valores faltantes.
- Incluye edades fuera del rango fisiológico.
- Mantiene formatos originales de fecha.
- Conserva todas las variables originales.

---

## Versión 2 - Dataset limpio

**Ubicación**

```
data/clean-data/pacientes_clean.csv
```

Corresponde al conjunto de datos después de aplicar las decisiones de calidad documentadas.

Transformaciones realizadas:

- Eliminación de registros duplicados por paciente.
- Corrección de edades fuera del rango fisiológico.
- Imputación de valores faltantes.
- Normalización del formato de fechas.
- Validación de tipos de datos.

Este dataset fue utilizado durante el análisis exploratorio (EDA).

---

## Versión 3 - Dataset listo para modelar

**Ubicación**

```
data/model-data/pacientes_model.csv
```

Corresponde al conjunto de datos preparado para el entrenamiento del modelo.

Transformaciones adicionales:

- Eliminación de variables sin capacidad predictiva:
  - id_paciente
  - fecha_registro
  - frecuencia_muestreo_hz
  - derivacion_ecg

Las variables categóricas permanecen en su representación original. La codificación mediante LabelEncoder se realiza únicamente durante el pipeline de entrenamiento para mantener este dataset reutilizable e independiente del algoritmo utilizado.