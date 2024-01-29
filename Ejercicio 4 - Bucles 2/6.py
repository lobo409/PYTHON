# Realizar una algoritmo que muestre la tabla de multiplicar  de un número solicitado por teclado

contador = 0
numero = int(input("Introduce un numero:"))

while contador < 11:
    multiplicacion = contador * numero
    print (f"{numero} x {contador} = {multiplicacion}")
    contador += 1 