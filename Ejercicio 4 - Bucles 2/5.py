# Realizar una algoritmo que muestre la tabla de multiplicar  del 3
contador = 0
numero = 3

while contador < 11:
    multiplicacion = contador * numero
    print (f"{numero} x {contador} = {multiplicacion}")
    contador += 1