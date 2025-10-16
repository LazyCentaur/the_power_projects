# PROYECTO LÓGICA: Katas de Python: Ejercicio 10

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 89, 12]
lista3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista4 = []

class ListaVaciaError(Exception):
    """Se lanza cuando la lista está vacía."""
    pass

def calcula_promedio(lista_numeros):
    if not lista_numeros:
        raise ListaVaciaError("La lista está vacía")
    return sum(lista_numeros) / len(lista_numeros)
    
listas = [lista1, lista2, lista3, lista4]

for i, L in enumerate(listas, start=1):
    try:
        print(f"resultado{i} =", calcula_promedio(L))
    except ListaVaciaError as e:
        print(f"resultado{i} -> error: {e}")
