# PROYECTO LÓGICA: Katas de Python: Ejercicio 38

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

# Astral requiere Python ≥ 3.7 y < 4.0

import datetime as dt

ahora = dt.datetime.now()
hora = ahora.hour
# hora = int(input("Introduce la hora (0-23): "))

if 6 <= hora < 12:
    print("Es de día (mañana)")
elif 12 <= hora < 20:
    print("Es de tarde")
else:
    print("Es de noche")