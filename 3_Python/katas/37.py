# PROYECTO LÓGICA: Katas de Python: Ejercicio 37

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: 
# contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto. 
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

import re

texto1 = (
    "Salí temprano, cuando la ciudad aún bostezaba. El aire fresco olía a pan recién hecho y a  promesa. "
    "Caminé sin rumbo, siguiendo luces intermitentes, charcos tímidos y persianas medio abiertas. Una cafetería "
    "pequeña me recibió con vapor, tazas gruesas y música lenta. Pedí un café negro, miré por la ventana, dejé "
    "el teléfono dormir. Afuera, dos vecinos discutían plantas; un perro perseguía hojas que no quería atrapar. "
    "Pensé en pendientes, ideas y errores, y me perdoné un poco. Al terminar, doblé la servilleta como un mapa. "
    "Decidí volver por otra calle, para encontrar algo diferente, aunque fuese pequeño."
)
    
texto2 = (
    "Aprender exige constancia, no heroísmo. Empieza por bloques pequeños, con objetivos claros y descansos "
    "cortos. Anota dudas sin resolver y vuelve a ellas con calma. Alterna teoría con práctica: después de leer, "
    "implementa un ejemplo mínimo, rompe algo, investiga por qué. Si estudias programación, escribe pruebas, nombra bien, "
    "elimina ruido. Guarda ejemplos en un repositorio; documenta lo que te costó entender. Pide revisión a alguien; "
    "aceptar críticas acelera. Mide avances por hábitos, no por horas. Cuando falles, registra el error y el contexto; " 
    "así aprenderás patrones invisibles. Y celebra pequeños logros: también entrenan la mente para continuar mañana."
)

def procesa_texto(opcion, texto, *args):
    match opcion:
        case "contar":
            return contar_palabras(texto)
        
        case "reemplazar":
            if len(args) != 2:
                raise TypeError("reemplazar requiere dos argumentos: palabra, palabra_nueva")
            palabra, palabra_nueva = args
            palabra_er = rf'\b{re.escape(palabra)}\b'
            return reemplazar_palabras(texto, palabra_er, palabra_nueva)
        case "eliminar":
            if len(args) != 1:
                raise TypeError("eliminar requiere un argumento: palabra")
            palabra = args[0]
            palabra_er = rf'\b{re.escape(palabra)}\b'
            return eliminar_palabra(texto, palabra_er)
        case _:
            raise ValueError("Opción inválida")
        
def contar_palabras(texto):
    # Extrae palabras (unicode), normaliza y cuenta
    palabras = re.findall(r"\b\w+\b", texto, flags=re.UNICODE)
    frec = {}
    for palabra in palabras:
        k = palabra.casefold()
        frec[k] = frec.get(k, 0) + 1
    return frec

def reemplazar_palabras(texto, palabra_vieja, palabra_nueva):
    # utilizo re.sub para que no reemplace partes de palabras, solo palabras enteras
    return re.sub(palabra_vieja, palabra_nueva, texto, flags=re.IGNORECASE)

def eliminar_palabra(texto, palabra):
    texto_nuevo = re.sub(palabra, "", texto, flags=re.IGNORECASE).strip()
    return texto_nuevo.replace("  ", " ")

print(procesa_texto("contar", texto1))

print(procesa_texto("reemplazar", texto2, "con", "NUEVA"))

print(procesa_texto("eliminar", texto2, "con"))

print(procesa_texto("eliminar", texto1, "Salí"))