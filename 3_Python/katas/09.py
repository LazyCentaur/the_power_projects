# PROYECTO LÓGICA: Katas de Python: Ejercicio 9

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()

mascotas = [
    "Perro", "Gato", "Conejo", "Serpiente Pitón", "Hámster", "Cobaya",
    "Hurón", "Chinchilla", "Rata doméstica", "Erizo pigmeo africano", "Canario",
    "Periquito", "Oso", "Agapornis", "Ninfa (carolina)", "Loro (yaco/amazonas)", "Tortuga de agua",
    "Tortuga terrestre", "Gecko leopardo", "Dragón barbudo", "Serpiente del maíz", "Pez betta",
    "Goldfish", "Guppy", "Axolote", "Camaleón velado", "Tarántula", "Tigre",
    "Mapache", "Cocodrilo"
]
mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

def excluye_mascotas_prohibidas(lista_mascotas, mascotas_prohibidas):
    """Función que sirve para comparar dos listas de mascotas y eliminar las coincidencias
    Args:
        lista_mascotas (list): lista de mascotas a revisar
        mascotas_prohibidas (list): lista de mascotas prohibidas

    Returns:
        list: lista de mascotas permitidas
    """
    if not isinstance(lista_mascotas, list) or not isinstance(mascotas_prohibidas, list):
        raise TypeError("Ambos parámetros deben ser listas")
    # Convertir mascotas prohibidas a minúsculas para comparación
    prohibidas_lower = [m.lower() for m in mascotas_prohibidas]
    return list(filter(lambda m: isinstance(m, str) and m.lower() not in prohibidas_lower, lista_mascotas))

mascotas_permitidas = excluye_mascotas_prohibidas(mascotas, mascotas_prohibidas)
print(f"Esta es tu lista de mascotas actualizada con las permitidas: {mascotas_permitidas}")