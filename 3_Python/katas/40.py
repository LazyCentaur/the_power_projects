# PROYECTO LÓGICA: Katas de Python: Ejercicio 40

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcula_area(figura, datos):
    """Función que calcula el área de una figura según la opción dada

    Args:
        figura (str): figura dada
        datos (tuple): medidas necesarias en tupla

    Returns:
        float: resultado del área de la figura
    """
        
    if figura not in {"rectangulo", "circulo", "triangulo"}:
        raise ValueError("Opción inválida")
    
    def es_num(x): return isinstance(x, (int, float)) and not isinstance(x, bool)
    
    if figura == "rectangulo":
        if len(datos) != 2 or not all(es_num(x) for x in datos):
            raise TypeError("rectangulo requiere (base, altura) numéricos")
        return round(datos[0] * datos[1], 2)
    elif figura == "circulo":
        if len(datos) != 1 or not es_num(datos[0]):
            raise TypeError("circulo requiere (radio,) numérico")
        return round(math.pi * (datos[0] ** 2), 2)
    elif figura == "triangulo": 
        if len(datos) != 2 or not all(es_num(x) for x in datos):
            raise TypeError("triangulo requiere (base, altura) numéricos")
        return round(datos[0] * datos[1] / 2, 2)
    else:
        raise ValueError("Opción inválida")
        
print(calcula_area("rectangulo", (7.4, 4)))
print(calcula_area("circulo", (8.2, )))
print(calcula_area("triangulo", (2.34, 5.1)))
print(calcula_area("triangulo", (2.34, "Hola")))