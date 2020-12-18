print("Funkcja print()")
print("\n")

def funkcja_test():
    print("Funkcja zdefiniowana przeze mnie")

funkcja_test()
funkcja_test()
funkcja_test()

#funkcja dodaj
def dodaj(x):
    print(x + 3)

dodaj(4)

#przeciążona funkcja dodaj (została nadpisana)
def dodaj(x, y):
    print(x + y)

dodaj(3, 4)

#next - domyślny parametr (zawsze na końcu)
def dodaj(x, y = 0):
    print(x + y)

dodaj(7)

#next1
def dodaj(x, y = 1, z = 0):
    print(x + y + z)

dodaj(7)
dodaj(7, 20)
dodaj(7, 20, 22)

#next, jak jest return to trzeba print, return funkcja skoku, zawsze ma końcu
print("zamiast print, return, a wynik to:")
def dodaj(x, y = 1, z = 0):
    print("a wynik to:")
    return x + y + z

print(dodaj(1, 2, 4))
#albo
wynik = dodaj(7, 14, 28)
print(wynik)
