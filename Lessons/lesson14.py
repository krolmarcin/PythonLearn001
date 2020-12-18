plik = open("test.txt", "a")
if plik.writable():
    ile = plik.write(input("Wprowadź tekst: ") + "\n")
    print("Zapisano: ", ile)
plik.close()

plik = open("test.txt", "r")

if plik.readable():
    print("Zawartość pliku:")
    for l in plik:
        print(l)
