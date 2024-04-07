# Opdracht 4 condities
# Naam student:
# Groep:


toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = []

for i in toppings: # Door mij (Steven) toegevoegd
    beschikbare_toppings.append(i) # Door mij (Steven) toegevoegd

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...
bestaat = False
for i in beschikbare_toppings:
    if keuze == i[0]:
        prijs = "{:.2f}".format(i[1])
        print(f"U hebt {i[0]} besteld, dat kost €{prijs}")
        bestaat = True

if not bestaat:
    print(f"Uw keuze \"{keuze}\" zit niet in ons assortiment")