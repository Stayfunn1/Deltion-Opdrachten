# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...


def c_to_f(c):
    f = c * 9 / 5 + 32
    f = round(f, 1)
    return f

def f_to_c(f):
    c = (f - 32) * 5 / 9
    c = round(c, 1)
    return c

def print_values(c, f):
    print(f"{c} graden Celsius is gelijk aan {c_to_f(c)} graden Fahrenheit")
    print(f"{f} graden Fahrenheit is gelijk aan {f_to_c(f)} graden Celsius")

c = -12
f = 102

print_values(c, f)

c = 62.2
f = 96

print_values(c, f)