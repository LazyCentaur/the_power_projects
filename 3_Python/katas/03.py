
# PROYECTO LÓGICA: Katas de Python: Ejercicio 3

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

lista_de_palabras = ["bufanda gris", "sombrero verde", "zapato de hombre", "zapato de mujer", 
                 "vestido rojo", "jersey verde", "copa gris", "árbol", "zapato negro", "jersey rojo"]
palabra_objetivo = "rojo"

def lista_palabras(lista, palabra):
    """Esta función busca dentro de una lista los strings que contengan
    otro string

    Args:
        lista (list): lista donde buscar
        palabra (string): palabra a buscar

    Returns:
        list: lista con el resultado de las coincidencias
    """
    if not isinstance(lista, list):
        raise TypeError("lista debe ser list")
    if not isinstance(palabra, str):
        raise TypeError("palabra debe ser str")
    if not palabra:
        return []

    lista_resultado = []
    for item in lista:
        if item.find(palabra) != -1:
            lista_resultado.append(item)
    return lista_resultado
            
lista2 = lista_palabras(lista_de_palabras, palabra_objetivo)
print(lista2)