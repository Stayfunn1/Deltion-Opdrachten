# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

input = "Deze zin wil ik gaan encrypten, dat lijkt me leuk"

enc_list = []
for char in input:
    enc = ord(char)
    enc += 5
    enc_list.append(enc)

enc_full_str = ""
for enc in enc_list:
    try:
        enc_str = chr(enc)
    except Exception as e:
        print(e)
    
    enc_full_str += enc_str


print(enc_full_str)

    


