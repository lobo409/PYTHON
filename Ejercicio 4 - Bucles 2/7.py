'''Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. 
A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número 
(además te dice en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que había generado.'''

import random
numero = random.randint(1, 100)
vidas = 10
contador = 0

while vidas > 0:
    intento = int(input("Ingresa un numero:"))
    
    if intento > numero:
        print("El numero es mas pequeño, sigue intentandolo")
        contador = contador + 1
        vidas = vidas - 1 
        print (f"Te quedan {vidas} vidas")
    elif intento < numero:
        print("El numero es mas mayor, sigue intentandolo")
        contador = contador + 1
        vidas = vidas - 1 
        print (f"Te quedan {vidas} vidas")
    else:
        print(f"Has acertado el numero en {contador} intentos")
        break

if vidas == 0:
    print("Has alcanzado tus intentos. Ejecute de nuevo el programa, siga intentandolo :(")