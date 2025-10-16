# PROYECTO LÓGICA: Katas de Python: Ejercicio 11

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

while True:
    edad_str = input("Introduce tu edad (0-120): ").strip()
    try: 
        edad = int(edad_str)
    except ValueError:
        print("Edad no válida, introduce un número entero")
        continue
    if 0 <= edad <= 120:
        print(f"Tu edad es {edad}")
        break    
    print("Edad fuera de rango, introduce un número entero desde 0 a 120")