# Zbiory:
liczby1 = {0, 1, 2, 4}
slowa = set(["a", "b", "c"])

print(liczby1)
print(slowa)

liczby1.add(5)
print(liczby1)

liczby1.remove(0)
print(liczby1)

liczby1.pop()
print(liczby1)

liczby1.add(1)
print(liczby1)

#Dodanie drugi raz 5 nic nie da, wartości są unikalne
liczby1.add(5)
print(liczby1)

print(1 in liczby1)
print(3 in liczby1)

print("a" in slowa)

liczby1 = {0, 1, 2, 4, 4}
liczby2 = {3, 4, 5, 6}

print()
print(liczby1)
print(liczby2)
print(liczby1 | liczby2)
# Część wspólna
print(liczby1 & liczby2)
# Odejmowanie zbiorów
print(liczby1 - liczby2)
print(liczby2 - liczby1)
# Różnica symetryczna - powtarzające się elementy są suwane
print(liczby2 ^ liczby1)
