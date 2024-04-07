# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

print("Standaard lijst:", my_list)

my_list = sorted(my_list)

print("\nGesorteerde lijst:", my_list)

my_list.append("Calzone")

print("\nToegevoegde pizza zonder opnieuw to sorteren:", my_list)

my_list.remove("verdi")

print("\nVerwijdererde pizza:", my_list)

print("\nEerste 3 pizza's geprint:", my_list[:3])

print("\nDe middelste pizza uit de lijst is:", my_list[int(len(my_list) / 2)])

print("\nDe laatste 3 pizza's in de lijst:", my_list[int(len(my_list) - 3):])