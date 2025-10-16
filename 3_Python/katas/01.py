# PROYECTO LÓGICA: Katas de Python: Ejercicio 1

# 1. Escribe una función que reciba una cadena de texto como parámetro 
# y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.

texto = input('escribe lo que quieras: ')

def frecuencia_letras(texto):
    """Esta función cuenta la cantidad de veces que aparece una
    letra en una frase, para ello se convierten todas a minúsculas
    y se omiten los espacios

    Args:
        texto (string): texto para el conteo
    Returns:
        dict: devuelve un diccionario donde la key es la letra 
        y el value la cantidad de veces que aparece
    """
    if not isinstance(texto, str):
        raise TypeError("texto debe ser str")
    
    lista = list(texto.lower())
    letras_revisadas = []
    resultado = {}
    
    for letra in lista:
        if letra == ' ':
            continue
        if letra not in letras_revisadas:
            letras_revisadas.append(letra)
            conteo = 0
            resultado[letra] = conteo
            for letra2 in lista:
                if letra == letra2:
                    conteo += 1
                    resultado[letra] = conteo
    return resultado
        
calculo_frecuencia = frecuencia_letras(texto)

for key, value in calculo_frecuencia.items():
    print(f'La frecuencia de la letra {key} es de {value} apariciones')