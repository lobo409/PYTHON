#Algoritmo que pida dos números e indique si el primero es mayor que el segundo.
numero1 = int(input("Indique el primer numero:"))
numero2 = int(input("Indique el segundo numero:"))
if numero1 == numero2:
        print("Los numero son iguales")
else:
    if numero1 > numero2:
        print("El numero 1 es mayor")
    else:
        print("El numero 1 es menor")