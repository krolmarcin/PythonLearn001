class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print("How How")

class Wolf(Dog):
    def getVoice(self):
        print("I'am a wolf,")
        super().voice()

class Cat(Animal):
    def getVoice(self):
        print("Meow Meow")

dog = Dog("Reksio", 7)
print(dog.name)
print(dog.age)
dog.voice()

cat = Cat("Mruczek", 3)
print(cat.name)
print(cat.age)
cat.getVoice()

wolf = Wolf("Geralt", 55)
wolf.getVoice()
print(wolf.name)
