# PROYECTO LÓGICA: Katas de Python: Ejercicio 7

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

lista_numeros = [1, 5, 26, 58, 10]
lista_de_tuplas = [
    (1, "uno"),
    (2, "dos"),
    (3, "tres"),
    (4, "cuatro"),
    (5, "cinco")
] 

lista_de_strings = list(map(lambda tupla: str(tupla), lista_de_tuplas))

print(lista_de_strings)