#Algoritmo que pida un número y diga si es positivo, negativo o 0.
numero1 = int(input("Indique el primer numero:"))
if numero1 > 0:
    print("El numero es positivo")
elif numero1 == 0:
    print("El numero es 0")
else:
    print("el numero es negativo")