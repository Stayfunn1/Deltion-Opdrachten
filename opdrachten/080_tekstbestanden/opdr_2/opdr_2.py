# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

print(prompt)
try:
    while True:
        gok = input("Voer je gok in: ")
        try:
            gok = int(gok)
            if gok == geheim_getal:
                print("Je hebt het juiste getal geraden, gefeliciteerd!")
                break

            elif gok > geheim_getal:
                print("Je hebt het niet geraden, het geheime getal is lager.")
            elif gok < geheim_getal:
                print("Je hebt het niet geraden, het geheime getal is hoger.")
        except:
            print("Voer een getal in")

except KeyboardInterrupt:
    print("\nWat jammer dat je weg gaat. Je zal mijn geheime getal NOOIT raden!")
except Exception as e:
    print("Error:", e)
