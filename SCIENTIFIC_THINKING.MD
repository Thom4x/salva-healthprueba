# Pensamiento científico

## Pregunta

**Si tuvieras dos días adicionales para mejorar este modelo, ¿qué hipótesis probarías primero y por qué?**

---

## Hipótesis 1 — Evaluar modelos no lineales

El modelo baseline desarrollado utiliza Regresión Logística, un algoritmo sencillo e interpretable que permite establecer una línea base de desempeño.

Como siguiente paso, evaluaría modelos como **Random Forest** o **XGBoost**, ya que pueden capturar relaciones no lineales entre las variables clínicas y la etiqueta objetivo.

La hipótesis es que estos modelos podrían mejorar el poder predictivo sin requerir cambios importantes en el conjunto de datos.

---

## Hipótesis 2 — Incorporar nuevas características

Durante el desarrollo se identificaron varias variables derivadas con potencial para mejorar el modelo:

- Índice de Masa Corporal (IMC).
- Grupo de edad.
- Categorías de frecuencia cardíaca.

Estas características podrían aportar información clínica adicional que actualmente no está representada de forma explícita.

---

## Hipótesis 3 — Optimización del proceso de entrenamiento

Con mayor tiempo también realizaría una búsqueda sistemática de hiperparámetros utilizando validación cruzada para comparar distintos modelos bajo las mismas condiciones experimentales.

Esto permitiría obtener una estimación más robusta del desempeño y reducir la dependencia de una única partición entrenamiento-prueba.

---

## Conclusión

Si dispusiera de dos días adicionales, priorizaría la incorporación de nuevas variables derivadas y la evaluación de modelos no lineales antes de intentar optimizar el modelo actual.

Considero que el principal potencial de mejora no se encuentra en modificar el algoritmo, sino en enriquecer la información disponible para el proceso de aprendizaje, especialmente mediante características obtenidas directamente de la señal ECG.