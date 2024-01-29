# Algoritmo que pida caracteres 20  e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, 
# el programa termina cuando se introduce un espacio.

contador = 0
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
espacio = [' ']

while contador < 20:
    caracter = input("Introduce un caracter:")
    
    if caracter in vocales:
        print(f"La {caracter} es una vocal")
    elif caracter in espacio:
        print("FIN DEL PROGRAMA")
        break
    else:
        print(f"La {caracter} NO es una vocal")