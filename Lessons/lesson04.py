print("Operatory logiczne: AND, OR, NOT")

print("\nzagnieżdżenie if")
wiek = 21
kasa = 49

if wiek >= 18:
    if kasa >= 35:
        print("Możesz wejść do kina")


print("\nOperator logiczny and")
wiek = 21
kasa = 49
if wiek >= 18 and kasa >= 35:
    print("Możesz wejść do kina")


print("\nOperator logiczny or")
wiek = 12
kasa = 5
if wiek <= 12 or kasa >= 30:
        print("Możesz wejść do kina")


print("\nOperator logiczny not")
wiek = 15
kasa = 4
if not wiek > 12 or kasa >= 30:
        print("Możesz wejść do kina")
else:
    print("Nie możesz wejść do kina")

print("\nInne podejście")
if True or False and False:
    print("Prawda")
else:
    print("Fałsz")

print("\nInne podejście z nawiasami ()")
if (True or False) and False:
    print("Prawda")
else:
    print("Fałsz")

print("\nInne podejście z nawiasami () i not")
if (True or False) and not False:
    print("Prawda")
else:
    print("Fałsz")
