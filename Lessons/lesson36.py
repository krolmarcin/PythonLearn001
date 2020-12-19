# Argumenty fukncji
# arg2 ma domyśly parametr jeśli go nie wywołam
def funkcja(arg1, arg2="World"):
    print(arg1, arg2)

funkcja("Hello")
funkcja("Hi", "Marcin")

# 2. Nowość, funkcja print,
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 3. nowa funkcja z args, *args - nieskończenie wiele
def funkcja1(arg1, arg2="World", *args):
    print(arg1, arg2, args, len(args))
    for x in args:
        print(x)

funkcja1("hi", "man", "!", ":-)")

# 4. kwars - słownik, key-value
def funkcja2(arg1, arg2="World", *args, **kwargs):
    print(arg1, arg2, args, len(args), kwargs)
    for x in args:
        print(x)
    for y in kwargs.values():
        print(y)

funkcja2("hi", "man", "!", ":-)", autor="Marcin", rok=2020)
