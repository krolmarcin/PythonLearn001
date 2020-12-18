#Cykl życia obiektu...
class Test:
    def __new__(cls):
        print("Hello Class")

objekt = Test()

#destruktor przeciwieństwo konstruktora, działa w momencie końca życia obiektu,
#wykonuje się na sam koniec, w celu oczyszczenia pamięci, albo jak napiszemy del - zakillujemy go
#Definicja: Obiekt kończy swoje isnienie, kiedy nie posiada żadnej referencji pod żadną zmienną
class Test1:
    def __del__(self):
        print("Bye Class")

objektNowy = Test1()
obj2 = objektNowy
lista = [obj2]
del objektNowy
del obj2
lista[0]
del lista

print("Koniec")
