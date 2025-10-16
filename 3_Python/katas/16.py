# PROYECTO LÓGICA: Katas de Python: Ejercicio 16

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva 
# una lista de todas las palabras que sean más largas que n. Usa la función filter()
import re

texto = "Hoy salí temprano, a caminar, por el parque encontré un café tranquilo pensé ideas nuevas para proyectos respiré profundo y volví feliz a casa sonriente"
numero = 8

def palabras_largas(texto, numero):
    """Devuelve palabras con longitud > numero

    Args:
        texto (string): cadena de texto
        numero (int): número entero

    Returns:
        list: lista de todas las palabras que sean más largas que número
    """
    
    if not isinstance(texto, str):
        raise TypeError("texto debe ser str")
    if not isinstance(numero, int) or numero < 0:
        raise ValueError("n debe ser entero ≥ 0")
    
    palabras = re.split(r"[ ,]+", texto.strip())
    return list(filter(lambda palabra: numero < len(palabra), palabras))
    
print(palabras_largas(texto, numero))