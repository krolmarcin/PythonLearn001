import re

wynik = re.match(r"^Hello World$", "Hello World")

if wynik:
    print("1. Dopasowano!")
else:
    print("1. Nie dopasowano!")

# 2. Grupy znaków
wynik2 = re.match(r"^(Hello) (Wor(ld))$", "Hello World")

if wynik:
    print("2. Dopasowano!")
    print(wynik2.group())
    print(wynik2.group(0))
    print(wynik2.group(1))
    print(wynik2.group(2))
    print(wynik2.group(3))
    print(wynik2.groups()) # Zraca wszystkie grupy w postaci krotki
else:
    print("2. Nie dopasowano!")

# 3. + mówi, że gruoa znaków musi się pojawć conajmniej raz, ale tu bez spacji, spację można dodać w tej grupie: ( World)
# grupy nienazwane
wynik3 = re.match(r"^(Hello) (World)+$", "Hello WorldWorldWorldWorldWorld")

if wynik3:
    print("3. Dopasowano!")
    print(wynik3.group())
    print(wynik3.group(0))
    print(wynik3.group(1))
    print(wynik3.group(2))
    print(wynik3.groups()) # Zraca wszystkie grupy w postaci krotki
else:
    print("3. Nie dopasowano!")

# 4. grupa nazwana, można wywołać po nazwanej etykiecie, pkt. 4
wynik4 = re.match(r"^(He(?P<first>ll)o) (World)+$", "Hello WorldWorldWorldWorldWorldWorld")

if wynik4:
    print("4. Dopasowano!")
    print(wynik4.group())
    print(wynik4.group(0))
    print(wynik4.group(1))
    print(wynik4.group(2))
    print(wynik4.group(3))
    print(wynik4.groups()) # Zraca wszystkie grupy w postaci krotki
    print(wynik4.group("first"))
else:
    print("4. Nie dopasowano!")

# 5. grupa nienazwana anonimowa, nie ma indexu grupy anonimowej
wynik5 = re.match(r"^((?:He)(?P<first>ll)o) (World)+$", "Hello WorldWorldWorldWorldWorldWorld")

if wynik5:
    print("5. Dopasowano!")
    print(wynik5.group())
    print(wynik5.group(0))
    print(wynik5.group(1))
    print(wynik5.group(2))
    print(wynik5.group(3))
    print(wynik5.groups()) # Zraca wszystkie grupy w postaci krotki
    print(wynik5.group("first"))
else:
    print("5. Nie dopasowano!")

# 6. jesli chcę kropkę to \., normalnie . ma znaczenie 1 znak, jest 1 z 2 znaków (1|.) - kropka jak dowolny
wynik6 = re.match(r"^((?:He)(?P<first>ll)o) (World)+(!|.)$", "Hello WorldWorldWorldWorldWorldWorld&")

if wynik6:
    print("6. Dopasowano!")
    print(wynik6.group())
    print(wynik6.group(0))
    print(wynik6.group(1))
    print(wynik6.group(2))
    print(wynik6.group(3))
    print(wynik6.groups()) # Zraca wszystkie grupy w postaci krotki
    print(wynik6.group("first"))
else:
    print("6. Nie dopasowano!")

# 7. sprawdzenie mala
wynik7 = re.match(r"^([A-Za-z0-9]+|[A-Za-z0-9\.-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9-\.]+[A-Za-z0-9])\.[A-Za-z0-9]+$"
                  , "marcin.krol@jakasdomena.com")

if wynik7:
    print("7. Dopasowano!")
else:
    print("7. Nie dopasowano!")
