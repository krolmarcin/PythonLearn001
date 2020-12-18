print(", ".join(["a", "b", "c"]))
print("Witaj Świecie".replace("Witaj", "Cześć"))
print("To jest zdanie".startswith("to")) #podaje True lub False
print("To jest zdanie.".endswith(".")) #podaje True lub False
print("j"in "To jest zdanie.") #podaje True lub False
print("To jest zdanie.".upper())
print("To jest zdanie.".lower())

print("===================")
lista = [10, 20, 26, 36, 40]

if all([i % 2 == 0 for i in lista]):
    print("Wszystkie parzyste")

if any([i % 2 == 0 for i in lista]):
    print("Chociaż 1 liczba jest parzysta w lista")

print("===================")
for i in lista:
    print(i)

for i in enumerate(lista):
    print(i)

for i in enumerate(lista):
    print(i[0] + 1, "-", i[1])
