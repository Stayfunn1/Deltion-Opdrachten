# Opdracht 3 condities
# Naam student:
# Groep:

normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

def bereken(eigenleeftijd):
    print(f"Uw ingevulde leeftijd is {eigenleeftijd}")
    for i in leeftijd:
        if leeftijd[i][0] <= eigenleeftijd <= leeftijd[i][1]: # In welke groep val je?
            print(f"U behoort tot de groep {i}")
            for k in kortings_percentages:
                if i == k: # Hoe veel korting krijg je?
                    print(f"U krijgt {kortings_percentages[k]}% korting")
                    procent_eraf = 100 - kortings_percentages[k]
                    # Hoeveel betaal je?
                    prijs = "{:.2f}".format(normale_toegangsprijs * procent_eraf / 100)
                    print(f"U betaald daarom €{prijs}")


eigenleeftijd = input("Vul je leeftijd in: ") # Vul je leeftijd in, dus volgens de opdracht 3, 23 en 89
eigenleeftijd = int(eigenleeftijd)

bereken(eigenleeftijd)

# Hier komt je code...
