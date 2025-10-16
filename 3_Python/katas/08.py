# PROYECTO LÓGICA: Katas de Python: Ejercicio 8

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

# Aquí he hecho dos casos separados para manejar los errores de manera distinta, 
# si no se puede convertir a float el string, lanza una excepción, 
# si el número es 0, pedirá que lo vuelvas a ingresar

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

def division_numeros(num1, num2):
    """Función para dividir dos números, revisamos que no sean 0 
    Args:
        num1 (float): primer número para la división
        num2 (float): segundo número para la división
    """
    if num1 == 0:
        num1 = float(input("No es posible dividir con un 0, vuelve a introducir el primer número: "))
    if num2 == 0:
        num2 = float(input("No es posible dividir con un 0, vuelve a introducir el segundo número: "))
        division_numeros(num1, num2)
    
    resultado = round(num1/num2, 2)
    print(f"El resultado de la división es: {resultado}")
        
division_numeros(numero1, numero2)