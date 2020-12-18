x = True
y = False
print(x)
print(y)

#operator porównania - zwróci True lub False
print(5 == 5)
print(5 == 1)

#różne
print(5 != 1)
print(5 != 5)

#większe
print(5 > 5)
print(5 > 10)

#mniejszy
print(5 < 5)
print(5 < 10)


#większy równy, mniejszy równy
print(5 >= 5)
print(5 >= 10)
print(5 <= 5)
print(5 <= 10)

#instrukcje warunkowe IF
print("instrukcja warunkowa if:")
if 5 == 5:
    print("Prawda: 5 == 5")
else:
    print("Fałsz")
print("Koniec")

#2
if 5 > 10:
    print("Prawda: 5 > 10")
else:
    print("Fałsz: 5 > 10")

#3
x = 10
y = 15

if x > y:
    print("x > y - większe")
elif x < y:
    print("x < y - mniejsze")
else:
    print("x = y - równe")
