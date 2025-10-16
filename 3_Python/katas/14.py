# PROYECTO LÓGICA: Katas de Python: Ejercicio 14

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. 
# Usa la función filter()

palabras = [
    "luna", "montaña", "murciélago", "orquídea", "nómada",
    "globo", "Teclado", "Café", "ventana", "píxel",
    "tornado", "sándalo", "guitarra", "algoritmo", "bosque",
    "nube", "espejo", "trueno", "puente", "canica",
    "azulejo", "río", "Brújula", "vórtice", "linterna",
    "susurro", "pradera", "quimera", "farola", "bitácora"
]

letra = "P"

def palabras_primera_letra(palabras, letra):
    """Devuelve las palabras que empiezan por `letra` (insensible a mayúsculas/acentos)."""
    if not letra:
        return []
    return list(filter(lambda palabra: palabra[0].lower() == letra.lower(), palabras))
        
print(palabras_primera_letra(palabras, letra))