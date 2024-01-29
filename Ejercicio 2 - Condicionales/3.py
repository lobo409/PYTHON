#Escribe un programa que lea un número e indique si es par o impar
numero1 = int(input("Indique el primer numero:"))
if numero1 % 2 == 0: # El operador % calcula el resto de la división del número ingresado
    print("El numero es par")
else:
    print("El numero es impar")