# PROYECTO LÓGICA: Katas de Python: Ejercicio 39

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

import math

nota = 80.2
  
def calificacion(nota):
    """Esta función sirve para devolver una calificación en string en función de una nota numérica

    Args:
        nota (int, float): nota numérica

    Returns:
        string: calificación en string
    """
    if (not isinstance(nota, (int, float)) or isinstance(nota, bool)
        or not math.isfinite(nota) or not (0 <= nota <= 100)):
        return "Introduce una nota numérica válida"
    
    return ("La calificación obtenida es: excelente" if 90 <= nota <= 100 else
            "La calificación obtenida es: muy bien" if 80 <= nota < 90  else
            "La calificación obtenida es: bien" if 70 <= nota < 80  else
            "La calificación obtenida es: insuficiente" if 0 <= nota < 70 else
            "Introduce una nota numérica válida")
    
print(calificacion(nota))