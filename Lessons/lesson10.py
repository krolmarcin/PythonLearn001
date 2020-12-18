def func(x):
    return x * x

print(func(2))

#czary
zmienna = func
print(zmienna(5))

#next
def func2(f1, x):
    return f1(x) * x

print(func2(func, 5))

#rekursja(rekurencja)
def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)

print(silnia(1))
print(silnia(2))
print(silnia(3))
print(silnia(4))
print(silnia(5))
print(silnia(6))
