print("Kolejność działań matematycznych:")
print(2 + 2 * 2)
print((2 + 2) * 2)
print("Dzielenie:")
print(5 / 2)
print("Dzielenie bez reszty czyli: //")
print(5 // 2) #bez reszty
print("Mnożenie:")
print(2 * 3)
print(2 ** 3) #potęgowanie
print("Skrócone wartości np. dodawania x:")
x = 5
x = x + 1
print(x)
x += 1
print(x)
# x++ - w Pythonie to błąd
print("Konwersja typów danych:")
a = input("Podaj 1 liczbę: ")
b = input("Podaj 2 liczbę: ")
print("Konkatenacja stringów:")
print(a + b)
# input standardowo podstawia Stringa, poniżej konwersja na integer
print("Dodanie integerów - konwersja")
print(int(a) + int(b))
# konwersja na float
print("Dodanie floatów - konwersja")
print(float(a) + float(b))

print("Teraz dodanie y i z: y = 2, z = 2")
y = 2
z = 2
print("dodanie dwóch floatów, bo y i z jest floatami,a nie stringami:")
print(y + z)
# knwersja na Stringa
print("Konkatencaja dwóch stringów wygląda tak: (konwersja na (str))")
print(str(y) + str(z))

print("to będzie błąd bo nie ma y, bo ją usunięto: del y")
del y
print(str(y) + str(z))
