x = 14
y = 0

try:
    lista = []
    print(lista[0])
    print(x + "!")
    print(x/y)
    print("Linijka po błędzie x/y teraz y!=0")
except (ZeroDivisionError, TypeError):
    print("Wystąpił 1 z 2 błędów")
except:
    print("Inny błąd!")
finally:
    print("finally: wykona się zawsze")

print("Dalsze instrukcje...")
