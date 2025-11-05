# Análisis de campaña

## 1. Propósito del proyecto

Este proyecto analiza el comportamiento de los clientes de un banco ante una campaña de marketing telefónico

### Fuentes de datos:
- `bank-additional.csv`: **información de las campañas** (llamadas, contexto macroeconómico, respuesta del cliente, etc.).
- `customer-details.xlsx`: tres hojas de Excel con **datos demográficos y de comportamiento** de los clientes (ingresos, hijos en el hogar, antigüedad, visitas web, etc.).

### El objetivo principal es responder a:

**¿Qué factores influyen más en que un cliente contrate (y = "yes") un producto en una campaña de marketing telefónico?** 

## 2. Estructura del proyecto

# Análisis de campañas de marketing bancario

## 1. Propósito del proyecto

Este proyecto analiza el comportamiento de los clientes de un banco portugués ante distintas **campañas de marketing telefónicas** cuyo objetivo es la contratación de un **depósito a plazo**.

Se utilizan dos fuentes de datos:

- `bank-additional.csv`: información de las campañas (llamadas, contexto macroeconómico, respuesta del cliente, etc.).
- `customer-details.xlsx`: tres hojas de Excel con **datos demográficos y de comportamiento** de los clientes (ingresos, hijos en el hogar, antigüedad, visitas web, etc.).

El objetivo principal es responder a:

> **¿Qué factores influyen más en que un cliente contrate (y = "yes") un producto en una campaña de marketing telefónico?**  

y extraer recomendaciones accionables para el negocio.

---

## 2. Estructura del proyecto

```text
.
├── datos_en_bruto/
│   ├── bank-additional.csv
│   └── customer-details.xlsx
├── datos_transformados/
│   ├── merged.csv / merged.xlsx
│   └── *.png
├── pruebas.ipynb
└── README.md
```

## 3. Requisitos

### 3.1. Software
```
Python 3.9+ (recomendado 3.10)
Gestor de paquetes: pip o conda
```
### 3.2. Librerías principales de Python
```
pandas
numpy
matplotlib
seaborn
openpyxl (para leer Excel)
```
## 4. Principales hallazgos

### Perfil del cliente

Edad media alrededor de 40 años.

Mayoría de clientes entre 29–64 años, población activa.

Profesiones: admin., blue-collar y technician.

Estado civil mayoritariamente married.

### Efectividad de la campaña

Tasa global de respuesta positiva (y = "yes") cercana al 11 %

No hay grandes diferencias por día de mes, pero los jueves presentan una ligera mejora en conversión.

El resultado de campañas previas sí es relevante

Cantidad de llamadas y número de contactos:
- Las campañas con llamadas más largas o con más intentos tienden a generar más respuestas afirmativas.

Variables macroeconómicas: 
- La tasa de variación de empleo, el Euribor y el número promedio de empleados muestran una correlación notable con la respuesta. Los clientes son más propensos a contratar en contextos económicos favorables.

Antigüedad del cliente:
- Los clientes más recientes son algo más receptivos a las campañas, mientras que los más antiguos tienden a no contratar nuevos productos.