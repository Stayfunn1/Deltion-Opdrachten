# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

def programma(zijde_a, zijde_b):
    zijde_c = math.sqrt(float(zijde_a)**2 + float(zijde_b)**2)
    return zijde_c


zijde_a = input("Geef de lengte van zijde a: ")
zijde_b = input("Geef de lengte van zijde b: ")

zijde_c = programma(zijde_a, zijde_b)

print(f"De lengte van de schuine zijde is: {zijde_c}")