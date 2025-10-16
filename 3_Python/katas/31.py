# PROYECTO LÓGICA: Katas de Python: Ejercicio 31

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego 
# solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime 
# un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def lista_de_nombres():
    """Función con la que generas una lista de nombres con input 
    y después buscas dentro de esa lista un nombre
    """
    lista_nombres = []
    print("Escribe uno a uno los nombres que quieres agregar en la llista, para finalizar escribe la palabra Terminar")
    nombre = input("Escribe un nombre: ").strip()
    while nombre.lower() != "terminar":
        lista_nombres.append(nombre)
        nombre = input("Escribe otro nombre: ").strip()
        
    print("Genial, lista terminada")
    buscar_nombre = input("Escribe ahora el nombre que quieras buscar: ").strip()
    if buscar_nombre in lista_nombres:
        print("Nombre en la lista!")
    else:
        print("El nombre no está en la lista")
        
lista_de_nombres()