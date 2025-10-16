
# PROYECTO LÓGICA: Katas de Python: Ejercicio 24

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

numeros = [17, -42, 88, 5, -9, 63, 23, -31, -76, 54]

def calcula_diferencia(nums):
    """_summary_

    Args:
        nums (list): lista de int

    Returns:
        int: devuelve la diferencia
    """
    if len(nums) < 2:
        return 0
    
    for i, x in enumerate(nums):
        if not isinstance(x, (int, float)) or isinstance(x, bool):
            raise TypeError(f"Elemento inválido en posición {i}: {x!r}")
    
    _, resultado = reduce(
        lambda acc, x: (x, acc[1] + abs(x - acc[0])),
        nums[1:],
        (nums[0], 0)
    )
    return resultado
    
resultado = calcula_diferencia(numeros)

print(resultado)