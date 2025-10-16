# PROYECTO LÓGICA: Katas de Python: Ejercicio 30

# 30. Crea una función que determine si dos palabras son anagramas, es decir, 
# si están formadas por las mismas letras pero en diferente orden.

from collections import Counter

palabra1 = "aceros"
palabra2 = "riesgo"
palabra3 = "Sergio"
palabra4 = "pagar"
palabra5 = "grapaa"
palabra6 = "arco"
palabra7 = "escora"

def anagramas(texto1, texto2):
    """Esta función sirve para comparar 2 palabras y saber si son anagramas

    Args:
        texto1 (string): primera palabra a comprar
        texto2 (_type_): segunda palabra a comparar

    Returns:
        string : respuesta a si es anagrama o no
    """
    if not isinstance(texto1, str) or not isinstance(texto2, str):
        raise TypeError("Ambos argumentos deben ser str")
    a, b = texto1.casefold(), texto2.casefold()
    if len(a) != len(b):
        return f"Las palabras ({texto1} y {texto2}) NO son anagramas"
    
    anagrama = True
    for letra1 in texto1:
        if texto2.find(letra1) == -1:
            anagrama = False
    for letra2 in texto2:
        if texto1.find(letra2) == -1:
            anagrama = False
    return f"Las palabras analizadas ({texto1} y {texto2}) SÍ son anagramas" if anagrama else f"Las palabras ({texto1} y {texto2}) NO no son anagramas"
              
print(anagramas(palabra1, palabra5))
print(anagramas(palabra4, palabra5))
print(anagramas(palabra1, palabra7))
print(anagramas(palabra3, palabra6))