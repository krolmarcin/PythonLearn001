class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + ", mam na imię " + self.name + " i mam " + str(self.age) + " lat."

objekt = Human("Marcin", 39)
print(objekt.name)
print(objekt.przedstawSie("Witam"))

#2obiekt
obiekt2 = Human("Stefan", 18)
obiekt2.name = "Stefan1"
print(obiekt2.przedstawSie())
print(objekt.przedstawSie())
