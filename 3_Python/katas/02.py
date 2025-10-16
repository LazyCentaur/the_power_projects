
# PROYECTO LÓGICA: Katas de Python: Ejercicio 2

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
# Usa la función map()

lista_numeros = [1, 5, 26, 58, 10]

# Aplicamos la función numero*2 a cada elemento de la lista
lista_doble_valor = list(map(lambda numero: numero*2, lista_numeros))

print(lista_doble_valor)