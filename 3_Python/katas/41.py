# PROYECTO LÓGICA: Katas de Python: Ejercicio 41

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales 
# para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. 
# El programa debe hacer lo siguiente:
#  1. Solicita al usuario que ingrese el precio original de un artículo.
#  2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#  3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#  4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
#  5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#  6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

try:
    precio_original = float(input("Introduce el precio del artículo: "))
    cupon_dto = input("¿Tienes un cupón descuento? (S/N): ")
    precio_final = 0

    if cupon_dto == "S" or cupon_dto == "s":
        valor_dto = float(input("Ingresa el valor del cupón descuento: "))
        if 0 < valor_dto < precio_original:    
            precio_final = precio_original - valor_dto
            print(f"El precio original sin descuento era {precio_original}")
            print(f"El precio final con descuento del artículo es {precio_final}")
        elif valor_dto > precio_original:
            print("El descuento no puede ser mayor que el precio original")
        else:
            print("El descuento no es válido")
    else:
        print(f"No tienes un cupón descuento, el valor del artículo es {precio_original}")
except ValueError:
    print("Introdce precio válido")


