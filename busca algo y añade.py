# Pedir al usuario que introduzca la cadena
cadena = input("Introduce una cadena: ")

# Pedir al usuario que introduzca el carácter a buscar
caracter_a_buscar = ","

# Verificar si el carácter está presente en la cadena
if caracter_a_buscar in cadena:
    # Pedir al usuario que introduzca la cadena a añadir después del carácter
    cadena_a_anadir = " "

    # Iterar sobre la cadena para encontrar el carácter y agregar la cadena nueva
    nueva_cadena = ""
    for i in cadena:
        nueva_cadena += i
        if i == caracter_a_buscar:
            nueva_cadena += cadena_a_anadir
    print(f"La nueva cadena es: {nueva_cadena}")
else:
    print(f"No se encontró el carácter '{caracter_a_buscar}' en la cadena.")