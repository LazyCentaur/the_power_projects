# PROYECTO LÓGICA: Katas de Python: Ejercicio 26

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

num1  = 98
num2 = 25

try:
    if not isinstance(num1, (int, float)) or isinstance(num1, bool):
        raise TypeError("num1 debe ser (int/float)")
    if not isinstance(num2, (int, float)) or isinstance(num2, bool):
        raise TypeError("num2 debe ser (int/float)")
    if num2 == 0:
        raise ZeroDivisionError("no debe haber 0 en la división")
except (TypeError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    resto = lambda x, y: x % y
    print(resto(num1, num2))