# PROYECTO LÓGICA: Katas de Python: Ejercicio 34

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

from clases.arbol import Arbol

# Primer árbol
print("Primer árbol")
arbol1 = Arbol(1,[])
arbol1.crecer_tronco(1)
arbol1.nueva_rama()
arbol1.crecer_ramas()
arbol1.nueva_rama()
arbol1.nueva_rama()
arbol1.quitar_rama(2)
print(arbol1.info_arbol())

# Segundo árbol
print("Segundo árbol")
arbol2 = Arbol(1, [2,5,1])
arbol2.crecer_tronco(1)
arbol2.nueva_rama()
print(f"Tronco: {arbol2.tronco}. Ramas: {arbol2.ramas}")
arbol2.crecer_ramas()
arbol2.nueva_rama()
arbol2.crecer_ramas()
arbol2.crecer_ramas()
print(f"Tronco: {arbol2.tronco}. Ramas: {arbol2.ramas}")
arbol2.nueva_rama()
print(f"Tronco: {arbol2.tronco}. Ramas: {arbol2.ramas}")
arbol2.quitar_rama(1)
arbol2.quitar_rama(3)
print(f"Tronco: {arbol2.tronco}. Ramas: {arbol2.ramas}")