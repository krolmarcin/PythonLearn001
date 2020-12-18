import re

wzor1 = "banan\nbanan\tbanan"
wzor2 = r"banan\nbanan\tbanan"
print(wzor1)
print(wzor2)

wzor = r"banan"
tekst = r"gruszkabananjabłkobanan"

print()
print(re.match(wzor, tekst))

#pierwszy if, tu match sprawdza. czy tekst zaczyna się od tego co we wzorze
if re.match(wzor, tekst):
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

#drugi if, tu match sprawdza. czy w tekscie jest to co we wzorze
if re.match(r".*" + wzor + r".*", tekst):
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

#trzeci if
if re.search(wzor, tekst):
    print("Dopasowano - funckja search")
else:
    print("Nie dopasowano!")

#4 if
print(re.findall(wzor, tekst))

#5
dopasowanie = re.search(wzor, tekst)
if dopasowanie:
    print(dopasowanie.group())
    print(dopasowanie.start()) #gdzie dop się zaczyna
    print(dopasowanie.end()) #gdzie dop się kończy
    print(dopasowanie.span())

#6
print(wzor)
print(tekst)
tekst2 = re.sub(wzor, r"jagoda", tekst)
print(tekst2)
