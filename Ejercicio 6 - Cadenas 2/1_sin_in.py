# 1. Debe implementar un algoritmo para la funcion LEN
cadena = input("Introduce una cadena:")
contador = 0

while cadena[contador:]: # [contador:] contador empieza en la posicion 0 y llega hasta el final de la cadena
    contador += 1

print(f"Hay {contador} caracteres")
