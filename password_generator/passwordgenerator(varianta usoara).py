import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like on your password?\n"))
nr_numbers = int(input("How many numbers woukd you like on your password?\n"))
nr_symbols = int(input("How many symbols would you like on your password?\n"))


# cod pt. litere
lista_de_litere = []
b = 0
for i in letters:
    b += 1
    if b <= nr_letters:
        i = random.randint(0, len(letters))
        c = letters[i -1]
        lista_de_litere.append(c)
l = ""
for j in lista_de_litere:
    l += j
print(l)


# cod pt. numere
lista_de_numere = []
a = 0
for t in numbers:
    a += 1
    if a <= nr_numbers:
        y = random.randint(0, len(numbers))
        v = numbers[y -1]
        lista_de_numere.append(v)
p = ""
for u in lista_de_numere:
    p += u
print(p)

# cod pt. simboluri
q = 0
lista_de_simboluri = []
for k in symbols:
    q += 1
    if q <= nr_symbols:
        s = random.randint(0, len(symbols))
        h = symbols[s -1]
        lista_de_simboluri.append(h)
r = ""
for z in lista_de_simboluri:
    r += z
print(r)


len_password = l + p + r
print(len_password)


