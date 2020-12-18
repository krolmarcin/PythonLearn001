lista = ["Subskrybuj", "Kanał", "o", "Wszystkim", ]

print("Długość listy:", len(lista))

i = 0
while i < len(lista):
    print(lista[i])
    i += 1

print("\nPętla for...")
for x in lista:
    print(x)

print("\n")
print(list(range(10)))

print("\n")
for y in range(10):
    print(y)

print("\n")
for y in range(1, 11):
    print(y)

print("\n")
for y in range(1, 11, 2):
    print(y)

print("\n")
for y in range(0, 50, 7):
    print(y)
