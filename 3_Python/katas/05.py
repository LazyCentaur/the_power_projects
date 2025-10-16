# PROYECTO LÓGICA: Katas de Python: Ejercicio 5

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

alumno1 = [1, 7, 6, 8, 4, 3, 5, 6, 5, 5]
alumno2 = [2, 2, 0, 6, 2, 7, 1, 6, 8, 3]
alumno3 = [7, 7, 4, 3, 9, 3, 10, 6, 5, 8]

def calificacion(notas, nota_de_corte = 5):
    """Función que calcula la media de una lista de notas
        y devuelve el resultado dependiendo de la media
        que por defecto es 5

    Args:
        notas (list): lista de notas numéricas
        nota_de_corte (int, optional): _description_. Defaults to 5.

    Returns:
        _type_: _description_
    """
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía")
    for i, nota in enumerate(notas):
        if not isinstance(nota, (int, float)) or isinstance(nota, bool):
            raise TypeError(f"Notas inválidas")

    
    media = sum(notas) / len(notas)
    return ("Aprobado", media) if media >= nota_de_corte else ("Suspenso", media)
    
resultadoAlumno1 = calificacion(alumno1)
resultadoAlumno2 = calificacion(alumno2)
resultadoAlumno3 = calificacion(alumno3, 7)    
print(resultadoAlumno1)
print(resultadoAlumno2)
print(resultadoAlumno3)