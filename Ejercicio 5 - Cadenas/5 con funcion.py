# 5. Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado. CON FUNCION

cadena_1 = input("Introduce una cadena: ")
cadena_2 = input("Introduce una subcadena: ")

if cadena_1.find(cadena_2):
        print(f"La subcadena '{cadena_2}' está presente en la cadena 1.")
else:
    print(f"La subcadena '{cadena_2}' no está presente en la cadena 1.")