# PROYECTO LÓGICA: Katas de Python: Ejercicio 19

# 19. Crea una función lambda que filtre los números impares de una lista dada.

lista_numeros = [34, 72, 5, 89, 16, 47, 23, 90, 11, 58, 3, 76, 29, 64, 51, 8, 95, 12, 
                 37, 68, 2, 84, 19, 43, 70, 27, 60, 14, 99, 6, 32, 78, 21, 56, 9, 88, 
                 40, 13, 65, 31, 74, 18, 52, 7, 83, 26, 61, 10, 96, 45]

numeros_impares = list(filter(lambda x: x%2 == 1, lista_numeros))

print(numeros_impares)