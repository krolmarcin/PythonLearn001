import re

# Symbol '.' dany tekst musi zaczynać się od patternu 'ko'
# chyba, że ^ko.$ = 3 znaki 3 dowolny

if re.match("ko.", "kot"):
    print("1. Dopasowano!")
else:
    print("1. Nie dopasowano!")

# Klasa znaków
if re.match("^[Kk]o.$", "koc"):
    print("2. Dopasowano!")
else:
    print("2. Nie dopasowano!")
