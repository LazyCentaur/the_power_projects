# PROYECTO LÓGICA: Katas de Python: Ejercicio 21

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

numero = 24

def cubo(numero):
    if not isinstance(numero, (int, float)) or isinstance(numero, bool):
        raise TypeError("n debe ser numérico")
    return numero ** 3

print(cubo(numero))