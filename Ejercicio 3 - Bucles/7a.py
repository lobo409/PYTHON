#7.	Mostrar el factorial de un numero que previamente se introduce por teclado(for)
factorial=int(input('Introduce un numero para calcular su factorial:'))
total=1
for i in range(1,factorial + 1):
    total*=i
print(total)
