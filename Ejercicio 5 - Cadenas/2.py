# 2. Escribir por pantalla cada carácter de una cadena introducida por teclado.for y contar el número de caracteres

cadena = input("Ingresa una cadena: ")
contador = 0

for letra in cadena:
    print(letra)
    contador = contador + 1
print(f"El numero de caracteres es {contador}")