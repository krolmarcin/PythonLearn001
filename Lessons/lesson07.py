zmienna = 6
zmienna2 = "g"

lista = [1, 2, "c", "d", "e", zmienna, zmienna2, 8, ]
print(lista)
print(lista[0])
print(lista[7])
lista[2] = 3
print(lista)
tekst = "Hello World"
print(tekst)
print(tekst[0])
print(tekst[1])
#listy łączą się, dodają, ale nie na stałe
print(lista + ["i", "j"])
print(lista)
#dodanie do listy "ij" na stałe
lista += ["i", "j"]
print(lista)
#listę można pomnożyć przez jakąś wartość
print(lista * 3)
print("Ilość elementów w liście: ", len(lista))

#zadanie - zrobić pętle while, która tyle ile jest elementów w liście przeszła po niej i wypisała jej wartości
print("\nzadanie - zrobić pętle while, która tyle ile jest elementów w liście przeszła po niej i wypisała jej wartości:")
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

#po zadaniu
#append funkcja, która dołącza(dodaje) do listy na stałe jak wyżej dodałem na stałe
print("\nappend funkcja, która dołącza(dodaje) do listy na stałe jak wyżej dodałem na stałe")
lista.append("k")
print(lista)
print("Ilość elementów w liście: ", len(lista))
lista.append(["12", "ł"])
print(lista)
print("Ilość elementów w liście: ", len(lista))
print("Lista ma", len(lista), "elementów, a pod 12 jest lista")
#lista 2D. dostęp do jej elementów, wiersze i kolumny obrazują to
print(lista[11][0])
print(lista[11][1])
#insert trzeba podać gdzie dodać obiekt,
print("\nDodanie do listy elemntu 3 za trójką, za pomocą lista.insert: ")
lista.insert(3, 3)
print(lista)
print("Ilość elementów w liście: ", len(lista))
#liczenie wystąpień danego elementu(wartości) na liście
print("Ilość trójek: ", lista.count(3))
print("Ilość jedynek: ", lista.count(1))
#kolejna funkcja metod
print("Index:", lista.index("g"))
print("Index:", lista.index(3)) #pierwsze wystąpienie trójki
#wyświetlam listę
print("wyświetlam listę:")
print(lista)
print("Usuwam k (lista.remove\"k\")")
lista.remove("k")
print(lista)
#tworzenie nowej 2 listy z liczbami
print("\nTworzę listę nr 2:")
lista2 = [1, 20, 35, -5, 0]
print(lista2)
print("Wyświetlam wartość min. listy nr 2:", min(lista2))
print("Wyświetlam wartość max. listy nr 2:", max(lista2))
#sortowanie
print("\nlista2", lista2)
lista2.sort()
print("Posortowałem (sort) listę2:", lista2)
#odwracanie
lista2.reverse()
print("Odwróciłem (reverse) listę2:", lista2)
#czyszczenie clear
lista2.clear()
print("Wyczyściłem (clear) listę2:", lista2)
