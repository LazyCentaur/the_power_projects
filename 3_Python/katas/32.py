# PROYECTO LÓGICA: Katas de Python: Ejercicio 32

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

empleados = [
    {"nombre": "Lucía Hernández Soto", "cargo": "Desarrolladora Backend", "salario": 47000, "fecha_entrada": "2021-03-15", "fecha_salida": None},
    {"nombre": "Carlos Martín López", "cargo": "Ingeniero DevOps", "salario": 52000, "fecha_entrada": "2020-11-02", "fecha_salida": None},
    {"nombre": "Elena Rodríguez Vega", "cargo": "Data Scientist", "salario": 56000, "fecha_entrada": "2019-09-09", "fecha_salida": None},
    {"nombre": "Pablo Gómez Navas", "cargo": "QA Engineer", "salario": 34000, "fecha_entrada": "2022-01-10", "fecha_salida": None},
    {"nombre": "Sergio Ortiz Mena", "cargo": "Product Manager", "salario": 60000, "fecha_entrada": "2020-05-04", "fecha_salida": None},
    {"nombre": "Ana Beltrán Morales", "cargo": "Diseñadora UX/UI", "salario": 41000, "fecha_entrada": "2018-07-23", "fecha_salida": "2022-06-30"},
    {"nombre": "Diego Ruiz Alba", "cargo": "Desarrollador Frontend", "salario": 43000, "fecha_entrada": "2021-08-30", "fecha_salida": None},
    {"nombre": "María Pérez Cano", "cargo": "Analista Financiera", "salario": 37000, "fecha_entrada": "2019-02-18", "fecha_salida": None},
    {"nombre": "Javier López Crespo", "cargo": "Administrador de Sistemas", "salario": 39000, "fecha_entrada": "2018-03-12", "fecha_salida": "2024-09-01"},
    {"nombre": "Clara Santos Rivas", "cargo": "Especialista de Marketing", "salario": 36000, "fecha_entrada": "2022-11-21", "fecha_salida": None},
    {"nombre": "Hugo Ramírez Pardo", "cargo": "Ingeniero de Seguridad", "salario": 58000, "fecha_entrada": "2020-01-27", "fecha_salida": None},
    {"nombre": "Noelia Castillo León", "cargo": "RR. HH. Generalista", "salario": 32000, "fecha_entrada": "2021-05-17", "fecha_salida": None},
    {"nombre": "Tomás Cabrera Gil", "cargo": "Atención al Cliente", "salario": 26000, "fecha_entrada": "2023-04-03", "fecha_salida": None},
    {"nombre": "Aitor Navarro Mesa", "cargo": "Desarrollador Backend", "salario": 45000, "fecha_entrada": "2019-06-10", "fecha_salida": "2023-12-15"},
    {"nombre": "Beatriz Molina Fuentes", "cargo": "CTO", "salario": 85000, "fecha_entrada": "2018-01-15", "fecha_salida": None},
]

def encuentra_empleado(lista_empleados, persona):
    """_summary_

    Args:
        lista_empleados (_type_): _description_
        persona (_type_): _description_

    Returns:
        _type_: _description_
    """
    if not isinstance(lista_empleados, list):
        raise TypeError("lista_empleados debe ser list")
    if not isinstance(persona, str) or not persona.strip():
        raise TypeError("persona debe ser str no vacío")
    
    for empleado in lista_empleados:
        if empleado["nombre"] == persona and empleado["fecha_salida"] is None:
            return f"El cargo del empleado es: {empleado["cargo"]}"
    return "El empleado no trabaja en esta empresa"
    
print(encuentra_empleado(empleados, "Diego Ruiz Alba"))
print(encuentra_empleado(empleados, "Mónica Moreno Sotillo"))
print(encuentra_empleado(empleados, "Beatriz Molina Fuentes"))