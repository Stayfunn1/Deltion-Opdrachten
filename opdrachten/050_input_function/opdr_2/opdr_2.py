# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

def print_gasten(gasten):
    print("Gasten die komen:")
    for i in gasten:
        print("   ", i)

gasten = ["Steven", "Paul", "Kees", "Marie", "Hilda"]

print_gasten(gasten)

print("\nMarie belt helaas af")
gasten.remove("Marie")

print_gasten(gasten)

print("\nGeorge komt er gezellig bij")
gasten.append("George")

print_gasten(gasten)