# PROYECTO LÓGICA: Katas de Python: Ejercicio 23

# 23. Concatena una lista de palabras. Usa la función reduce().

from functools import reduce

palabras = ["luna", "montaña", "café", "murciélago", "ventana", 
            "bosque", "teclado", "tormenta", "brújula", "orquídea"]

def concatena_palabras(pal1, pal2):
    """ Concatena palabras separadas por un espacio"""
    return f"{pal1} {pal2}"

resultado = reduce(concatena_palabras, palabras)

print(resultado)