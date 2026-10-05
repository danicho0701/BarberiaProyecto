# Práctica 2 - Análisis estadístico

## Caso
Análisis del tiempo de atención de clientes en barbería.

## Descripción
En esta práctica yo analize  el tiempo de atención de 30 clientes de una barbería mediante estadística descriptiva y Z-Score.

## Variable principal
Aqui es el tiempo de atención de cada cliente, medido en minutos.

## Datos
Los datos se encuentran en:

datos/datos.csv

## Análisis
El análisis estadístico se realiza mediante el siguiente script:

scripts/analisis.py

El programa calcula:
- Cantidad de datos
- Media
- Mediana
- Mínimo
- Máximo
- Rango
- Varianza
- Desviación estándar
- Z-Score
- Valores atípicos

## Resultados principales
Se analizaron 30 datos.

La media fue de 39.93 minutos y la mediana de 38.5 minutos.

Se detectó un valor atípico correspondiente al cliente 30, con un tiempo de atención de 100 minutos y un Z-Score de 4.80.

## Informe
El informe completo se encuentra en:

reporte/informe.txt

## Ejecución

Para ejecutar el análisis se utiliza Python con las librerías pandas y numpy.

Comando:

python scripts/analisis.py