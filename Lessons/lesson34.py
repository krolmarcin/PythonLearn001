import re

# 1 litera duża, reszta mała
if re.match("^[A-Z][a-z]*$", "Marcin"):
    print("1. Dopasowano!")
else:
    print("1. Nie dopasowano!")

# 2 + oznac, że symbol musi wystąpić 1 raz
if re.match("^[A-Z][a-z]+$", "M"):
    print("2. Dopasowano!")
else:
    print("2. Nie dopasowano!")

# 3 ? mówi, że dany symbol musi wystąpić, ale tylko raz, lub wcale, chodzi tu o małą literę po pierwszej dużej
if re.match("^[A-Z][a-z]?[A-Z]$", "MaR"):
    print("3. Dopasowano!")
else:
    print("3. Nie dopasowano!")

# 4 ograniczenie do przedziału wystąpienia znaku, można nie narzucać górnego limitu, wtedy: {2,}
# nie dajemy drugiej liczby (z prawej strony), albo dolny limit {,5} nie dajemy pierwszej liczby (z lewej strony)
if re.match("^[A-Z][a-z]{2,5}$", "Marcin"):
    print("4. Dopasowano!")
else:
    print("4. Nie dopasowano!")
