# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...
from my_modules import csv

filename = "ja.csv"

def main():
    with open(filename, "r") as f:
        data = f.readlines()
    
    keuze = input("Wil je zoeken op; voornaam, tussenvoegsel, achternaam, adres, postcode, of plaats?: ")
    filter_k = input("Waar wil je uit filteren?: ")

    csv.do_filter(csv=data, filter=filter_k, type=keuze)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)