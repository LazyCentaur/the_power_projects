# PROYECTO LÓGICA: Katas de Python: Ejercicio 15

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

numeros = [34, -12, 57, 0, -89, 23, -5, 76, -41, 8, -22, 91, -64, 13, -7, 45, -33, 2, -58, 70]

resultado = list(map(lambda x: x + 3, numeros))

print(resultado) 