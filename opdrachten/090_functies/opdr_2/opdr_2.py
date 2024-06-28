# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
    miles = round(km / 1.609344, 1)
    return f"{km} km == {miles} mijl"

def miles_naar_kilometers(miles):
    km = round(miles * 1.609344, 1)
    return f"{miles} mijl == {km} km"

kilometers = 1223
miles = 867

print(kilometers_naar_miles(kilometers))
print(miles_naar_kilometers(miles))