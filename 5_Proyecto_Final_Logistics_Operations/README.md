# Logistics Operations Database Analysis 📊

## Descripción del Proyecto

Este proyecto consiste en el análisis de una base de datos operativa de una empresa ficticia de transporte (clase 8) que abarca tres años de actividad. El objetivo principal es transformar datos brutos en información valiosa para la toma de decisiones estratégicas de cara al cierre de 2024 y la planificación de 2025.

*Los objetivos del cliente son:*

De cara a los beneficios de año 2024, quieren reconocer a ciertos empleados los méritos hechos en la empresa, se han establecido estos tres objetivos:

- *1. Los 10 empleados que más viajes han realizado*
- *2. Los 10 empleados que más beneficios han reportado a la empresa*
- *3. Los 10 empleados que más tiempo han estado en la carretera*

También quieren conocer de cara al planning del 2025:

- *4. Qué rutas aportan mayores beneficios*
- *5. Qué camiones tienen un mantenimiento más costoso*
- *6. Qué perfil de cliente tiene la empresa. Tipos de contrato, cargas que contratan, etc*
- *7. Qué cliente es el que más abandona la empresa*

El dataset incluye más de 85,000 registros con información sobre conductores, viajes, mantenimiento, combustible y eventos de entrega.

## Estructura del Proyecto

El proyecto está dividido en:
-  6 archivos notebook de python:
   1. Transformación y limpieza profunda de los datos.
   2. Análisis descriptivo y estadístico de los datos.
   3. Respuestas a los requerimientos del cliente.
   4. Análisis exhaustivo del df principal.
   5. Clustering para buscar grupos en los viajes .
   6. Búsqueda de patrones de temporaridad.
- Dashboard operativo en Power BI, con gráficos interactivos
- Informe explicativo del análisis en Presentaciones de Google

Carpetas en el repositorio:
├──  datos_en_bruto (archivos csv en bruto)
├──  datos_transformados (archivos csv una vez limpios y trabsformados)
├──  notebooks (archivos notebook)
├──  notebooks/csv_clustering (csv para el cluestering)
├──  README.md  

## Instalación y Requisitos

Este proyecto utiliza Python 3.10.18 en un entorno virtual.

Bibliotecas utilizadas:
- numpy
- pandas
- math
- matplotlib
- seaborn
- plotly

## Acerca de este conjunto de datos

**url: https://www.kaggle.com/datasets/yogape/logistics-operations-database**

Una base de datos operativa completa de una empresa ficticia de transporte por carretera de clase 8 que abarca tres años. No se trata de datos extraídos de la web ni de contenido simplificado de tutoriales, sino de una simulación realista basada en 12 años de experiencia logística en el mundo real, diseñada específicamente para analistas que se están pasando a los ámbitos de la cadena de suministro y el transporte.

El conjunto de datos contiene más de 85 000 registros en 14 tablas interconectadas que abarcan todo, desde las asignaciones de conductores y las compras de combustible hasta los programas de mantenimiento y el rendimiento de las entregas. Cada tabla mantiene las relaciones de claves externas adecuadas, lo que la hace ideal para practicar consultas SQL complejas, crear canalizaciones de datos o desarrollar paneles operativos.

### ¿Por qué existe este conjunto de datos?

La mayoría de los conjuntos de datos logísticos son privados (no están disponibles) o excesivamente simplificados (poco realistas). Esto llena el vacío: complejidad operativa sin preocupaciones de confidencialidad. Los datos reflejan patrones reales de la industria:

- Los precios del combustible siguen la tendencia al alza del diésel en 2022 y la caída en 2023-2024.
- La rotación de conductores se sitúa en el 15 % anual (estándar del sector).
- La utilización media del equipo es del 65 % (típica para las operaciones con furgonetas secas).
- El rendimiento en cuanto a entregas puntuales oscila entre el 85 % y el 95 % (niveles de servicio realistas).
- Los intervalos de mantenimiento siguen los programas de mantenimiento preventivo de clase 8.

### Estructura del conjunto de datos

##### Entidades principales (tablas de referencia):

- **Drivers** (150 registros) - Datos demográficos, historial laboral, información sobre el permiso de conducir comercial (CDL).
- **Trucks** (120 registros) - Especificaciones de la flota, fechas de adquisición, estado
- **Trailers** (180 registros) - Tipos de equipos, asignaciones actuales
- **Customers** (200 registros) - Cuentas de remitentes, condiciones contractuales, potencial de ingresos
- **Facilities** (50 registros) - Terminales y almacenes con coordenadas geográficas
- **Routes** (60+ registros) - Pares de ciudades con distancias y estructuras tarifarias

##### Transacciones operativas:

- **Loads** (más de 57 000 registros): detalles del envío, ingresos, tipo de reserva.
- **Trips** (más de 57 000 registros): asignaciones de conductores y camiones, rendimiento real.
- **Fuel Purchases** (más de 131 000 registros): datos a nivel de transacción con precios
- **Maintenance Records** (más de 6500 registros): historial de servicio, costes, tiempo de inactividad
- **Delivery Events** (más de 114 000 registros): marcas de tiempo de recogida/entrega, retenciones
- **Safety Incidents** (114 registros): accidentes, infracciones, reclamaciones

##### Análisis agregados

- **Driver Monthly Metrics** (más de 5400 registros): resúmenes de rendimiento.
- **Truck Utilization Metrics** (más de 3800 registros): eficiencia de los equipos.


LOGISTICS DATABASE SCHEMA
=========================

1. DRIVERS
   - Primary Key: driver_id
   - Contains: Driver demographics, employment history, license info
   
2. TRUCKS
   - Primary Key: truck_id
   - Contains: Fleet equipment details, acquisition info, status
   
3. TRAILERS
   - Primary Key: trailer_id
   - Contains: Trailer inventory, types, status
   
4. CUSTOMERS
   - Primary Key: customer_id
   - Contains: Customer accounts, contract types, revenue potential
   
5. FACILITIES
   - Primary Key: facility_id
   - Contains: Terminal and warehouse locations, capacity
   
6. ROUTES
   - Primary Key: route_id
   - Contains: Origin-destination pairs, distances, rate structures
   
7. LOADS
   - Primary Key: load_id
   - Foreign Keys: customer_id, route_id
   - Contains: Shipment details, revenue, booking type
   
8. TRIPS
   - Primary Key: trip_id
   - Foreign Keys: load_id, driver_id, truck_id, trailer_id
   - Contains: Actual trip performance, fuel consumption, duration
   
9. FUEL_PURCHASES
   - Primary Key: fuel_purchase_id
   - Foreign Keys: trip_id, truck_id, driver_id
   - Contains: Fuel transactions, prices, locations
   
10. MAINTENANCE_RECORDS
    - Primary Key: maintenance_id
    - Foreign Keys: truck_id
    - Contains: Service history, costs, downtime
    
11. DELIVERY_EVENTS
    - Primary Key: event_id
    - Foreign Keys: load_id, trip_id, facility_id
    - Contains: Pickup/delivery timestamps, detention, on-time status
    
12. SAFETY_INCIDENTS
    - Primary Key: incident_id
    - Foreign Keys: trip_id, truck_id, driver_id
    - Contains: Accidents, violations, damage costs
    
13. DRIVER_MONTHLY_METRICS (Aggregated)
    - Composite Key: driver_id, month
    - Contains: Monthly performance summaries per driver
    
14. TRUCK_UTILIZATION_METRICS (Aggregated)
    - Composite Key: truck_id, month
    - Contains: Monthly equipment utilization summaries