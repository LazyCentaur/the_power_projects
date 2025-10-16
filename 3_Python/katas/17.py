# PROYECTO LÓGICA: Katas de Python: Ejercicio 17

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

numeros = [9,5,7,2,6,3,2,1]

def lista_a_num(numeros):
    """Función para concatenar dos números enteros

    Args:
        num1 (int): primer número
        num2 (int): segundo número

    Returns:
        int: número concatenado
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    if not all(isinstance(num, int) and 0 <= num <= 9 for num in numeros):
        raise ValueError("Todos los elementos deben ser dígitos 0–9")
    return reduce(lambda acc, num: acc * 10 + num, numeros, 0)

print(lista_a_num(numeros))

