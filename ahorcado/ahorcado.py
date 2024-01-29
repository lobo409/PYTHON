import random

palabras = ["python", "programacion", "ahorcado", "juego", "divertido", "codigo"]
palabra = random.choice(palabras)

intentos_maximos = 10
intentos = 0
letras_usadas = []

# CREAR TABLERO
tablero = ["_"] * len(palabra)
while True:
    # IMPRIMIR TABLERO ACTUAL "join para juntar las lineas separadas por espacios eliminando todo lo demas"
    print(" ".join(tablero))

    # PEDIR UNA LETRA
    letra = input("Ingrese una letra: ")
    # SI LA LETRA ESTA EN LETRAS USADAS VUELVE AL PRINCIPIO DEL BUCLE
    if letra in letras_usadas:
        print("Ya has utilizado esa letra, use otra letra")
        continue
    # SI LETRA NO ESTA EN PALABRA AUMENTA INTENTOS, MENSAJE CON INTENTOS QUE QUEDAN Y PINTA DE NUEVO EL TABLERO CON LETRAS
    if letra not in palabra:
        intentos += 1
        print(f"Incorrecto. Te quedan {intentos_maximos - intentos} intentos")
        letras_usadas.append(letra)
    # SI LA LETRA ESTA SE AÑADE A LETRAS USADAS
    else:
        letras_usadas.append(letra)

    # ACTUALIZAR TABLERO CON LAS LETRAS ADIVINADAS - I es posicion y letra_palabra es la letra
    for i, letra_palabra in enumerate(palabra):
        # COMPROBAR SI LA LETRA ESTA ADIVINADA
        if letra_palabra in letras_usadas:
            # PARA LA POSICION DONDE ESTE LA LETRA REMPLAZA POR LA LETRA
            tablero[i] = letra_palabra
    
    if "_" not in tablero:
        print("¡Felicidades! ¡Has adivinado la palabra!")
        break

    if intentos == intentos_maximos:
        print(f"¡Perdiste! La palabra era: {palabra}")
        break