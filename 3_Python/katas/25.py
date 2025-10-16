# PROYECTO LÓGICA: Katas de Python: Ejercicio 25

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

texto = "Este es un texto de ejemplo con caracteres, pensado para prueba rápidas de longitud sin trucos extraños."

def numero_caracteres(texto):
    """Devuelve el número de caracteres del string dado."""
    if not isinstance(texto, str):
        raise TypeError("texto debe ser str")
    return len(texto)

total_caracteres = numero_caracteres(texto)

print(f"El número total de caracteres es {total_caracteres}")