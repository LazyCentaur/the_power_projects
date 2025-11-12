# PROYECTO LÓGICA: Katas de Python: Ejercicio 28

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# entiendo que en esta lista el primer elemento es "repetido", 
# no que se refiere al 42 que está repetido pero sale más adelante

lista_elementos = [42, "repetido", -7, 3.14, True, "QA", 0, "python", 9999, False,
 "katas", "repetido", "bug", 27, "release", -100.5, "commit", 64, "merge", 1,
 "ticket-42", 88, "ok", 256, "QA", 42, "refactor", 2.718, "árbol", -33]

def encuentra_duplicado(lista):
    vistos = []
    for elem in lista:
        if elem in vistos:
            # añado este for porque sino el 0 lo toma como False, y el primer elemento repetido que saca es False
            for v in vistos:
                if v == elem and type(v) == type(elem):
                    return elem
        vistos.append(elem)
    return None

resultado = encuentra_duplicado(lista_elementos)

print(resultado)