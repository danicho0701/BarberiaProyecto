import pandas as pd
import numpy as np

# Lee los datos
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

datos = pd.read_csv(BASE_DIR / "datos" / "datos.csv", sep=";")

# Variable principal
tiempo = datos["tiempo_atencion_min"]

# los Estadísticoss descriptivos
cantidad = len(tiempo)
media = tiempo.mean()
mediana = tiempo.median()
minimo = tiempo.min()
maximo = tiempo.max()
rango = maximo - minimo
varianza = tiempo.var()
desviacion = tiempo.std()

# Calcular Z-Score
z_score = (tiempo - media) / desviacion

# Detectar valores atípicos
outliers = datos[abs(z_score) > 3].copy()

# Mostrar aqui los resultados
print("======================================")
print("ANÁLISIS DEL TIEMPO DE ATENCIÓN")
print("======================================")

print("\nESTADÍSTICOS DESCRIPTIVOS")
print("Cantidad de datos:", cantidad)
print("Media:", round(media, 2))
print("Mediana:", round(mediana, 2))
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Rango:", round(rango, 2))
print("Varianza:", round(varianza, 2))
print("Desviación estándar:", round(desviacion, 2))

print("\nVALORES ATÍPICOS - Z-SCORE")

if len(outliers) > 0:
    print(outliers[["id_cliente", "tiempo_atencion_min"]])
else:
    print("No se detectaron valores atípicos.")

print("\nZ-SCORES")
for i, z in enumerate(z_score):
    print(
        "Cliente",
        datos.loc[i, "id_cliente"],
        "- Tiempo:",
        datos.loc[i, "tiempo_atencion_min"],
        "- Z-Score:",
        round(z, 2)
    )