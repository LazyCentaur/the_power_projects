
## Datos descargados de:
https://www.kaggle.com/datasets/debasisdotcom/parkinson-disease-detection


## Enlace a Google Sheets

https://docs.google.com/spreadsheets/d/1DiMnvymQDm9oPXcnem6V6pikuHkdCXMMVo1RAPmNbmw/edit?usp=sharing



# Transformación y limpieza de los datos.

Primero eliminé las filas vacías que había al final del archivo y me quedé con **196 registros válidos**. Después creé la tabla de trabajo y revisé la columna name, que funciona como identificador único de cada paciente. Comprobé que no había valores vacíos ni duplicados. A continuación, en el resto de variables numéricas sustituí los puntos por comas para adaptarlos a mi configuración regional y convertí todas las columnas a tipo número, para poder trabajar con ellas en Google Sheets. Finalmente, verifiqué que ninguna columna tuviera valores faltantes, dejando los datos listos y consistentes para el análisis.


# Análisis Descriptivo de los Datos

Este proyecto utiliza un conjunto de datos con **medidas de la voz** de personas **sanas** y pacientes con **Parkinson**.  
La base contiene **195 registros** y **24 variables**, que incluyen tanto características básicas (frecuencia, amplitud, ruido) como medidas más técnicas (**jitter, shimmer, RPDE, DFA, spread1, spread2, D2, PPE**).

## Balance de la muestra
La variable **status** indica si la persona tiene Parkinson (`1`) o es sana (`0`).  
La muestra está **desequilibrada**, con más pacientes con Parkinson que controles sanos.

## Frecuencia Fundamental
Las variables **MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz)** representan el tono de la voz.  
- El promedio de **Fo** es de ~**145 Hz**, con valores entre **80 Hz y 250 Hz**.  
- Los pacientes con Parkinson se concentran más en el rango **120–140 Hz**.

## Variabilidad de la voz
- **Jitter** (variación en frecuencia) y **Shimmer** (variación en amplitud) son más **altos en pacientes con Parkinson**, lo que refleja una voz menos estable.  

## Ruido en la voz
- El **HNR (Relación Armónica-Ruido)** es mayor en personas sanas, indicando voces más limpias.  
- El **NHR** es mayor en pacientes con Parkinson, lo que confirma la mayor presencia de ruido.

## Medidas no lineales
Parámetros como **RPDE, DFA, spread1, spread2, D2, PPE** muestran que las voces de pacientes con Parkinson tienen un patrón más **irregular y caótico** comparado con los controles.

---

### Conclusión
Las características acústicas analizadas permiten **diferenciar entre voces sanas y con Parkinson**, mostrando diferencias claras en:
- **Frecuencia fundamental**  
- **Estabilidad de la voz (jitter y shimmer)**  
- **Proporción de armónicos frente al ruido (HNR/NHR)**  

Esto convierte al dataset en un buen punto de partida para análisis exploratorios y modelos de clasificación.

# Informe explicativo del análisis

Para este trabajo analicé un conjunto de datos con medidas de la voz de pacientes sanos y con Parkinson. El objetivo fue explorar las variables disponibles y comprobar si existen diferencias claras entre ambos grupos.

Empecé con un análisis descriptivo, revisando la proporción de pacientes en cada grupo, la distribución de la frecuencia fundamental de la voz y el comportamiento de medidas relacionadas con la estabilidad y el ruido (jitter, shimmer, HNR, NHR). Este primer paso me permitió entender la estructura de los datos y confirmar que los pacientes con Parkinson muestran valores más inestables y con mayor presencia de ruido en la voz.

Después preparé varios gráficos y dashboards en Google Sheets para visualizar los patrones encontrados:

Un gráfico circular para mostrar la proporción de pacientes sanos frente a los que tienen Parkinson.

Histogramas para observar la distribución de la frecuencia fundamental de la voz tanto a nivel global como separando por estado.

Gráficos de barras para comparar métricas de jitter y shimmer entre grupos.

Diagramas de dispersión para analizar la relación entre variables clave (como frecuencia fundamental y HNR).

Gráficos de líneas de tendencia que muestran cómo cambian los valores medios de HNR y NHR entre sanos y pacientes con Parkinson.

Con estas visualizaciones comprobé de forma clara que las diferencias entre los dos grupos son consistentes: los pacientes con Parkinson tienden a tener menor HNR, mayor NHR y valores más altos de jitter y shimmer, lo que refleja una voz más ruidosa e inestable.