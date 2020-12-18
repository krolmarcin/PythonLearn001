def funkcja(f, liczba):
    return f(liczba)

print(funkcja(lambda x: x * x, 7))

def kwadrat(x):
    return x * x

print(kwadrat(7))

wyn = (lambda x: x * x)(7)
print(wyn)

lam = lambda x: x * x
print(lam(9))
print(lam(7))

lam2 = lambda x, y: x * y
print(lam2(2, 7))

print((lambda x, y: x + y)(3, 4))
