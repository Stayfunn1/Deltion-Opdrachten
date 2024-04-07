# Opdracht 2 lists
# Naam student:
# Groep:

def print_tekst(rivier_info, rivieren, index_rivier, index_land):
    rivier = rivieren[index_rivier - 1]
    land = rivier_info[str(rivieren[index_rivier - 1])][index_land - 1]
    print(f"De rivier {rivier.capitalize()} stroomt onder andere door {land.capitalize()}")


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())

# print(rivieren[1], rivier_info[str(rivieren[1])][2])

print_tekst(rivier_info, rivieren, 2, 1)

print_tekst(rivier_info, rivieren, 3, 3)

# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....