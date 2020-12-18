#from random import randint
#
#for i in range(100):
#    print(randint(1, 10))

from random import randint

los = randint(1, 10)
odp = -1
i = 0
print("Zgadnij liczbę z przedzialu 1 - 10")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbę: "))
    if odp > los:
        print("Niesety, wylosowana liczba jest mniejsza od Twojej")
    elif odp < los:
        print("Niesety, wylosowana liczba jest większa od Twojej")
print("Brawo! Odgadłeś za", i, "razem.")
