# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier
import os

pwd = os.path.dirname(__file__)

meningbestand = f"{pwd}/meningen.txt"


q_regering = input("Wat vind je van de huidige regering?: ")
q_python_lessen = input("Wat vind je van de Python-lessen tot nu toe?: ")
q_mooiste_stad = input("Wat vind jij de mooiste stad van Nederland?: ")

tekstbestand_inhoud = f"Mening regering: {q_regering}\nMening Python lessen: {q_python_lessen}\nMooiste stad Nederland: {q_mooiste_stad}"

with open(meningbestand, 'w') as f:
    f.write(tekstbestand_inhoud)