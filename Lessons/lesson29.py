# Hermetyzacja w Pythonie to dodanie podłogi, ale to tylko informacja dla developera, że ta zmienna ma być prywatna
# przed zmienną w Javie jest private

class Test:
    __lista = []
    def dodaj(self, arg):
        self.__lista.append(arg)

    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) - 1)
        else:
            return

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj._Test__lista.append("X")
print(obj._Test__lista)
print(obj.zdejmij())
print(obj._Test__lista)
