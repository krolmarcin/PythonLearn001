plik = open("test19.txt", "r")
tekst = plik.read()
plik.close()

def policz(txt, znak):
    licznik = 0
    for z in txt:
        if z == znak:
            licznik += 1
    return licznik

print(policz(tekst, "o"))
print(policz(tekst, "O"))
print(policz(tekst, "o") + policz(tekst, "O"))
print(policz(tekst.lower(), "o"))

for z in "abcdefghijklmnoprstuwxyz":
    ile = policz(tekst.lower(), z)
    procent = 100 * ile / len(tekst)
    #print(procent)
    print("{0} - {1} - {2}%".format(z.upper(), ile, round(procent, 2)))

