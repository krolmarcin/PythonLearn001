slownik = {1: "Poniedziałek", 2: "Wtorek", 7: "Niedziela"}

print(slownik[1])
print(slownik[7])
slownik[3] = "Środa"
slownik[4] = False
slownik[5] = 5
print(slownik)
print(slownik[3])
slownik["a"] = 1
print(slownik["a"])
print(slownik)

#print(slownik[8])
print(slownik.get(8, "Nie ma, daję jako nieistniejący"))
print(slownik.get(7, "Opcjonalnie jak nie ma keya w słowniku to jest to"))

print("\nPętla:")
#to wyświetli tylko keys słownika
for l in slownik:
    print(l)

#to też, jak wyżej
print("\nPętla:")
for l in slownik.keys():
    print(l)

#iterowanie po wartościach
print("\nPętla:")
for l in slownik.values():
    print(l)

#usuwanie elementu ze słownika
print("\n----------------------")
print("Uswam ze słownika:", slownik[1])
print(slownik.pop(1))
print(slownik)
