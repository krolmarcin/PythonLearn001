#podejście do while
i = 0

while i < 5:
    print(i)
    i += 1
print("Koniec\n")

#podejście do while z breakiem
i = 0

while True:
    print(i)
    i += 1
    if i >= 10:
        break
print("Koniec\n")

#podejście do while z breakiem wartości parzyste czyli dzieląc na 2 daje nam to resztę 1
i = 0

while True:
    i += 1
    if i % 2 == 1:
        continue
    print(i)
    if i > 10:
        break
print("Koniec")
