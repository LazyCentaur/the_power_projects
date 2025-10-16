# PROYECTO LÓGICA: Katas de Python: Ejercicio 38

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

# Astral requiere Python ≥ 3.7 y < 4.0
# pip install astral
from astral import LocationInfo
from astral.sun import sun
from zoneinfo import ZoneInfo
import datetime as dt

city = LocationInfo("Madrid", "Spain", "Europe/Madrid", 40.4168, -3.7038)
tz = ZoneInfo(city.timezone)

ahora = dt.datetime.now(tz)
hoy = ahora.date()

s = sun(city.observer, date=hoy, tzinfo=tz)
amanecer = s["sunrise"]
atardecer = s["sunset"]
mediodia = dt.datetime(hoy.year, hoy.month, hoy.day, 12, 0, 0, tzinfo=tz)

print("Amanecer:", amanecer)
print("Atardecer:", atardecer)
print("Ahora:", ahora)

if amanecer <= ahora < mediodia:
    print("Es de día")
elif mediodia <= ahora < atardecer:
    print("Es por la tarde")
else:
    print("Es de noche")