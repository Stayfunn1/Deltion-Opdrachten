# Opdracht 2 lists
# Naam student:
# Groep:

rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}


rivieren = list(rivier_info.keys())



# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']
# Hier jouw code.....


def print_tekst(index_rivier, index_land):
    rivier = rivieren[index_rivier - 1]
    land = rivier_info[str(rivieren[index_rivier - 1])][index_land - 1]
    print(f"De rivier {rivier.capitalize()} stroomt onder andere door {land.capitalize()}")

    
print_tekst(2, 1)

print_tekst(3, 3)

