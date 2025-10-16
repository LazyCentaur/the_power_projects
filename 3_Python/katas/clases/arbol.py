class Arbol:
    """
    Árbol genérico con un tronco y una lista de ramas.

    Atributos:
        tronco (int): Longitud del tronco.
        ramas (List[int]): Longitudes de cada rama.
    """
    def __init__(self, tronco, ramas=None):
        """
        Inicializa el árbol.

        Args:
            tronco: Longitud inicial del tronco (p. ej., 1).
            ramas: Lista inicial de longitudes de ramas. Si es None, empieza sin ramas.
        """
        self.tronco = tronco
        self.ramas = list(ramas) if ramas is not None else []
        
    def crecer_tronco(self, unidad):
        """
        Aumenta la longitud del tronco.

        Args:
            unidad: Unidades a sumar al tronco (p. ej., 1).
        """
        self.tronco += unidad
        
    def nueva_rama(self):
        """
        Añade una nueva rama de longitud 1 al árbol.
        """
        self.ramas.append(1)
        
    def crecer_ramas(self):
        """
        Incrementa en 1 la longitud de todas las ramas existentes.
        """
        for i, rama in enumerate(self.ramas):
            self.ramas[i] = rama + 1
        
    def quitar_rama(self, rama):
        """
        Elimina la rama en la posición indicada.

        Args:
            indice: Índice de la rama a eliminar.
        """
        self.ramas.pop(rama)
        
    def info_arbol(self):
        """
        Devuelve información resumida del árbol.

        Returns:
            str: Texto con la longitud del tronco y las longitudes de las ramas.
        """
        return f"Tronco: {self.tronco}. Ramas: {self.ramas}"