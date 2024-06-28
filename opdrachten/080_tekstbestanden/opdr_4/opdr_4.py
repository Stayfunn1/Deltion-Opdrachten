# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
voornaam = input("1. Wat is je voornaam?\n")
achternaam = input("2. Wat is je achternaam?\n")
drank = input("3. Wat neem je mee aan drank?\n")
eten = input("4. Wat neem je mee om te eten?\n")


content = f"""----
voornaam: {voornaam}
achternaam: {achternaam}
drank: {drank}
eten: {eten}
"""

with open("party_details.txt", "a") as file:
    file.write(content)
