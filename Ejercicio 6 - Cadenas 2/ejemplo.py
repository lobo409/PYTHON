cadena_1 = input("Introduce una cadena: ")
cadena_2 = input("Introduce una subcadena: ")

posicion = cadena_1.find(cadena_2) #FIND se utiliza para buscar algo en algo

if posicion != -1:
    print(f"La subcadena '{cadena_2}' está presente en la cadena 1.")
else:
    print(f"La subcadena '{cadena_2}' no está presente en la cadena 1.")
