# PROYECTO LÓGICA: Katas de Python: Ejercicio 4

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. 
# Usa la función map()

lista_numeros = [1, 5, 26, 58, 10]
lista_numeros2 = [3, 1, 67, 13, 90]

# Función que calcula la diferencia entre dos elementos, para en la más corta
lista_diferencia = list(map(lambda num1, num2: abs(num1 - num2), lista_numeros, lista_numeros2))

print(lista_diferencia)