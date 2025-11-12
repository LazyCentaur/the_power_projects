# PROYECTO LÓGICA: Katas de Python: Ejercicio 30

# 30. Crea una función que determine si dos palabras son anagramas, es decir, 
# si están formadas por las mismas letras pero en diferente orden.

palabra1 = "aceros"
palabra2 = "riesgo"
palabra3 = "Sergio"
palabra4 = "pagar"
palabra5 = "grapaa"
palabra6 = "arco"
palabra7 = "escora"
              
def anagramas(texto1, texto2):
    if not isinstance(texto1, str) or not isinstance(texto2, str):
        raise TypeError("Ambos argumentos deben ser str")
    
    a, b = texto1.lower(), texto2.lower()
    
    # Los anagramas deben tener la misma longitud
    if len(a) != len(b):
        return f"Las palabras ({texto1} y {texto2}) NO son anagramas"
    
    # Comparar las letras ordenadas
    if sorted(a) == sorted(b):
        return f"Las palabras analizadas ({texto1} y {texto2}) SÍ son anagramas"
    else:
        return f"Las palabras ({texto1} y {texto2}) NO son anagramas"              


print(anagramas(palabra1, palabra5))
print(anagramas(palabra4, palabra5))
print(anagramas(palabra1, palabra7))
print(anagramas(palabra3, palabra6))