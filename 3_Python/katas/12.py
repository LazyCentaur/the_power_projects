# PROYECTO LÓGICA: Katas de Python: Ejercicio 12

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

# He añadido el import re para que separe también por ","

import re

frase = "Esto es una frase, y esto también"

def longitud_palabras(texto):
    """Devuelve una lista con la longitud de cada palabra."""
    palabras = re.split(r"[ ,]+", texto.strip())
    return list(map(lambda longitud: len(longitud), palabras))
        
resultado = longitud_palabras(frase)

print(f"Estos son las longitudes de las pablabras: {resultado}")