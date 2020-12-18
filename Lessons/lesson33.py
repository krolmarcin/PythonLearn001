import re

# Symbol '.' dany tekst musi zaczynać się od patternu 'ko'
# chyba, że ^ko.$ = 3 znaki 3 dowolny
if re.match("ko.", "kot"):
    print("1. Dopasowano!")
else:
    print("1. Nie dopasowano!")

# Klasa znaków - wyraz składa się z trzech znaków dwa pierwsze to Duże 'K', albo małe 'k'
if re.match("^[Kk]o.$", "koc"):
    print("2. Dopasowano!")
else:
    print("2. Nie dopasowano!")

# Wyraz zaczyna się z dużej litery od A do Z
if re.match("[A-Z]", "Mocno"):
    print("3. Dopasowano!")
else:
    print("3. Nie dopasowano!")

# Wyraz zaczyna się z dużej, albo małej litery od A do Z
if re.match("[A-Za-z]", "maniek"):
    print("3. Dopasowano!")
else:
    print("3. Nie dopasowano!")

# Wyraz zaczyna się z litery, która nie zawiera się w tym konkretym zbiorze (negacja), daszek '^'
if re.match("[^A-Za-z]", "maniek"):
    print("3. Dopasowano!")
else:
    print("3. Nie dopasowano!")

# kondensacja wiedzy :)
if re.match("^[rR]ok[-_=][0-9][0-9][0-9][0-9]$", "Rok=2020"):
    print("3. Dopasowano!")
else:
    print("3. Nie dopasowano!")
