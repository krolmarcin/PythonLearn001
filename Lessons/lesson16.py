krotka = (2, 4, 8, 16, 32, 64, 128, "abc")
print("Ilość wartości w krotce:", len(krotka))
print("Krotki jak listy liczy się od 0. Krotka to uproszczona lista (jest stała i niezmienna).")
print(krotka[0])
print(krotka[6])
print(krotka)
#nie można przypisać, modyfikować krotki, to błąd w Pythonie
#krotka[0] = 1

print("Ilośc elementów (takich jak po councie):", krotka.count(2))
print("Index: (element tez jest na wartości klucza: key)", krotka.index(64))

print("\nWycinki:")
print(krotka)
print(krotka[0:3])
print(krotka[3:5])
print(krotka[3:6])
#index ktotki w wycinkach od:do = do-1 i nie powodują błędów - out of range
print(krotka[3:7])
print(krotka[0:7])
print(krotka[0:100])
#zamieniona wartość sort liczy od prawej, ale nie od 0, a od 1, ost parametr nie jest wyświetlony czyli nie ma >=
print(krotka[-5:-3]) #to nie sortuje
#skok, tu co drugi elem. 3 wartość to skok, 2 param może być pusty to onzacza koniec tupli
print(krotka[0:8:2])
print(krotka[0::2])
#bez skoku od początkku do końca tupli, 2 param nieobecny/pusty
print(krotka[0:])
#może być tak, od początku do końca
print(krotka[:])
#to sortuje od końca - kolejność odwrotna
print(krotka[::-1])
print(krotka[::-2]) #co drugi element
