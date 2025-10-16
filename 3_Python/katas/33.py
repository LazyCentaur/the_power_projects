# PROYECTO LÓGICA: Katas de Python: Ejercicio 33

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [12, -5, 0, 33, -18, 7, 21, -2, 45, 8, 90, 54]

# suma las listas hasta la lista más corta
suma_listas = lambda lista1, lista2: [a + b for a, b in zip(lista1, lista2)]

print(suma_listas(lista1, lista2))