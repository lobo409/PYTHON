numero=int(input('Introduce un numero para calcular su factorial:'))
i=1
factorial=1
while (i <= numero):
    factorial = factorial * i
    i = i + 1
print(factorial)