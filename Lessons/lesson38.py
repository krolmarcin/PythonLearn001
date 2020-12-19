# skrócony if
print("Prawda") if 5 > 2 else print("Nieprawda")

#
a = "Parzysta" if 5 % 2 == 0 else "Nieparzysta"
print(a)

#==============
# skrócony else
for i in range(10):
    if i > 5:
        continue
else:
    print("Koniec 1")

# drugie zastosowanie else, else wykona się jeśli pętla nie zostanie przerwana, finally zawsze
try:
    s = 5/0
except ZeroDivisionError:
    print("Błąd")
else:
    print("Koniec 2")
finally:
    print("Finally zawsze :)")
