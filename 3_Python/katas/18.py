# PROYECTO LÓGICA: Katas de Python: Ejercicio 18

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor 
# o igual a 90. Usa la función filter()

nota_corte = 90

class Estudiante:
    """
    Clase Estudiante que representa un estudiante
    """
    def __init__(self, nombre, edad, calificacion):
        
        # Validaciones básicas
        if not isinstance(nombre, str) or not nombre.strip():
            raise TypeError("nombre debe ser str no vacío")
        if not isinstance(edad, int) or isinstance(edad, bool) or edad < 0:
            raise TypeError("edad debe ser int ≥ 0")
        if not isinstance(calificacion, (int, float)) or isinstance(calificacion, bool):
            raise TypeError("calificación debe ser numérica")
        if not (0 <= calificacion <= 100):
            raise ValueError("calificación debe estar entre 0 y 100")
        
        self.nombre = nombre.strip()
        self.edad = edad
        self.calificacion = float(calificacion)
        """
        Constructor de la clase Estudiante.

        Args:
            nombre (str): El nombre del estudiante.
            edad (int): La edad del estudiante.
            calificacion (float): La calificación del estudiante.
        """
    @classmethod
    def crea_estudiante(cls, nombre, edad, calificacion):
        return cls(nombre, edad, calificacion)   

estudiante1 = Estudiante.crea_estudiante("María Isabel", 25, 99.4)
estudiante2 = Estudiante.crea_estudiante("Laura", 22, 85.0)
estudiante3 = Estudiante.crea_estudiante("Lucía", 24, 70.9)
estudiante4 = Estudiante.crea_estudiante("Juan Manuel", 21, 97.3)
estudiante5 = Estudiante.crea_estudiante("Alberto", 25, 57.4)
estudiante6 = Estudiante.crea_estudiante("Marta", 20, 65)
estudiante7 = Estudiante.crea_estudiante("Juan", 22, 89.9)
estudiante8 = Estudiante.crea_estudiante("David", 23, 90)
estudiante9 = Estudiante.crea_estudiante("Luis", 26, 88.4)
estudiante10 = Estudiante.crea_estudiante("Aurora", 24, 90.1)

lista_estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, estudiante6, 
                     estudiante7, estudiante8, estudiante9, estudiante10]

def estudiantes_sobresalientes(lista_estudiantes, nota_corte):
    return list(filter(lambda estudiante: estudiante.calificacion >= nota_corte, lista_estudiantes))

resultado = estudiantes_sobresalientes(lista_estudiantes, nota_corte)

for r in resultado:
    print(f"Es estudiante {r.nombre}, con edad {r.edad}, ha obtenido una calificación de {r.calificacion}")