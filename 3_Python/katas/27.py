# PROYECTO LÓGICA: Katas de Python: Ejercicio 27

# 27. Crea una función que calcule el promedio de una lista de números.

lista_numeros = [37, -12, 84, 5, -29, 63, 0, 48, -7, 91, 22, -54, 13, 76, -33]

def calcula_promedio(numeros):
    """ Calcula el promedio de los números de una lista"""
    return sum(numeros) / len(numeros) if numeros else 0
    
promedio = calcula_promedio(lista_numeros)

print(promedio)
    
# otra opcion

import statistics as stats

promedio2 = stats.mean(lista_numeros)

print(promedio2)
    