class Human:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Nazywam się " + self.name)

    @classmethod
    def new_human(cls, name):
        return cls(name)

    @staticmethod
    def greet(arg):
        print("Cześć " + arg)

#Human.introduce()
obj = Human("Marcin")
obj.introduce()

h1 = Human.new_human("Mart")
h1.introduce()
h2 = h1.new_human("MartH2")
h2.introduce()

Human.greet("przyjacielu!")
h2.greet("człowieku.")
