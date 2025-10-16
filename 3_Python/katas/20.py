# PROYECTO LÓGICA: Katas de Python: Ejercicio 20

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. 
# Usa la función filter()

lista_int_str = [
    42, "hola", 0, "marta", -7, "QA", 123, "python", 9999, "katas",
    3, "prueba", 18, "bug", 27, "feature", -100, "release", 5, "commit",
    64, "merge", 1, "ticket-42", 88, "ok", 256, "done", 73, "refactor"
]

resultado = list(filter(lambda x: type(x) is int, lista_int_str))

print(resultado) 