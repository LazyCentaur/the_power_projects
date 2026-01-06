# Ejercicio 1: Variables y Tipos de Datos
# Define una variable llamada numero con el valor 10 y otra llamada nombre con tu nombre.

numero <- 10
nombre <- "Marta"

# Ejercicio 2: Funciones class e is.numeric
# Utiliza las funciones class e is.numeric para determinar el tipo de dato de numero.
class(numero)
class(nombre)
is.numeric(numero)
is.numeric(nombre)

# Ejercicio 3: Operaciones Aritméticas
# Realiza una operación aritmética que sume numero y el doble de numero.
resultado <- numero + (numero *2) 
resultado

# Ejercicio 4: Vectores y Listas
# Crea un vector llamado edades con las edades de tres personas y
# una lista llamada informacion con el nombre y la edad de una persona.
edades = c(25, 48, 36)
información = c("José", "Laura", "Sergio")

# Ejercicio 5: Funciones is.character e is.logical
# Verifica si nombre es de tipo caracter y si es_numerico es de tipo lógico.
is.character(nombre)
is.logical(numero)

# Ejercicio 6: Operaciones Lógicas
# Crea una variable llamada mayor_de_edad que sea TRUE si la edad
# de la primera persona en edades es mayor o igual a 18.
mayor_de_edad <- if (edades[1] > 18) {
  TRUE
} else {
  FALSE
}
mayor_de_edad

# Ejercicio 7: Comparaciones de Vectores
# Utiliza el operador %in% para verificar si el valor 30 está presente en el vector edades .
presente <- if (30 %in% edades) {
  TRUE
} else {
  FALSE
}
presente

# Ejercicio 8: Operadores de Comparación
# Compara si el doble de numero es mayor que edades[3] .
doble <- if ((numero * 2) > edades[3]) {
  TRUE
} else {
  FALSE
}
doble

# Ejercicio 9: Utilizar Operador Lógico
# Define dos variables lógicas, condicion1 y condicion2 , ambas con
# valor TRUE . Comprueba si ambas condiciones son verdaderas.
condicion1 <- TRUE
condicion2 <- TRUE
verdaderas <- condicion1 & condicion2
verdaderas

# Ejercicio 10: Utilizar Operador Lógico
# Define una variable lógica, verdadero , con valor TRUE. 
# Comprueba que su valor NO sea verdadero.
verdadero = TRUE
valor <- verdadero != verdadero
valor
