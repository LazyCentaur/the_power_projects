# PROYECTO LÓGICA: Katas de Python: Ejercicio 13

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

# como no especifica nada del orden de las letras, he decidido utilizar el set que descarta duplicados


lista_letras = ['m','a','t','r','A','q','x','ñ','a','l','j']

def lista_mayus_minus(letras):
    return list(set(map(lambda letra: tuple([letra.upper(), letra.lower()]), letras)))
    
print(lista_mayus_minus(lista_letras))