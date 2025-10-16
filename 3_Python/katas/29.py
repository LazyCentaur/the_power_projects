# PROYECTO LÓGICA: Katas de Python: Ejercicio 29

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos 
# los caracteres con el carácter '#', excepto los últimos cuatro.

var1 = 123456789101112131415643

var2 = "Esto es una cadena de texto"

def enmascara_caracteres(variable):
    """Convierte a str y enmascara todo salvo los últimos 4 caracteres."""
    variable_str = str(variable)
    if len(variable_str) <= 4:
        return variable_str
    return "#" * (len(variable_str) - 4) + variable_str[-4:]
            
print(enmascara_caracteres(var1))
print(enmascara_caracteres(var2))