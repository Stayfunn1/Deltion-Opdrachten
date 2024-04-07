# Opdracht 1
# Naam student:
# Groep:

# Hier komt je code...

from collections import Counter
 
my_string = "Tinus gaat op zijn tandem naar de hottentottententoonstelling"
my_list = [my_string]

print(f"De letter \"t\" komt {my_list[0].count("t")}x voor in my_string")

number = 0
for i in my_list[0]:
    if i.lower() == "t":
        number = number + 1

print(f"De letter \"t\" en \"T\" komt {number}x voor in my_string") # For loop
print(f"De letter \"t\" en \"T\" komt {my_list[0].lower().count("t")}x voor in my_string")
