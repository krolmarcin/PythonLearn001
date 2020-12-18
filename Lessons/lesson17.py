lista = list(range(10))

nowa = [i * 2 for i in lista]
nowa2 = [i + 2 for i in lista if i % 2 == 0] #dodawanie działa po sprawdzeniu ifa:
nowa3 = [i + 1 for i in lista if i % 2 == 0]

print(lista)
print("Nowa lista, arg * 2:", nowa)
print("Nowa2:", nowa2)
print("Nowa3 (nieparzyste bo dodawanie działa po sprawdzeniu if:\n", nowa3)

#Formatowanie ciągów String
argumenty = ["Marcin", 39]
tekst = "Czesc mam na imię {imie} i mam {wiek} lat. \n{imie}.".format(imie = argumenty[0], wiek = argumenty[1])
print(tekst)
