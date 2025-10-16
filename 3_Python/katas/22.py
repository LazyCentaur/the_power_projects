# PROYECTO LÓGICA: Katas de Python: Ejercicio 22

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce().

from functools import reduce

numeros = [17, -42, 88, 5, -9, 63, 23, -31, -76, 54]

if 0 in numeros:
        print("Hay un 0; el producto total será 0")

def calcula_producto(num1, num2):
    """ Devuelve el producto de dos números"""
    return 0 if num1 == 0 or num2 == 0 else num1 * num2

# El 1 es por si la lista viene vacía
producto = reduce(calcula_producto, numeros, 1)

print(producto)