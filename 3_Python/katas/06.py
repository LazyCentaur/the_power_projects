# PROYECTO LÓGICA: Katas de Python: Ejercicio 6

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

numero = 18

def factorial_numero(numero):
    """Esta función calcula el factorial de un número dado

    Args:
        numero (int): número del que queremos conocer el factorial
    
    Returns:
        int: factorial del número dado
    """
    
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError("n debe ser un entero no booleano")
    if numero < 0:
        raise ValueError("n debe ser >= 0")
    
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial_numero(numero - 1)
        
resultado = factorial_numero(numero)
print(resultado)