# Opdracht 1 functies
# Naam student:
# Groep:
import math

def kubus_vol(m):
    volume = m * m * m
    return f"Inhoud kubus:\t{round(volume, 2)}"

def bol_vol(r):
    volume = 4/3 * math.pi * r ** 3
    return f"Inhoud bol:\t{round(volume, 2)}"

zijde = 5
radius = 4

print(kubus_vol(5))
print(bol_vol(4))